#ジャンケンをするプログラム
#まずはこれを写してPythonの理解を深めよう

 #ライブラリのインポート
import time #時間に関するライブラリ
import random as rnd # 乱数に関するライブラリ as で別の名前にすることもできる

hand_type = {0:"グー",1:"チョキ",2:"パー"} #辞書形式 {インデックス1:値1,インデックス2:値3,…}
rand = rnd.uniform(0,3) # 0〜3のランダムな小数を生成
index = int(rand) # 小数を切り下げて整数に
hand = hand_type[index] # indexを使ってhand_typeを呼び出す


print("じゃーんけーん")

time.sleep(2) #2秒待つ

print("ぽん!         [{}]".format(hand)) # format()は文字列中の{}に値を入れ込める 

time.sleep(2)

print("うふふふ♪")

"""
課題1
    input()を使ってプレイヤーとジャンケンするプログラムに改良してみよう
課題2
    if elif else を使ってどちらが勝ったかを判定するプログラムに改良してみよう
課題3
    for を使って3回勝負でどちらが勝ったかを判定するプログラムに改良してみよう
    ただし、あいこは1回と見なします。
"""