# !pip install torch

import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple feedforward neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(3, 3)  # 3 input nodes, 3 output nodes

    def forward(self, x):
        return self.fc1(x)

# Create a random tensor of size (1, 3)
input_data = torch.randn(1, 3)

# Initialize the network and optimizer
net = Net()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# Forward pass
output = net(input_data)

# Compute a dummy loss
loss = torch.mean(output)
loss.backward()

# Update the weights
optimizer.step()

print("Output after one forward pass:", output)


# This `example.py` file provides a simple demonstration of defining a neural network, performing a forward pass, computing a loss, and updating the network's weights using gradient descent in PyTorch.

# **Output after one forward pass:** This phrase indicates that the system has processed some data and is now showing the result.

# **tensor([[ 1.5769, -0.4462, -0.4074]]):** A tensor is a fancy term for a multi-dimensional array, similar to a list of numbers. Here, the tensor contains three numbers: 1.5769, -0.4462, and -0.4074. These numbers are the processed values after the data has gone through the system.

# **grad_fn=<AddmmBackward0>:** This part might sound a bit technical, but it's essentially a note to say that this tensor has some special properties related to how it was computed. Specifically, it remembers the operations that produced it, which can be useful for certain advanced tasks. For our purposes, we can think of it as a label or tag attached to the tensor.

# In simpler terms: The system took some input data, processed it, and gave us a list of three numbers as the result. The extra label at the end is just a technical detail about how the numbers were computed.