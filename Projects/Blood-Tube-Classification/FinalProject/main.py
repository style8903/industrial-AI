from efficientnet_pytorch import EfficientNet
import numpy as np
import json
from PIL import Image
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
import time
import os
import copy
import random
import pandas as pd
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from torch.utils.data import Subset


#############################################학습 함수########################################################
def train_model(model, criterion, optimizer, scheduler, num_epochs=25):
    since = time.time()
    data_path = 'E:\FinalProject\my_data'

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0
    train_loss, train_acc, valid_loss, valid_acc = [], [], [], []

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        # Each epoch has a training and validation phase
        for phase in ['train', 'valid']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()  # Set model to evaluate mode

            running_loss, running_corrects, num_cnt = 0.0, 0, 0

            # Iterate over data.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    # backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                # statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
                num_cnt += len(labels)
            if phase == 'train':
                scheduler.step()

            epoch_loss = float(running_loss / num_cnt)
            epoch_acc = float((running_corrects.double() / num_cnt).cpu() * 100)

            if phase == 'train':
                train_loss.append(epoch_loss)
                train_acc.append(epoch_acc)
            else:
                valid_loss.append(epoch_loss)
                valid_acc.append(epoch_acc)
            print('{} Loss: {:.2f} Acc: {:.1f}'.format(phase, epoch_loss, epoch_acc))

            # deep copy the model
            if phase == 'valid' and epoch_acc > best_acc:
                best_idx = epoch
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())
                #                 best_model_wts = copy.deepcopy(model.module.state_dict())
                print('==> best model saved - %d / %.1f' % (best_idx, best_acc))

##################################################################추가 함수############################################################################
            # #if (epoch%5 == 4):
            # if phase == 'valid':
            #     test_and_visualize_model(model, phase='test')
            #     torch.save(model.state_dict(), f"{data_path}/run/{epoch}.pth")
    ##################################################################추가 함수############################################################################

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
    print('Best valid Acc: %d - %.1f' % (best_idx, best_acc))

    # load best model weights
    model.load_state_dict(best_model_wts)
    torch.save(model.state_dict(), 'test3_best_model.pt')
    torch.save(model, 'test3-1_best_model.pt')
    print('model saved')
    return model, best_idx, best_acc, train_loss, train_acc, valid_loss, valid_acc

############################################결과 Visualation 함수##################################################
def test_and_visualize_model(model, phase='test', num_images=4):
    # phase = 'train', 'valid', 'test'

    was_training = model.training
    model.eval()
    fig = plt.figure()
    ##############################################
    predlist = []
    truelist = []
    ##############################################

    running_loss, running_corrects, num_cnt = 0.0, 0, 0

    with torch.no_grad():
        for i, (inputs, labels) in enumerate(dataloaders[phase]):
            inputs = inputs.to(device)
            labels = labels.to(device)

            outputs = model(inputs)

            _, preds = torch.max(outputs, 1)

            loss = criterion(outputs, labels)  # batch의 평균 loss 출력

            ##################################################
            pred_output = preds.data.cpu().numpy()
            predlist.extend(pred_output)
            true_label = labels.data.cpu().numpy()
            truelist.extend(true_label)
            ##################################################

            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)
            num_cnt += inputs.size(0)  # batch size

        #         if i == 2: break

        test_loss = running_loss / num_cnt
        test_acc = running_corrects.double() / num_cnt
        print('test done : loss/acc : %.2f / %.1f' % (test_loss, test_acc * 100))

        #########################################
        my_label_list = ('type1', 'type2', 'type3', 'type4', 'type5', 'type6', 'type7', 'type8')
        print("Test Data Amount: " + str(len(predlist)) + ", " + str(len(truelist)))
        cf_matrix = confusion_matrix(truelist, predlist, normalize='true')
        df_cm = pd.DataFrame(cf_matrix, index=[i for i in my_label_list], columns=[i for i in my_label_list])
        plt.figure(figsize=(12,7))
        sn.heatmap(df_cm, annot=True)
        plt.savefig('output.png')
        #########################################

    model.train(mode=was_training);  # 다시 train모드로

