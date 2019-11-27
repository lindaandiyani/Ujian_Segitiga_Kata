import json
with open('ccNasabah.json') as jsonFile:
    data = json.load(jsonFile)

# print(data)
def cekAwalan(rekening):
    if rekening[0] =='4' or rekening[0]=='5' or rekening[0]== '6':
        valid= True
    else: valid= False
    return valid
def cekjumlahDigit(rekening):
    valid = False
    num=['0','1','2','3','4','5','6','7','8','9','-']
    cekdigit= rekening.replace('.','')
    cekdigit= cekdigit.replace('-','')
    cekdigit= cekdigit.replace(' ','')
    if len(cekdigit) ==16:
        valid= True
        for j in rekening:
            if j not in num:
                valid= False
                break
    else:
        valid= False
    return valid

def cekHubungan(rekening):
    
    hubung = False
    valid= False
    for i in rekening:
        if i =='-':
            hubung = True
            
            break
        else:
            hubung= False
    if hubung == True:
        listRekening= rekening.split('-')
        
        # print(listRekening)
        for elemen in listRekening:
            if len(elemen)==4:
                valid= True
                # print(valid)
            else:
                # print('y', len(elemen))
                valid = False
                break
    # print(hubung,valid)
    return hubung, valid
def cekUlangan(rekening):
    rekening= rekening.replace('-','')
    rekening= rekening.replace('.','')
    valid = True
    ulang= 0
    for i in range(1,len(rekening)):
        if rekening[i-1]== rekening[i]:
            ulang +=1
            if ulang >=3:
                valid= False
                break
        else:
            ulang=0
    return valid

def cekCreditCard(rekening):
    semuaValid = False
    awalanValid = cekAwalan(rekening)
    hubungValid, validValid= cekHubungan(rekening)
    # print(hubungValid,validValid)
    # if hubungValid == True and validValid == True:
    #     print(rekening)
    jumlahdigitvalid= cekjumlahDigit(rekening)
    perulanganValid = cekUlangan(rekening)

    if jumlahdigitvalid and awalanValid and perulanganValid == True:
        if hubungValid == True:
            # print(hubungValid)
            if validValid == True:
                semuaValid= True
            else:
                semuaValid = False
        else:
            semuaValid= True
    return semuaValid

def cekValidInvalid(rekening):
    listValid= []
    listInvalid= []
    for i in rekening:
        # valid= False
        listRekening= i['noCreditCard']
        # print(listRekening)
        statusValid = cekCreditCard(listRekening)
        if statusValid == True:
            # print(i['nama'])
            # print(i['noCreditCard'])
            listValid.append(i)
        else:
            listInvalid.append(i)
    # print(listValid)
    # print(listValid)
    # for i in listValid:
    #     print(i)

    with open('creditCardValid.json','w') as file:
        json.dump(listValid,file)
    with open('creditCardInvalid.json','w') as file2:
        json.dump(listInvalid,file2)


cekValidInvalid(data)
# print(listData)



