def sep():
    print(60*'-')

def cekJumlahKarakter(input):
    lenInput = len(input)
    bisa = False
    counter =0
    for i in range(1, lenInput):
        # print(lenInput)
        lenInput -=i
        counter +=1
        if lenInput == 0:
            bisa = True
        if lenInput < 0 :
            break
    return bisa, counter

def segitigaKata(inputKal):
    sep()
    print("kalimat : ", inputKal)
    input = inputKal.replace(' ', '')
    lenInput = len(input)
    # print(cekJumlahKarakter(inputKal) )
    bisa, baris = cekJumlahKarakter(input)
    print("ini ",baris)
    if not bisa :
        print("*** Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola. ***")
    else:
        # print("lanjut")
        start = 0
        stop=0
        counter = 0
        for i in range(1, baris):
            counter+=1
            stop += i
            # print(input[start:stop]+ " ")
            x = list(input[start:stop])
            for h in x :
                print(h+ ' ', end='')
            print('')
            start = stop
        
        # cc = counter
        # print(stop)
        stop = stop-1
        start =0
        # print(start+counter)
        for i in range(0, baris):
            # stop = counter
            # print(input[start:start+counter])
            x = list(input[start:start+counter])
            for h in x :
                print(h+ ' ', end='')
            print('')
            start = counter + start
            counter -=1

def main():
    kalimat = input("masukkan kalimat : ")
    # kalimat = "Purwadhika Startup and Coding School @BSD"
    sep()
    segitigaKata(kalimat)

    # segitigaKata('Purwadhika')
    # segitigaKata('Purwadhika Startup and Coding School @BSD')
    # segitigaKata('kode')
    # segitigaKata('kode python')
    # segitigaKata('lintang')


if __name__ == '__main__':
    main()
    
    