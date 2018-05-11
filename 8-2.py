str = input("문자열 : ")
print("개별 문자 출력 : ", end = "")
for i in range(len(str)):
    print(str[i], end="")
print("")
print("역숙 개별 문자 출력 : ", end = "")
for i in range(len(str)-1, -1, -1):
    print(str[i], end="")
