import calc_bmi
weight  = float(input('あなたの体重を入力してください(kg): '))
height0 = float(input('あなたの身長を入力してください(cm): '))
height = height0/100
bj = calc_bmi.bmi(weight, height)
print("----" * 10)
print("あなたのBMI: " + str(bj[0]) + '\nあなたの体型: ' + bj[1])
