import os
import glob
import torch
import numpy as np
import pandas as pd
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import torch.nn.functional as F
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets, models, transforms
from PIL import Image

class Cnn(nn.Module):
    def __init__(self):
        super(Cnn,self).__init__()
        
        self.conv1 = nn.Sequential(
            nn.Conv2d(3,16,kernel_size=3, padding=0,stride=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        
        self.conv2 = nn.Sequential(
            nn.Conv2d(16,32, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2)
            )
        
        self.conv3 = nn.Sequential(
            nn.Conv2d(32,64, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.linear1 = nn.Linear(3*3*64,10)
        self.linear2 = nn.Linear(10,2)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        
        
    def forward(self,x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.conv3(out)
        out = out.view(out.size(0),-1)
        out = self.relu(self.linear1(out))
        out = self.linear2(out)
        out = self.dropout(out)
        return out

class dataset(torch.utils.data.Dataset):
    def __init__(self,file_list,transform=None):
        self.file_list = file_list
        self.transform = transform
        
    def __len__(self):
        return len(self.file_list)
    
    def __getitem__(self,index):
        image_path = self.file_list[index]
        image = Image.open(image_path)
        image_return = self.transform(image)

        label = image_path.split('\\')[1].split('.')[0]
        if label == 'dog':
            label = 1
        elif label == 'cat':
            label = 0
            
        return image_return,label

if __name__ == '__main__':
    lr = 0.001
    batch_size = 100 
    epochs = 10 

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    #Seed
    '''
    torch.manual_seed(1980)
    if device =='cuda':
        torch.cuda.manual_seed_all(1980)
    '''

    #Directories
    train_dir = './train'
    test_dir = './test'

    train_list = glob.glob(os.path.join(train_dir,'*.jpg'))
    test_list = glob.glob(os.path.join(test_dir, '*.jpg'))

    random_idx = np.random.randint(1,25000,size=10)

    fig = plt.figure()
    i=1
    for idx in random_idx:
        ax = fig.add_subplot(2,5,i)
        img = Image.open(train_list[idx])
        plt.imshow(img)
        i+=1

    #Environment tests
    #plt.axis('off')
    #plt.show()
    #print(train_list[0])
    #print(train_list[0].split('\\')[1].split('.')[0])
    #print(len(train_list), len(test_list))

    train_list, val_list = train_test_split(train_list, test_size=0.2)

    #data Augumentation
    train_transforms =  transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
        ])

    val_transforms = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
        ])


    test_transforms = transforms.Compose([   
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
        ])


    train_data = dataset(train_list, transform=train_transforms)
    test_data = dataset(test_list, transform=test_transforms)
    val_data = dataset(val_list, transform=test_transforms)

    train_loader = torch.utils.data.DataLoader(dataset = train_data, batch_size=batch_size, shuffle=True )
    test_loader = torch.utils.data.DataLoader(dataset = test_data, batch_size=batch_size, shuffle=True)
    val_loader = torch.utils.data.DataLoader(dataset = val_data, batch_size=batch_size, shuffle=True)

    model = Cnn().to(device)
    model.train()

    optimizer = optim.Adam(params = model.parameters(),lr = lr)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        epoch_loss = 0
        epoch_accuracy = 0

        for data, label in train_loader:
            label = torch.from_numpy(np.array(label))
            data = data.to(device)
            label = label.to(device)
            
            output = model(data)
            loss = criterion(output, label)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            acc = ((output.argmax(dim=1) == label).float().mean())
            epoch_accuracy += acc/len(train_loader)
            epoch_loss += loss/len(train_loader)
            
        print('Epoch : {}, train accuracy : {}, train loss : {}'.format(epoch+1, epoch_accuracy,epoch_loss))
        
        
        with torch.no_grad():
            epoch_val_accuracy=0
            epoch_val_loss =0
            for data, label in val_loader:
                data = data.to(device)
                label = label.to(device)
                
                val_output = model(data)
                val_loss = criterion(val_output,label)
                
                acc = ((val_output.argmax(dim=1) == label).float().mean())
                epoch_val_accuracy += acc/ len(val_loader)
                epoch_val_loss += val_loss/ len(val_loader)
                
            print('Epoch : {}, val accuracy : {}, val loss : {}'.format(epoch+1, epoch_val_accuracy,epoch_val_loss))

    dog_probs = []
    model.eval()
    with torch.no_grad():
        for data, fileid in test_loader:
            data = data.to(device)
            preds = model(data)
            preds_list = F.softmax(preds, dim=1)[:, 1].tolist()
            dog_probs += list(zip(list(fileid), preds_list))

    dog_probs.sort(key = lambda x : int(x[0]))
    idx = list(map(lambda x: x[0],dog_probs))
    prob = list(map(lambda x: x[1],dog_probs))
    submission = pd.DataFrame({'id':idx,'label':prob})
    submission.to_csv('result.csv',index=False)
