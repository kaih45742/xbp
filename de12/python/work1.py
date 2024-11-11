name="aaa"
waist=84
age=90
#はコマンドとして認識されない(コメント)

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist > 85:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん腹囲は問題ありません")
