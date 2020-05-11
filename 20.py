Pascal = [[1]]
num = int(input("Nhap n: "))
print(Pascal[0])
for i in range(1,num+1):
    Pascal.append([1])
    for j in range(len(Pascal[i-1])-1):
        Pascal[i].append(Pascal[i-1][j]+Pascal[i-1][j+1])
    Pascal[i].append(1)
    print(Pascal[i])