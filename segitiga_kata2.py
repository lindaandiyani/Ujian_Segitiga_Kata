inputan= input('masukkan kata : ')
kalimat = inputan.replace (' ', '')
kalimatlist = list(kalimat)


rules = []
for a in range(len(kalimatlist)):
    X = int((a*(a+1))/2)
    rules.append (X)
print (rules)

n=0
if len(kalimatlist) not in rules:
    print ('jumlah karaker belum bisa di proses.')
else:
    n= rules.index(len(kalimatlist))
def segitigaKata(n):   
    num = 0
    for i in range(0, n): 
        for j in range(0, i+1): 
            print(kalimatlist[num], end=" ")  
            num = num + 1
        print("\r") 
def segitigaKataMundur(n):   
    num = 0
    for i in range(n, 0, -1): 
        for j in range(1, i+1): 
            print(kalimatlist[num], end=" ")  
            num = num + 1
        print("\r") 
       
segitigaKata(n)
segitigaKataMundur(n)