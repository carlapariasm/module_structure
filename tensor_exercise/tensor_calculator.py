import torch

__all__ = ['TensorCalculator']


class TensorCalculator():

    def __init__(self):
        return None

    def tensor_zeros(self, dim_x, dim_y):
        zeros = torch.zeros([dim_x, dim_y])
        return zeros

    def tensor_ones(self, dim_x, dim_y):
        ones = torch.ones([dim_x, dim_y])
        return ones

    def tensor_random(self, dim_x, dim_y):
        random = torch.rand([dim_x, dim_y])
        return random

    def tensor_sum(self, t1, t2):
        if t1.size() != t2.size():
            print("Error: Both tensors must have the same size.")
            return None
        else:
            sum_tensors = torch.add(t1, t2)
            return sum_tensors

    def tensor_product(self, t1, t2):
        if t1.size() != t2.size():
            print("Error: Both tensors must have the same size.")
            return None
        else:
            product_tensors = torch.mul(t1, t2)
            return product_tensors

    def tensor_transpose(self, t):
        if t.size(0) != t.size(1):
            print("Error: The tensor must be square.")
            return None
        else:
            transpose_tensor = torch.transpose(t, 0, 1)
            return transpose_tensor

    def tensor_subtract(self, t1, t2):
        if t1.size() != t2.size():
            print("Error: Both tensors must have the same size.")
            return None
        else:
            subtraction_tensor = torch.sub(t1, t2)
            return subtraction_tensor
