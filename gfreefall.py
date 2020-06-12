# -*- coding: utf-8 -*-
"""
gfreefall.pyプログラム
自由落下シミュレーション
自由落下の運動方程式を数値的に解く
matplotlibによるグラフ描画機能付き
"""
# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt

# 定数
G = 9.80655

#メイン実行部
t =0.0      #時刻t
h = 0.001   #時刻の刻み幅h

# 係数の入力
v = float(input("初速度v0を入力してください:"))
x = float(input("初期高度x0を入力してください:"))
print("{:.7f} {:.7f} {:.7f}".format(t, x, v))   # 現在時刻と現在の位置
#グラフデータに現在位置を追加
tlist = [t]
xlist = [x]

#自由落下の計算
while x >= 0:   #　地面に達するまでの計算
    t += h      #　時刻の更新
    v += G * h  #　速度の計算
    x -= v * h  # 位置の更新
    print("{:.7f} {:.7f} {:.7f}".format(t, x, v))   #　現在時刻と現在の位置
    # グラフデータに現在位置を追加
    tlist.append(t)
    xlist.append(x)
#グラフの表示
plt.plot(tlist, xlist)  #グラフをプロット
plt.show()
