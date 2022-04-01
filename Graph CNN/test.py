import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import torch



MUT_LABEL_ENC = pd.Series(data = ["C","O", "Cl","H","N","F","Br","S","P","I","Na","K","Li","Ca"])
print("Number of different elements: ", len(MUT_LABEL_ENC))

from torch_geometric.datasets import TUDataset

# Load the dataset
dataset = TUDataset(
    root=".", name="Mutagenicity",
    transform=None,
).shuffle()

print(f'Dataset: {dataset}:')
print('====================')
print(f'Number of graphs: {len(dataset)}')
print(f'Number of features: {dataset.num_features}')
print(f'Number of classes: {dataset.num_classes}')
print(f'Samples per class: {[ np.sum([1 for graph in dataset if graph.y == i ]) for i in range(dataset.num_classes) ]}')