###################################################################################################################
if __name__ == '__main__':
    model_name = 'efficientnet-b0'  # b5
    model = EfficientNet.from_name('efficientnet-b0')

    image_size = EfficientNet.get_image_size(model_name)
    print(image_size)

    #분류 갯수 설정
    model = EfficientNet.from_pretrained(model_name, num_classes=8)
    batch_size  = 8
    random_seed = 123
    random.seed(random_seed)
    torch.manual_seed(random_seed)
    class_names = {
        "0": "type1",
        "1": "type2",
        "2": "type3",
        "3": "type4",
        "4": "type5",
        "5": "type6",
        "6": "type7",
        "7": "type8"
    }

    ## 데이터셋 경로 설정
    data_path = 'E:\FinalProject\my_data'
    my_dataset = datasets.ImageFolder(
                                    data_path,
                                    transforms.Compose([
                                        transforms.Resize((224, 224)),
                                        transforms.ToTensor()
                                    ]))

    ## data split
    #전체 데이터 중 40%를 test data로 분류
    train_idx, tmp_idx = train_test_split(list(range(len(my_dataset))), test_size=0.4, random_state=random_seed)
    datasets = {}
    datasets['train'] = Subset(my_dataset, train_idx)
    tmp_dataset = Subset(my_dataset, tmp_idx)

    #test data중 50%를 test, 나머지를 val로 분류
    val_idx, test_idx = train_test_split(list(range(len(tmp_dataset))), test_size=0.5, random_state=random_seed)
    datasets['valid'] = Subset(tmp_dataset, val_idx)
    datasets['test'] = Subset(tmp_dataset, test_idx)

    ## data loader 선언
    dataloaders, batch_num = {}, {}
    dataloaders['train'] = torch.utils.data.DataLoader(datasets['train'],
                                                  batch_size=batch_size, shuffle=True,
                                                  num_workers=2) #num_workers는 cpu에서 사용할 코어 갯수
    dataloaders['valid'] = torch.utils.data.DataLoader(datasets['valid'],
                                                  batch_size=batch_size, shuffle=False,
                                                  num_workers=2)
    dataloaders['test']  = torch.utils.data.DataLoader(datasets['test'],
                                                  batch_size=batch_size, shuffle=False,
                                                  num_workers=2)
    batch_num['train'], batch_num['valid'], batch_num['test'] = len(dataloaders['train']), len(dataloaders['valid']), len(dataloaders['test'])
    print('batch_size : %d,  tvt : %d / %d / %d' % (batch_size, batch_num['train'], batch_num['valid'], batch_num['test']))

    #cuda 사용 여부
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  # set gpu
    model = model.to(device)
    #손실함수
    criterion = nn.CrossEntropyLoss()
    #최적화함수
    optimizer_ft = optim.SGD(model.parameters(),
                             lr = 0.05,
                             momentum=0.9,
                             #오비피팅 방지. 특정 네트워크의 가중치 값이 클 경우 패널티처리. L2 Regularization. 가중치가 커지지 않도록
                             weight_decay=1e-4)

    lmbda = lambda epoch: 0.98739
    exp_lr_scheduler = optim.lr_scheduler.MultiplicativeLR(optimizer_ft, lr_lambda=lmbda)
    #학습시작
    model, best_idx, best_acc, train_loss, train_acc, valid_loss, valid_acc = train_model(model, criterion, optimizer_ft, exp_lr_scheduler, num_epochs=10)

    #결과 그래프 그리기
    print('best model : %d - %1.f / %.1f'%(best_idx, valid_acc[best_idx], valid_loss[best_idx]))
    fig, ax1 = plt.subplots()

    ax1.plot(train_acc, 'b-')
    ax1.plot(valid_acc, 'r-')
    plt.plot(best_idx, valid_acc[best_idx], 'ro')
    ax1.set_xlabel('epoch')
    # Make the y-axis label, ticks and tick labels match the line color.
    ax1.set_ylabel('acc', color='k')
    ax1.tick_params('y', colors='k')

    ax2 = ax1.twinx()
    ax2.plot(train_loss, 'g-')
    ax2.plot(valid_loss, 'k-')
    plt.plot(best_idx, valid_loss[best_idx], 'ro')
    ax2.set_ylabel('loss', color='k')
    ax2.tick_params('y', colors='k')

    fig.tight_layout()
    plt.show()

    #visualation
    test_and_visualize_model(model, phase='test')