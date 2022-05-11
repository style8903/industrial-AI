import os
import numpy as np
import torch.nn as nn
import torch.onnx
from torchvision import models
from torchvision import transforms
import onnx
from onnx import shape_inference
import onnx.numpy_helper as numpy_helper
from efficientnet_pytorch import EfficientNet
import cv2
from PIL import Image


# CreateNetwork should be modified by custom deep-learning model
def CreateNetwork():
    net = EfficientNet.from_pretrained('efficientnet-b0', num_classes=8)
    path = "test1_best_model.pt"
    net.set_swish(memory_efficient=False)
    net.load_state_dict(torch.load(path))
    return net


def compare_two_array(actual, desired, layer_name, rtol=1e-7, atol=0):
    flag = False
    try:
        np.testing.assert_allclose(actual, desired, rtol=rtol, atol=atol)
        print(layer_name + ": no difference.")
    except AssertionError as msg:
        print(layer_name + ": Error.")
        print(msg)
        flag = True
    return flag


# parameters
channel = 3
height = 224
width = 224
onnx_path = "my_model7.onnx"

# ① 사용할 딥러닝 네트워크를 불러온 뒤 평가 모드로 설정합니다.
net = CreateNetwork()
net.eval()

# ② torch 모델을 이용하여 onnx 모델을 생성합니다.
# (B, C, H, W) 의 dimension을 가지는 것으로 가정함
dummy_data = torch.empty(1, channel, height, width, dtype=torch.float32)
torch.onnx.export(net, dummy_data, onnx_path, input_names=['input'], output_names=['output'], verbose=True)

# ③ 생성한  onnx 모델을 다시 블루어와서 torch 모델과 onnx 모델의 weight를 비교합니다.
# 입력 받은 onnx 파일 경로를 통해 onnx 모델을 불러옵니다.
onnx_model = onnx.load(onnx_path)

# onnx 모델의 정보를 layer 이름 : layer값 기준으로 저장합니다.
onnx_layers = dict()
for layer in onnx_model.graph.initializer:
    onnx_layers[layer.name] = numpy_helper.to_array(layer)

# torch 모델의 정보를 layer 이름 : layer값 기준으로 저장합니다.
torch_layers = {}
for layer_name, layer_value in net.named_modules():
    torch_layers[layer_name] = layer_value

# onnx와 torch 모델의 성분은 1:1 대응이 되지만 저장하는 기준이 다릅니다.
# onnx와 torch의 각 weight가 1:1 대응이 되는 성분만 필터합니다.
onnx_layers_set = set(onnx_layers.keys())
# onnx 모델의 각 layer에는 .weight가 suffix로 추가되어 있어서 문자열 비교 시 추가함
torch_layers_set = set([layer_name + ".weight" for layer_name in list(torch_layers.keys())])
filtered_onnx_layers = list(onnx_layers_set.intersection(torch_layers_set))

difference_flag = False
for layer_name in filtered_onnx_layers:
    onnx_layer_name = layer_name
    torch_layer_name = layer_name.replace(".weight", "")
    onnx_weight = onnx_layers[onnx_layer_name]
    torch_weight = torch_layers[torch_layer_name].weight.detach().numpy()
    flag = compare_two_array(onnx_weight, torch_weight, onnx_layer_name)
    difference_flag = True if flag == True else False

# ④ onnx 모델에 기존 torch 모델과 다른 weight가 있으면 전체 update를 한 후 새로 저장합니다.
if difference_flag:
    print("update onnx weight from torch model.")
    for index, layer in enumerate(onnx_model.graph.initializer):
        layer_name = layer.name
        if layer_name in filtered_onnx_layers:
            onnx_layer_name = layer_name
            torch_layer_name = layer_name.replace(".weight", "")
            onnx_weight = onnx_layers[onnx_layer_name]
            torch_weight = torch_layers[torch_layer_name].weight.detach().numpy()
            copy_tensor = numpy_helper.from_array(torch_weight, onnx_layer_name)
            onnx_model.graph.initializer[index].CopyFrom(copy_tensor)

    print("save updated onnx model.")
    onnx_new_path = os.path.dirname(os.path.abspath(onnx_path)) + os.sep + "updated_" + os.path.basename(onnx_path)
    onnx.save(onnx_model, onnx_new_path)

# ⑤ 최종적으로 저장된 onnx 모델을 불러와서 shape 정보를 추가한 뒤 다시 저장합니다.
if difference_flag:
    onnx.save(onnx.shape_inference.infer_shapes(onnx.load(onnx_new_path)), onnx_new_path)
else:
    onnx.save(onnx.shape_inference.infer_shapes(onnx.load(onnx_path)), onnx_path)

import onnxruntime

session = onnxruntime.InferenceSession("my_model7.onnx")

input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

image_name = "test_img3.jpg"

img = cv2.imread(image_name).astype(np.float32)

# image resize가 필요한 경우 아래와 같이 적용
#img = cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)
img = cv2.resize(img, (width, height))

# image 스케일을 [0, 255] → [0, 1]로 변경 이 필요하면 변경한다.
img = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
# image의 normalization이 필요하면 적용한다.

# [height, width, channel] → [channel, height, width]
img = img.transpose((2, 1, 0))

# [channel, height, width] → [1, channel, height, width] (1은 batch를 의미함)
img = np.expand_dims(img, axis=0)

# out : [1, 출력 shape] (1은 batch를 의미함)
out = session.run([output_name], {input_name : img})[0]
# out : 출력 shape (batch dimension 제거)
out = out.squeeze(0)

img = torch.from_numpy(img)
output = net(img)

tfms = transforms.Compose([transforms.Resize(224), transforms.ToTensor()])
                        #   transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),])
img2 = tfms(Image.open('test_img2.jpg')).unsqueeze(0)
out2 = net(img2)

print(output)
print(out)
print(out2)