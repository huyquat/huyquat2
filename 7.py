S=input('Nhap chuoi:')
S1=S.split(' ')
S2=''.join([i for i in S if not i.isdigit()])
print(S2)
