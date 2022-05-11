import torch.onnx
from torch.autograd import Variable
import torch
import torchvision
from efficientnet_pytorch import EfficientNet
import onnx
import onnxruntime
import cv2

device = torch.device("cpu")
model = EfficientNet.from_pretrained('efficientnet-b0', num_classes=8)
path = "test2_best_model.pt"
model.set_swish(memory_efficient=False)
model.load_state_dict(torch.load(path))
model.to(device)
model.eval()


dummy_input = torch.empty(1, 3, 224,224, dtype=torch.float32)
dummy_ouput = model(dummy_input)
ip_names = ["input"]
op_names = ["output"]
print("Input is valid")

torch.onnx.export(model, dummy_input, "my_model4.onnx", opset_version= 9,verbose=True, input_names=ip_names, output_names=op_names)
#torch.onnx.export(model, dummy_input, "my_model5.onnx")