import matplotlib.pyplot as plt
import os
import re

epochs = 400
directory = 'assets/weight_reuse_case/epoch=%d/plots' % epochs
input_file = 'assets/weight_reuse_case/epoch=%d/epoch=%d.txt' % (epochs, epochs)

if not os.path.isdir(directory):
    os.mkdir(directory)

if __name__ == '__main__':
    array = []
    f = open(input_file, 'r')
    for line in f:
        pair = re.findall(r"(\d*\.*\d+)", line)
        print(pair)
        array.append(pair)

    hidden_units, parameters = [], []
    train_losses, train_accs, test_losses, test_accs = [], [], [], []

    for pair in array:
        hidden_units.append(float(pair[0]))
        train_losses.append(float(pair[1]))
        train_accs.append(float(pair[2]))
        test_losses.append(float(pair[3]))
        test_accs.append(float(pair[4]))

    for hidden_unit in hidden_units:
        parameters.append(784 * hidden_unit + hidden_unit * 10)

    plt.figure()
    plt.plot(hidden_units, train_losses, marker='o', label='train')
    plt.plot(hidden_units, test_losses, marker='o', label='test')
    plt.xlabel('Number of Hidden Units')
    plt.ylabel('MSE loss')
    plt.title('Double Descent Curve')
    plt.savefig(os.path.join(directory, 'MSE-Neurons.png'))

    plt.figure()
    plt.plot(parameters, train_losses, marker='o', label='train')
    plt.plot(parameters, test_losses, marker='o', label='test')
    plt.xlabel('Number of Model Parameters')
    plt.ylabel('MSE loss')
    plt.title('Double Descent Curve')
    plt.savefig(os.path.join(directory, 'MSE-Parameters.png'))

    plt.figure()
    plt.plot(hidden_units, train_accs, marker='o', label='train')
    plt.plot(hidden_units, test_accs, marker='o', label='test')
    plt.xlabel('Number of Hidden Units')
    plt.ylabel('Accuracy')
    plt.title('Double Descent Curve')
    plt.savefig(os.path.join(directory, 'Accuracy-Neurons.png'))

    plt.figure()
    plt.plot(parameters, train_accs, marker='o', label='train')
    plt.plot(parameters, test_accs, marker='o', label='test')
    plt.xlabel('Number of Model Parameters')
    plt.ylabel('MSE loss')
    plt.title('Double Descent Curve')
    plt.savefig(os.path.join(directory, 'Accuracy-Parameters.png'))