word_list = []
success_list = []
import random
import string
import time

start = time.time()
for i in range (0,5):
    for i in range (0,5):
        a = random.randint(0,35)
        #各数字とアルファベットの出る確率を均一にするため
        if a<10:
          b = str(a)
          #strは数字を文字列に変換する

        else:
            b = random.choice(string.ascii_lowercase)
            #random.choice()はランダムな文字を生成する()の中身を変えれば大文字や数字も生成可能
        word_list.append(b)

    c = (word_list[0]+ "" +word_list[1]+ "" +word_list[2]+ "" +word_list[3]+ "" +word_list[4])
    #ここで+ "" +を間に置かないと文字の間に""が出力されて見づらくなってしまう
    d = (c+ " " +"→ ")
    #これを挟まないとinputする時に見づらい
    e = input(d)
    if e == c:
       print("成功!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
       success_list.append(int(1))
    else:
       print("失敗：；")
    del word_list[:]    
end = time.time()
f=sum(success_list)
g = end - start
print(f,"/ 5")
print(g,"秒")
if f ==5 and g<=20:
   print("すげえ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
   #s = '　　　　　　　　　　　　　■■■■■\n　　　　　　　   　　■■■　　　　　■■■\n　　　　　　　　■■　　　　　　　　　　　■■\n　　　　　　■■　　　　　　　　　　　　　　　■■\n　　　　　■　　　　　　　　　　　　　　　　　　■■\n　　　　■　　　　　　　　　　　　　　　　　　　　　■\n　　　■■　　　　　　　　　　　　　　　　　　　　　■■\n　　　■　　　　　　　　　　　　　　　　　　　　　　　■\n　　■　　　　　　　　　　　　　　　　　　　　　　　　　■\n　　　　　　　　　　　　　　　　　　　　　　　　　　　　■\n　　　■■■■■■■■■　　　　　　　■■■■■■■■■\n　■■■■　　　　　■■■■　　　■■■■　　　　　■■■■\n■■■　　　　　　　　　　■■■■■　　　　　　　　　■■■\n\n　　■■■■■■■■■■■■　　　■■■■■■■■■■■■\n■　■■■■■■■■■■■■　　　■■■■■■■■■■■■\n■　　■■■■■■■■■■　　　　　■■■■■■■■■■　■\n■■　■■■■　■■■■　　　　　　■■■■　　■■■　　■\n　■　　　■■■■■■　　　　　　　　　■■■■■■　　　■\n　■　　　　　　　　　　　　　　　　　　　　　　　　　　　■\n　■■　　　　　　　　　　　　　　　　　　　　　　　　　■■\n　　■　　　　　　■■　　　　　　　　　■■　　　　　■■\n　　■■　　　　　　■■■　　　　　■■■　　　　　　■■\n　　　■■　　　　　　■■■■■■■■■　　　　　　■■\n　　　　■■　　　　　　　　　　　　　　　　　　　■■\n　　　　■■■　　　　　　　　　　　　　　　　　■■■\n　　　　　■■■　　　　　　　　　　　　　　■■■\n　　　　　　　■■■■　■　　　■　■　■■■■\n　　　　　　　　■■■■　■　■　　■■■■■\n 　　　　　　　　　　■■■■■■■■■'
   #print(s)
   #↑ここは顔文字を生成しようとしたけど、記号の大きさの関係でずれたので諦めました