# -*- coding: utf-8 -*-
import numpy as np
import xlrd
#import math
#import matplotlib.pyplot as plt

class NNPredictor:#用于用户预测的类
    def __init__(self, predict_source_path):
        self.predict_source_path = predict_source_path
        self.trained_parameters_path = './model/dataAnalyze/trained-parameters.txt'
        
    def read_predict_data(self):
        bk = xlrd.open_workbook(self.predict_source_path)
        try:
            sh = bk.sheet_by_name("Sheet1")
        except:
            print ("no sheet in %s named Sheet1" %(self.predict_source_path))
        ncols = sh.ncols
        nrows = sh.nrows
        data = []
        for i in range(1, nrows):
            for j in range(ncols):
                data.append(sh.cell_value(i, j))
        #def normalization_data(data):
                # pass
        data = np.reshape(data, (nrows-1, ncols)).T
        
#        min_X = np.reshape(np.min(data, axis = 1), (np.shape(data)[0], -1))
#        max_X = np.reshape(np.max(data, axis = 1), (np.shape(data)[0], -1))
#        self.X = np.divide((data*1.0 - min_X), (max_X - min_X*1.0))
        
        sid = [[160], [8], [7], [100], [220], [5], [10], [12], [6], [160], [220]]
        sid = np.array(sid)
        self.X = data / (sid*1.0)
        
#        self.X = data
    
    def get_trianed_parameters(self):
        #use self.trained_parameters_path get trained-parameters
        #获取神经网络的维度信息
        f = open(self.trained_parameters_path, 'r')
        lines = f.readlines()
        dims_string = lines[0]
        layer_dims = []
        for dim in dims_string.split(','):
            layer_dims.append(int(dim))
        weight_dims = []
        for i in range(1, len(lines)):
            weight_dims.append(float(lines[i]))
        weight_dims = np.reshape(weight_dims, (np.shape(weight_dims)[0], -1))
        #print layer_dims
        #print np.shape(weight_dims)
        
        #利用layer_dims和weight_dims生成parameters字典：
        parameters = {}
        l = np.shape(layer_dims)[0]
        begin = 0
        for i in range(1, l):
            end = begin + layer_dims[i]*layer_dims[i-1]
            parameters['W' + str(i)] = np.reshape(weight_dims[begin: end, 0], (layer_dims[i], layer_dims[i-1]))
            begin = end + 1
            end = begin + layer_dims[i]
            parameters['b' + str(i)] = np.reshape(weight_dims[begin: end, 0], (layer_dims[i], -1))
        self.parameters = parameters

    def forward_propagation(self):
        l = len(self.parameters) // 2  #不含有数据层
        A_prev = self.X
        
        def linear_activation_forward(A_prev, W, b, activation_function):
            #linear->activation   :  step1:z = w * a + b step2:a = activation_function(z)
            def linear_forward(A, W, b):
                #linear  :  z = w * a + b
                Z = np.dot(W, A) + b
                return Z
            def sigmoid(Z):
                A = 1.0 / (1.0 + np.exp(-Z))
                return A
            def relu(Z):
                A = np.maximum(0, Z)
                return A
                
            Z = linear_forward(A_prev, W, b)
            if(activation_function == 'sigmoid'):
                A= sigmoid(Z)
            elif(activation_function == 'relu'):
                A= relu(Z)
            return A
    
        for i in range(0, l-1):
            A = linear_activation_forward(A_prev, self.parameters['W'+str(i+1)], self.parameters['b'+str(i+1)], 'relu')
            A_prev = A
        AL = linear_activation_forward(A_prev, self.parameters['W'+str(l)], self.parameters['b'+str(l)], 'sigmoid')

        self.AL = AL
    
    def predict(self):
        self.read_predict_data()
        self.get_trianed_parameters()
        self.forward_propagation()
        #print self.X[:, 0]
        return self.AL
        
        
def predicter_interface(filename):
        
    predict_source_path = './static/EXCL' + filename
    predictor = NNPredictor(predict_source_path)
    prob = predictor.predict()
    return prob
    
    #return float(prob)
    
# if __name__ == '__main__':
#     predicter_interface('18850067743')