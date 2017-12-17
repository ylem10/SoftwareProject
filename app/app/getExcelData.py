# -*- coding: utf-8 -*-
# env config

import xlrd
import os
import xlwt
import pandas as pd


def getExcelData(filename):
    data = xlrd.open_workbook("./static/EXCL"+filename)
    table = data.sheets()[0]  # this need to be verify more
    a = []
    line_num = table.nrows
    for i in range(1,line_num):
        dict = {}
        for j in range(0,11):
            dict[table.cell(0,j).value] = table.cell(i,j).value
        a.append(dict)
        # print(table.cell(0,j).value,table.cell(i,j).value)
    # print(a)
    return a