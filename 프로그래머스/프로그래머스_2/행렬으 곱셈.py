#https://programmers.co.kr/learn/courses/30/lessons/12949
#
import numpy as np

def solution(arr1, arr2):
    return (np.matrix(arr1) * np.matrix(arr2)).tolist()
