import time
import random as rnd

class Janken:
    def __init__(self):
        self.hand_type = {0:"グー",1:"チョキ",2:"パー"}
        self.rand = rnd.uniform(0,3)
        self.index = int(self.rand)
        self.shouhai = [[0,1,-1],[-1,0,1],[1,-1,0]]
        self.hand = self.hand_type[self.index]
    
    def refresh(self):
        self.rand = rnd.uniform(0,3)
        self.index = int(self.rand)
        self.hand = self.hand_type[self.index]

    def print_hand(self, index, print_hand = True):
        self.hand = self.hand_type[index]
        if print_hand == True:
            print(self.hand)
        return self.hand

    
    def play(self, match_num = 1, sleep_time = 2):
        count = [0, 0, 0] # [win, lose, aiko]
        print("じゃーんけーん")
        time.sleep(sleep_time)        
        for i in range(match_num):
            #自分の手の入力
            myself = int(input("グー:0,チョキ:1,パー:2   :"))
            print("ぽん!") 
            print("CP>>[{0}]  [{1}]<<あなた".format(self.hand, self.hand_type[myself]))
            time.sleep(sleep_time)
            #勝敗の判定
            winlose = self.shouhai[myself][self.index]
            #勝敗のカウント
            if winlose == 1:
                count[0] += 1
            elif winlose == -1:
                count[1] += 1
            else:
                count[2] += 1
            #コンピュータの手の更新
            self.refresh()
        #勝敗結果の表示
        print("あなたの{0}勝{1}敗、あいこは{2}つでした".format(count[0],count[1],count[2]))
        print("うふふふ♪")
