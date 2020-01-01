import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as m
import statistics as st


def m_o(X, y):
    mean_all = 0
    for i in range(len(X)):
        mean_all = mean_all + X[i] * y[i]
    return mean_all


def m_o_2(X, y):
    mean_2_all = 0
    for i in range(len(X)):
        mean_2_all = mean_2_all + X[i] * X[i] * y[i]
    return mean_2_all


def m_o_3(X, y):
    mean_3_all = 0
    for i in range(len(X)):
        mean_3_all = mean_3_all + X[i] * X[i] * X[i] * y[i]
    return mean_3_all


def m_o_4(X, y):
    mean_4_all = 0
    for i in range(len(X)):
        mean_4_all = mean_4_all + X[i] * X[i] * X[i] * X[i] * y[i]
    return mean_4_all


def disp(X, y):
    d = 0
    for i in range(len(X)):
        d = d + ((X[i] - m_o(X, y)) ** 2) * y[i]
    return d


def disp_3(X, y):
    d_3 = m_o_3(X, y) - 3 * m_o(X, y) * m_o_2(X, y) + 2 * (m_o(X, y) ** 3)
    return d_3


def disp_4(X, y):
    d_4 = m_o_4(X, y) - 4 * m_o(X, y) * m_o_3(X, y) + 6 * (m_o(X, y) ** 2) * m_o_2(X, y) - 3 * (m_o(X, y) ** 4)
    return d_4


def sigma(X, y):
    return m.sqrt(disp(X, y))


def median_data(X, y):
    y_n = []
    k = 0
    int_1 = 0
    int_2 = 0
    int_3 = 0
    for i in range(len(y)):
        k = k + y[i]
        y_n.append(k)
        if (k >= 0.5):
            k = (-1) * y.sum()
            int_1 = y[i]
            int_2 = y_n[i - 1]
            int_3 = X[i] - 0.5
    med = int_3 + (0.5 - int_2) / int_1
    return med


def A_s(X, y):
    return (disp_3(X, y) / (sigma(X, y) ** 3))


def E_k(X, y):
    return (disp_4(X, y) / (sigma(X, y) ** 4) - 3)


def check_moda(X, y):
    i = 0
    max = y.max()
    for value in y:
        if value == max:
            i = i + 1
    if i == 1:
        return X[y.argmax()]
    else:
        return "Моды нет"
