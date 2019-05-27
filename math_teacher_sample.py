import time

print("さぁ、算数の時間だ")
time.sleep(1)
print("これから出す問題を解いてみせろ")
time.sleep(1)

q = ("第一問 2 + 4 * 6 :","第二問 101 * 99 :","第三問 53 を 11 で割ったときの余りは？:","第四問 1.2 + 0.34 :")
a = ('26', '9999', '9', '1.54')

print("はじめ！")

answer = [input("{}".format(q[i])) for i in range(4)]

correct = [25 for i in range(4) if answer[i] == a[i]]
point = 0
for i in correct:
    point += i

time.sleep(2)
print("結果発表")
time.sleep(5)
print("{} / 100 ".format(point))

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