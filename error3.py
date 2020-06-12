# -*- coding: utf-8 -*-
"""
error3.pyプログラム
計算誤差の例題プログラム
情報落ち誤差の例題
"""
#メイン実行部
#　初期設定
x = 1e10
y = 1e-8
temp = 0.0

# y(1e-8) をx(1e10)に1000000回加える
for i in range(1000000):
    x = x+y
#結果出力
print(x)

#先にy(1e-8)を1000000回加える
for i in range(1000000):
    temp += y
#加える結果をx(1e10)に加える
x = 1e10
x += temp
#結果出力
print(x)
