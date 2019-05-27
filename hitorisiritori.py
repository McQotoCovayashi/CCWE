#一人しりとりをするプログラムです
#まずは書き写してPythonの理解を深めましょう


import time

print("しりとりしましょ！")
time.sleep(4)
print("ただし！！")
time.sleep(2)
print("おまえ一人でなwww")
time.sleep(1)
print("まずはしりとりの り からだゼ！")
word0 = "しりとり"
time.sleep(1)
word1 = input("「{0}」の「{1}」:".format(word0, word0[-1]))

while word0[-1] == word1[0]:
    word0 = word1
    word1 = input("「{0}」の「{1}」:".format(word0, word0[-1]))
    time.sleep(0.5)

print("はい、ざんねーん")

""" 
課題1
    if と break を使って「ん」で終わった言葉を入力したら、
    終了するプログラムに改良してみよう
課題2
    while の前後を変えて、何回続いたかカウントして表示する
    プログラムに改良してみよう
課題3
    このプログラムは何も入力しないでenterを押すとエラーになります。
    if文を使ってこのエラーを回避してみましょう
発展
    リスト型のデータとtry,exceptを使って一度入力したことが
    ある単語を再度入力したら、終了するプログラムに改良してみよう

"""