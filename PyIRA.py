#!/usr/bin/env python
#coding: utf-8
"""
    __     _             _        _
    Python Interindustry Relation Analysis
"""
import numpy as np
import scipy as sp
import csv
import time

if __name__ == "__main__":
    print u"$*********************************$"
    print u"$ 均衡産出高モデル解析ツールPyIRA $"
    print u"$*********************************$"

#numpy配列を作成
    n = 14              #マトリクスサイズ(部門数)
    A = np.zeros((n,n)) #投入係数
    I = np.zeros((n,n)) #単位行列
    f1 = np.zeros(n)    #家計外消費支出
    f2 = np.zeros(n)    #民間消費支出
    f3 = np.zeros(n)    #一般政府消費支出
    f4 = np.zeros(n)    #国内総固定資本形成（公的）
    f5 = np.zeros(n)    #国内総固定資本形成（民間）
    f6 = np.zeros(n)    #在庫純増
    f7 = np.zeros(n)    #国内最終需要計
    f8 = np.zeros(n)    #国内需要計
    f9 = np.zeros(n)    #輸出（調整項含む）
    f10= np.zeros(n)    #最終需要計
    f11= np.zeros(n)    #需要合計
    f12= np.zeros(n)    #（控除）輸入
    f13= np.zeros(n)    #（控除）関税
    f14= np.zeros(n)    #（控除）輸入品商品税
    f15= np.zeros(n)    #（控除）輸入計
    f16= np.zeros(n)    #最終需要部門計
    X  = np.zeros(n)    #解ベクトル

    time.sleep(2)
#対角要素を1にする
    for i in range(14):
        for j in range(14):
            if(i==j):
                I[i,j] = 1.
#投入係数表の読み込み
    amatData = csv.reader(open('Amatrix14.csv','rb'))
    i = 0
    for row in amatData:
        #print "line Num = %02d" % count
        j = 0
        for data in row:
           A[i,j] = float(data)
           j += 1
        i += 1
#最終需要ベクトルの読み込み（16個ある)
    fvecData = csv.reader(open('Fvector14.csv','rb'))
    i = 0
    for row in fvecData:
        f1[i] = float(row[0])
        f2[i] = float(row[1])
        f3[i] = float(row[2])
        f4[i] = float(row[3])
        f5[i] = float(row[4])
        f6[i] = float(row[5])
        f7[i] = float(row[6])
        f8[i] = float(row[7])
        f9[i] = float(row[8])
        f10[i] = float(row[9])
        f11[i] = float(row[10])
        f12[i] = float(row[11])
        f13[i] = float(row[12])
        f14[i] = float(row[13])
        f15[i] = float(row[14])
        f16[i] = float(row[15])
        i += 1

#([I]-[A])X=F
    X1 = np.linalg.solve(I-A,f16)
    print X1
    f16[8] = f16[8] * 0.9
    X2 = np.linalg.solve(I-A,f16)
    print X2

    print X2-X1
# 入力を求める（PyScripterではshift_jisでエラーが出る）
    print raw_input(u"解析終了．出力ファイルを確認して下さい．".encode("shift_jis"))
