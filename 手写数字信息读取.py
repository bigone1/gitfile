import gzip, os
import numpy as np

location = input('The directory of MNIST dataset: ')
path = os.path.join(location, 'train-images-idx3-ubyte.gz')
try:
    with gzip.open(path, 'rb') as fi:
        data_i = np.frombuffer(fi.read(), dtype=np.int8, offset=16)
        images_flat_all = data_i.reshape(-1, 784)
        print(images_flat_all)
        print('----- Separation -----')
        print('Size of images_flat: ', len(images_flat_all))
except:
    print("The file directory doesn't exist!")
	
path_label = os.path.join(location, 'train-labels-idx1-ubyte.gz')
with gzip.open(path_label, 'rb') as fl:
    data_l = np.frombuffer(fl.read(), dtype=np.int8, offset=8)

print(data_l)
print('----- Separation -----')
print('Size of images_labels: ', len(data_l), type(data_l[0]))