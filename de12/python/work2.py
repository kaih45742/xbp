name=input("名前を教えて下さい")
waist=float(input("腹囲は？"))
age=int(input("年齢は？"))



print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>85 and age>40:
    print(name,"さん、高齢で内臓脂肪蓄積注意です")
elif waist>85 and age<=40:
    print(name,"さん、若年で内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")#←なぜこれがうまくいかないのか謎#←数値ではなく文字列として認識されていたため


