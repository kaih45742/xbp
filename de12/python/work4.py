for i in range(1,4):
    print(i,"人目")
    name=input("名前を教えて下さい")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))
    print(i,"人目の",name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if waist>85 and age>40:
        print(name,"さん、高齢で内臓脂肪蓄積注意です")
    elif waist>85 and age<=40:
        print(name,"さん、若年で内臓脂肪蓄積注意です")
    else:
        print(name,"さん、腹囲は問題ありません")
#tabはそれ以下の内容が以上に含まれていることを示せる
