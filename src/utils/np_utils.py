import numpy as np
from core.config import Config
import os
import sys
sys.path.append("../../")
from src.FLAGS_DEFINE import *


def cartesian_product(arrays):
    la = len(arrays)
    dtype = arrays[0].dtype
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[..., i] = a
    return arr.reshape(-1, la)


def convert_npy_file_to_txt_file(src, dst):
    data = np.load(src)
    print('data.shape =', data.shape)
    shape_len = len(data.shape)
    data = data.tolist()

    with open(dst, 'w') as writer:
        if shape_len == 1:
            for x in data:
                writer.write('%.10f\n' % (x))
        else:
            for row_data in data:
                writer.write(' '.join(['%.10f' % (i) for i in row_data]) + '\n')

def check_order(mappings):
    count = 0
    for i in range(mappings.shape[0] - 1):
        if mappings[i] > mappings[i + 1]:
            print(i, mappings[i], mappings[i + 1])
            count += 1
    print('error-count =', count)

def check_multi_dim_data_order(data, labels=None):
    if labels is not None:
        idxes = np.argsort(labels)
        data = data[idxes]

    N = data.shape[0]
    flag = True
    for i in range(N):
        x_i = data[i, 0]
        y_i = data[i, 1]
        for j in range(i, N):
            x_j = data[j, 0]
            y_j = data[j, 1]
            if x_i > x_j and y_i > y_j:
                print('i =', i, ', j =', j, data[i], data[j])
                flag = False

    return flag

def check_split_points(data):
    flag = True
    if len(data.shape) == 1:
        data = np.reshape(data, [1, -1])

    N = data.shape[0]
    for i in range(N):
        data_i = data[i]
        for j in range(data_i.shape[0] - 1):
            if data_i[j] >= data_i[j + 1]:
                print(i, j, data_i[j], data_i[j + 1])
                flag = False


    return flag