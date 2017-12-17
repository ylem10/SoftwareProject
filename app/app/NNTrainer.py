# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 18:19:40 2017

数据矩阵的结构为：[n, m], 其中n为数据的特征维度，m为数据的个数（items）
标签矩阵的结构为：[1, m], 其中m未数据的个数（items）
神经网络的结构为：(linear->relu)*(L-1) -> (linear->sigmoid) -> prob
                    
##读取写入数据  to  excel
@author: liutao
"""

import numpy as np
import xlrd
import math
import matplotlib.pyplot as plt

np.random.seed(43)

class NNTrainer:   #用于用户训练的类
    def __init__(self, train_source_path, layer_dims, learn_rate = 0.1, mini_batch_size = 1024, iteration = 5000, show_cost = True):
        self.train_source_path = train_source_path
        self.layer_dims = layer_dims
        self.learn_rate = learn_rate
        self.show_cost = show_cost
        self.mini_batch_size = mini_batch_size
        self.cost_list = []
        self.trained_parameters_path = '../model/trained-parameters.txt'  #save trained-parameters
        self.iteration = iteration
        
    def read_train_data_and_label(self):
        bk = xlrd.open_workbook(self.train_source_path)
        try:
            sh = bk.sheet_by_name("Sheet1")
        except:
            print ("no sheet in %s named Sheet1" %(self.train_source_path))
        ncols = sh.ncols
        nrows = sh.nrows
        data = []
        for i in range(1, nrows):
            for j in range(ncols-1):
                data.append(sh.cell_value(i, j))      
        #def normalization_data(data):
           # pass
        data = np.reshape(data, (nrows-1, ncols-1)).T
        label = []
        for i in range(1, nrows):
            for j in range(ncols-1, ncols):
                label.append(sh.cell_value(i, j))
        label = np.reshape(label, (1, nrows-1))
        
        #归一化数据
#        mean_X = np.reshape(np.mean(data, axis = 1), (np.shape(data)[0], -1))
#        var_X = np.reshape(np.var(data, axis = 1), (np.shape(data)[0], -1))
#        self.X = (data - mean_X) / var_X
        
#        min_X = np.reshape(np.min(data, axis = 1), (np.shape(data)[0], -1))
#        max_X = np.reshape(np.max(data, axis = 1), (np.shape(data)[0], -1))
#        self.X = np.divide((data*1.0 - min_X), (max_X - min_X*1.0))
        
        sid = [[160], [8], [7], [100], [220], [5], [10], [12], [6], [160], [220]]
        sid = np.array(sid)
        self.X = data / (sid*1.0)
        
#        self.X = data
        self.Y = label
        
    
    def split_data_mini_batch(self):
        m = self.X.shape[1]
        mini_batch = []
        permutation = list(np.random.permutation(m))
        shuffled_X = self.X[:, permutation]
        shuffled_Y = self.Y[:, permutation]
        num_complete_minibatches = int(math.floor(m / self.mini_batch_size))
        for i in range(0, num_complete_minibatches):
            mini_set_X = shuffled_X[:, self.mini_batch_size*i: self.mini_batch_size*(i+1)]
            mini_set_Y = shuffled_Y[:, self.mini_batch_size*i: self.mini_batch_size*(i+1)]
            mini_batch.append((mini_set_X, mini_set_Y))
            
        if (m % self.mini_batch_size != 0):
            mini_set_X = shuffled_X[:, self.mini_batch_size * num_complete_minibatches: ]
            mini_set_Y = shuffled_Y[:, self.mini_batch_size * num_complete_minibatches: ]
            mini_batch.append((mini_set_X, mini_set_Y))
        self.mini_batch = mini_batch
        
    def sigmoid(self, Z):
        A = 1.0 / (1.0 + np.exp(-Z))
        cache = (Z)
        return A, cache
    def sigmoid_backward(self, dA, cache):
        Z = cache
        s = 1.0 / (1.0 + np.exp(-Z))
        dZ = dA * s * (1 - s)
        return dZ
    
    
    def relu(self, Z):
        A = np.maximum(0, Z)
        cache = (Z)
        return A, cache
    def relu_backward(self, dA, cache):
        Z = cache
        dZ = np.array(dA, copy = True)
        dZ[Z <= 0] = 0
        return dZ
        
    def initialize_parameters_deep(self):  #initialize the NN's parameters
        parameters = {}
        l = np.shape(self.layer_dims)[0]
        for i in range(1, l):
            parameters['W' + str(i)] = np.random.randn(self.layer_dims[i], self.layer_dims[i-1]) * 0.001
            parameters['b' + str(i)] = np.zeros((self.layer_dims[i], 1))
#        for i in range(1, l):
#            print 'W' + str(i), np.shape(parameters['W'+str(i)])
#            print 'b' + str(i), np.shape(parameters['b'+str(i)])  
        self.parameters = parameters
    
    
    def forward_propagation(self):
        cache = []
        l = len(self.parameters) // 2  #不含有数据层
        A_prev = self.X
        
        def linear_activation_forward(A_prev, W, b, activation_function):
            #linear->activation   :  step1:z = w * a + b step2:a = activation_function(z)
        
            def linear_forward(A, W, b):
                #linear  :  z = w * a + b
                Z = np.dot(W, A) + b
                cache = (A, W, b)  #cache 是一个tuple 
                return Z, cache  
                
            Z, cache_linear = linear_forward(A_prev, W, b)
            if(activation_function == 'sigmoid'):
                A, cache_activation = self.sigmoid(Z)
            elif(activation_function == 'relu'):
                A, cache_activation = self.relu(Z)
            cache = (cache_linear, cache_activation)
            return A, cache
        
        for i in range(0, l-1):
            A, cache_linear_relu = linear_activation_forward(A_prev, self.parameters['W'+str(i+1)], self.parameters['b'+str(i+1)], 'relu')
            A_prev = A
            cache.append(cache_linear_relu)
        AL, cache_linear_sigmoid = linear_activation_forward(A_prev, self.parameters['W'+str(l)], self.parameters['b'+str(l)], 'sigmoid')
        cache.append(cache_linear_sigmoid)
        
        self.AL = AL
        self.cache = cache
        
        
    def compute_cost(self):
        m = self.Y.shape[1]
        cost = (-1.0/m) * np.sum((np.multiply(self.Y, np.log(self.AL)) + np.multiply((1-self.Y), np.log(1-self.AL))))
        
        self.cost_list.append(cost)
        

    def backward_propagation(self):
        grads = {}
        L = len(self.cache)
        #m = self.AL.shape[1]
        self.Y = self.Y.reshape(self.AL.shape)
        
        
        def linear_activation_backward(dA, cache, activation_function):
            ##  Z_prev = W * A_prev + b    A_prev = activation(Z_prev)
            cache_linear, cache_activation = cache
                
            if(activation_function == 'relu'):
                dZ = self.relu_backward(dA, cache_activation)
            elif(activation_function == 'sigmoid'):
                dZ = self.sigmoid_backward(dA, cache_activation)
                
            def linear_backward(dZ, cache):
                ###     Z = W * A_prev + b
                #    A_prev = cache[0]
                #    W = cache[1]
                #    b = cache[2]
                A_prev, W, b = cache
                m = A_prev.shape[1]
                dW = (1.0/m) * np.dot(dZ, A_prev.T)
                db = (1.0/m) * np.sum(dZ, axis = 1, keepdims = True)
                dA_prev = np.dot(W.T, dZ)
                return dA_prev, dW, db       
            
            dA_prev, dW, db = linear_backward(dZ, cache_linear)
            #grads = {"dA": dA_prev, "dW": dW, "db": db, "dZ": dZ}
            return dA_prev, dW, db
        
        dAL = -np.divide(self.Y, self.AL) + np.divide((1-self.Y), (1-self.AL))
        #sigmoid_divide
        last_cache = self.cache[-1]
        dA_prev, grads["dW"+str(L)], grads["db"+str(L)] = linear_activation_backward(dAL, last_cache, 'sigmoid')
        #end sigmoid_divide
        #relu_divide
        for i in reversed(range(L-1)):
            dA_prev, grads["dW"+str(i+1)], grads["db"+str(i+1)] = linear_activation_backward(dA_prev, self.cache[i], 'relu')
            
        self.grads = grads
        
        
    def update_parameter(self):
        L = len(self.grads) // 2
        for i in range(L):
            self.parameters["W"+str(i+1)] = self.parameters["W"+str(i+1)] - self.learn_rate * self.grads["dW"+str(i+1)]
            self.parameters["b"+str(i+1)] = self.parameters["b"+str(i+1)] - self.learn_rate * self.grads["db"+str(i+1)]
           
           
    def save_trained_parameters(self):
        l = len(self.layer_dims)
        key_name = []
        for i in range(1, l):
            key_name.append('W' + str(i))
            key_name.append('b' + str(i))
            
        theta = []
        count = 0
        for key in key_name:
            # flatten parameter
            new_vector = np.reshape(self.parameters[key], (-1,1))
#            keys = keys + [key]*new_vector.shape[0]
            
            if count == 0:
                theta = new_vector
            else:
                theta = np.concatenate((theta, new_vector), axis=0)
            count = count + 1
        theta = np.reshape(theta, (np.shape(theta)[0], -1))
        f = open(self.trained_parameters_path, 'w')
        f.truncate()
        #写神经网络的维度信息：
        dims_string = str(self.layer_dims[0])
        for i in range(1, len(self.layer_dims)):
            dims_string = dims_string + ',' + str(self.layer_dims[i])
        f.write(dims_string)
        f.write('\n')
        #写权重信息
        for i in range(np.shape(theta)[0]):
            f.write(str(theta[i, 0]))
            f.write('\n')
        f.close()
    
    def plot_cost(self):
        plt.plot(self.cost_list)
        plt.ylabel('cost')
        plt.xlabel('iterations')
        plt.title("Learning rate =" + str(self.learn_rate))
        plt.show()
    
    def model(self):
        self.read_train_data_and_label()
        self.initialize_parameters_deep()
        self.split_data_mini_batch()
        mini_batch_num = len(self.mini_batch)
        message_dict = {}
        for i in range(self.iteration):
            self.X, self.Y = self.mini_batch[i %  mini_batch_num]
            #print np.shape(self.X)
            #print np.shape(self.Y)
            self.forward_propagation()
            self.compute_cost()
            if(i % 100 == 0 and self.show_cost):
                #print ("Cost after iteration %i: %f" %(i, self.cost_list[-1]))
                message_dict[str(i)] = self.cost_list[-1]
            self.backward_propagation()
            self.update_parameter()
            
        self.plot_cost()
        self.save_trained_parameters()
        #string = "training nn has done"
        return message_dict


def trainer_interface(train_source_path, layer_dims, learn_rate = 0.1, mini_batch_size = 1024, iteration = 5000, show_cost = True):
    trainer = NNTrainer(train_source_path, layer_dims, learn_rate, iteration, show_cost)
    message_dict = trainer.model()
    keys = message_dict.keys
    for key in keys:
        print (message_dict[key])
    
if __name__ == '__main__':
    #layer_dims is a list, which contians the number of units in every NN layer.And the first number is the data dimensionality

    layer_dims = [11,10 ,1]
    train_source_path = './static/EXCL/data/train_data.xls'
    trainer = NNTrainer(train_source_path, layer_dims, learn_rate = 0.01, iteration = 10000, show_cost = True)
    message_dict = trainer.model()
    keys = message_dict.keys()
    
    for i in range(len(keys)):
        print (i*100, message_dict[str(i*100)])

#
#    prob = interface('18850067743')
#    print float(prob)