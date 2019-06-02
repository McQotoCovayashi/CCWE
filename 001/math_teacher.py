import time

print("さぁ、算数の時間だ")
time.sleep(1)
print("これから出す問題を解いてみせろ")
time.sleep(1)

print("はじめ！")

q1 = input("第一問 2 + 4 * 6 :")
a1 = 2 + 4 * 6

q2 = input("第二問 101 * 99 :")
a2 = 101 * 99

q3 = input("第三問 53 を 11 で割ったときの余りは？:")
a3 = 53 % 11

q4 = input("第四問 1.2 + 0.34 :")
a4 = 1.2 + 0.34

point = 0
if int(q1) == a1:
    point += 1
if int(q2) == a2:
    point += 1
if int(q3) == a3:
    point += 1
if float(q4) == a4:
    point += 1

time.sleep(2)
print("結果発表")
time.sleep(5)
print("{} / 4 ".format(point))

"""
課題1
    インタープリターを使ってそれぞれの問題をpythonで計算させてみましょう
    答えはいくつでしょうか
課題2
    22行目以降を変更して、100点満点で評価するプログラムに改良してみましょう
課題3
    リストや辞書形式、for文を使って、繰り返し同じコードを書いている部分を
    スッキリさせてみましょう

"""