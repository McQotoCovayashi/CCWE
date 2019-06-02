#ジャンケンをするプログラム
#まずはこれを写してPythonの理解を深めよう

 #ライブラリのインポート
import time #時間に関するライブラリ
import random as rnd # 乱数に関するライブラリ as で別の名前にすることもできる

hand_type = {0:"グー",1:"チョキ",2:"パー"} #辞書形式 {インデックス1:値1,インデックス2:値3,…}
rand = rnd.uniform(0,3) # 0〜3のランダムな小数を生成
index = int(rand) # 小数を切り下げて整数に
hand = hand_type[index] # indexを使ってhand_typeを呼び出す

shouhai = [[0,1,-1],[-1,0,1],[1,-1,0]]

print("じゃーんけーん")

time.sleep(2) #2秒待つ

count = [0, 0, 0] # [win, lose, aiko]
for i in range(3):
    #自分の手の入力
    myself = int(input("グー:0,チョキ:1,パー:2   :"))
    print("ぽん!") 
    print("CP>>[{0}]  [{1}]<<あなた".format(hand, hand_type[myself]))# format()に複数の値を入れる場合は番号を振る
    
    time.sleep(2)
    #勝敗の判定
    winlose = shouhai[myself][index]
    #勝敗のカウント
    if winlose == 1:
        count[0] += 1
    elif winlose == -1:
        count[1] += 1
    else:
        count[2] += 1
    #コンピュータの手の更新
    index = int(rnd.uniform(0,3))
    hand = hand_type[index]

#勝敗結果の表示
print("あなたの{0}勝{1}敗、あいこは{2}つでした".format(count[0],count[1],count[2]))
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