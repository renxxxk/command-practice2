def bmi(weight, height):
    bmi_data = []
    w = weight
    h = height
    bmi = w/(h*h)
    bmi = round(bmi, 1)
    bmi_data.append(bmi)
    if bmi<18.5:
        ans = "やせ型です"
    elif bmi>=18.5 and bmi<25:
        ans = "標準です"
    else:
        ans = "肥満です"
    bmi_data.append(ans)
    return bmi_data
