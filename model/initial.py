# Following https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html

# Check out https://developer.apple.com/metal/ on the MacBook

# Don't forget https://paperswithcode.com/trends

import torch
from torch import nn

# There are many different libraries such as TorchText, TorchVision and TorchAudio
from torchvision.transforms import ToTensor

# Datasets store samples and their corresponding labels
from torchvision import datasets
# DataLoaders wrap an iterable around the Dataset
from torch.utils.data import DataLoader


# torchvision.datasets contains many sample Datasets
# Download training data from open datasets
training_data = datasets.FashionMNIST(
        root='data',
        train=True,
        download=True
        transform=ToTensor()
)

# Download test data from open datasets
test_data = datasets.FashionMNIST(
        root='data',
        train=False,
        download=True
        transform=ToTensor()
)


