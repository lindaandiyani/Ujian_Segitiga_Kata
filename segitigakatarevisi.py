kata = input('masukkan kata : ')
def cekKata(kata):
    panjang = len(kata)
    bisa = False
    jumlahbaris =0
    for i in range(1,panjang):
        panjang -= i
        jumlahbaris +=1
        if panjang == 0:
            bisa = True
        if panjang <0:
            break
    return bisa, jumlahbaris
# print(cekKata(kata))
def segitigaKata(inputKa):
    inputan= inputKa.replace(' ','')
    lenInput= len(inputan)
    bisa, jumlahbaris = cekKata(inputan)
    if bisa == False:
        print('mohon maaf kata yang anda inputkan tidak memenuhi syarat')
    else:
        start = 0
        stop= 0
        counter =0
        print(jumlahbaris)
        for i in range(1,jumlahbaris):
            counter +=1
            stop +=i
            x= list(inputKa[start:stop])
            for i in x:
                print(i,' ',end='')
            print('')
            start= stop
        stop = stop - 1
        start =0
        for i in range(0, jumlahbaris):
            x = list(inputKa[start:start+counter])
            for j in x:
                print(j,' ',end='')
            print('')
            start= counter + start
            counter -=1


segitigaKata(kata)


