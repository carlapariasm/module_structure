# TensorCalculator
TensorCalculator is a simple Python library for performing basic operations on 2-dimensional tensors using PyTorch. This library provides functions to create tensors filled with zeros, ones, or random values, as well as performing operations such as addition, subtraction, multiplication, and transpose.

# Installation
To use TensorCalculator, you'll need to have PyTorch installed on your system. You can install it using pip: pip install torch

Once you have PyTorch installed, you can simply copy the TensorCalculator class from this repository into your project.

# Usage
Import the TensorCalculator class into your Python script: from tensor_calculator import TensorCalculator

Initialize a TensorCalculator object: calculator = TensorCalculator()

# Creating Tensors
You can create tensors filled with zeros, ones, or random values using the following methods:

dim_x, dim_y = 3, 4 zeros_tensor = calculator.tensor_zeros(dim_x, dim_y) ones_tensor = calculator.tensor_ones(dim_x, dim_y) random_tensor = calculator.tensor_random(dim_x, dim_y)

# Basic Tensor Operations
Perform basic tensor operations such as addition, subtraction, multiplication, and transpose:

tensor1 = torch.rand([dim_x, dim_y]) tensor2 = torch.rand([dim_x, dim_y])

Add two tensors sum_result = calculator.tensor_sum(tensor1, tensor2)

Subtract two tensors subtraction_result = calculator.tensor_subtract(tensor1, tensor2)

Multiply two tensors product_result = calculator.tensor_product(tensor1, tensor2)

Transpose a tensor transpose_result = calculator.tensor_transpose(tensor1) Note that the tensors passed to the operations must have the same size, and for transposition, the input tensor must be square.

# Error Handling
The library includes error handling for cases where the input tensors do not meet the requirements, such as size mismatch for addition, subtraction, and multiplication, or non-square tensor for transposition.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
