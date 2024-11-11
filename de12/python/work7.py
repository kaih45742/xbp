#name_list=[]
#age_list=[]
#for i in range(1,6):
    #print(i,"人目")
    #age=int(input("年齢は？"))
    #age_list.append(age)
#l=len(age_list)#件数
#s=sum(age_list)#値の合計
#mean=s/l#平均
#print("今回の年齢の平均は",mean,"歳です。")

random_list=[]
for i in range (1,200000):
    import random
    a = random.randint(0,100)
    random_list.append(a)
l=len(random_list)
s=sum(random_list)
mean=s/l
print("平均は",mean,"です")