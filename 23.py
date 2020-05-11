s = input("Nhập chuoi: ")
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print ("Số chữ số là:", d["DIGITS"])
print ("Số chữ cái là:", d["LETTERS"])