score = 0
while(score >= 0 and score <= 100):
    score = int(input("점수 : "))
    if(score >= 90 and score <= 100):
        print(score, "= A")
        continue
    elif(score >= 80 and score <= 89):
        print(score, "= B")
        continue
    elif(score >= 70 and score <= 79):
        print(score, "= C")
        continue
    elif(score >= 60 and score <= 69):
        print(score, "= D")
        continue
    else:
        if(score < 0 or score > 100):
            print("입력 가능한 점수 범위는 0~100입니다.")
            continue
        print(score, "= F")
        continue
