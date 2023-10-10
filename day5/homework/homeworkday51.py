age=int(input("how old are you?"))
fathers_age=int(input("how old is your father?"))
year=int(input("enter year"))
for i in range(50):
    print((fathers_age+i)/(age+1))
    print("next year my father will be " + str((fathers_age+i)/(age+i)) + "times older then me" + str(year+i))