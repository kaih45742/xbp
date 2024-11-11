name_list=[]
age_list=[]
for i in range(1,4):
    print(i,"人目")
    name=input("名前を教えてください")
    name_list.append(name)
    age=int(input("年齢は？"))
    age_list.append(age)
l=len(age_list)#件数
s=sum(age_list)#値の合計
mean=s/l#平均



print(name_list[0],"さんは",age_list[0],"歳で、",name_list[1],"さんは",age_list[1],"歳で、",name_list[2],"さんは",age_list[2],"歳です。")
