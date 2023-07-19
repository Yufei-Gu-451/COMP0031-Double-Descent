import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import csv
import os

DATASET = 'CIFAR-10'

N_EPOCHS = 4000
N_SAMPLES = 4000
BATCH_SIZE = 64

TEST_GROUP = 0
TEST_NUMBER = 0

label_noise_ratio = 0.2
gap = 100

directory = f"assets/{DATASET}/N=%d-3d/TEST-%d/epoch=%d-noise-%d-model-%d" \
                    % (N_SAMPLES, TEST_GROUP, N_EPOCHS, label_noise_ratio * 100, TEST_NUMBER)

dictionary_path = os.path.join(directory, "dictionary.csv")
plots_path = os.path.join(directory, 'plots')

if not os.path.isdir(plots_path):
    os.mkdir(plots_path)

index, hidden_units, parameters, epochs = [], [], [], []
train_losses, train_accs, test_losses, test_accs = [], [], [], []

with open(dictionary_path, "r", newline="") as infile:
    # Create a reader object
    reader = csv.DictReader(infile)

    i = -1
    for row in reader:
        #if row['Hidden Neurons'] == '50': break

        if i == -1 or n == N_EPOCHS // gap:
            hidden_units.append([])
            parameters.append([])
            epochs.append(([]))
            train_losses.append([])
            train_accs.append([])
            test_losses.append([])
            test_accs.append([])
            i, n = i + 1, 0

        hidden_units[i].append(int(row['Hidden Neurons']))
        parameters[i].append(int(row['Parameters']))
        epochs[i].append(int(row['Epoch']))
        train_losses[i].append(float(row['Train Loss']))
        train_accs[i].append(float(row['Train Accuracy']))
        test_losses[i].append(float(row['Test Loss']))
        test_accs[i].append(float(row['Test Accuracy']))

        n += 1

hidden_units = np.flipud(np.array(hidden_units))
parameters = np.flipud(np.array(parameters))
epochs = np.array(epochs)
train_losses = np.flipud(np.array(train_losses))
train_accs = np.flipud(np.array(train_accs))
test_losses = np.flipud(np.array(test_losses))
test_accs = np.flipud(np.array(test_accs))

print(hidden_units)

my_col = cm.jet(test_accs/np.amin(test_accs))

fig = plt.figure(figsize=(15, 10))
ax = plt.axes(projection='3d')
ax.plot_surface(parameters, epochs, train_losses, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('Number of Parameters')
plt.ylabel('Number of Epochs')
ax.set_zlabel('Train Losses')
plt.title('Double Descent on MNIST (n = 4×10ˆ3,d = 784,K = 10)')
plt.savefig(os.path.join(plots_path, 'Train_Losses-Parameters.png'))

fig2 = plt.figure(figsize=(15, 10))
ax = plt.axes(projection='3d')
ax.plot_surface(parameters, epochs, test_losses, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('Number of Parameters')
plt.ylabel('Number of Epochs')
ax.set_zlabel('Test Losses')
plt.title('Double Descent on MNIST (n = 4×10ˆ3,d = 784,K = 10)')
plt.savefig(os.path.join(plots_path, 'Test_Losses-Parameters.png'))