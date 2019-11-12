import json
with open('ccNasabah.json','r') as CC:
    out = json.load(CC)
def inValid(x):
    with open('ccInvalid.json', 'w') as inV:
        json.dump(x, inV)

satu =[]
dua=[]
for i in out:
    j = i['noCreditCard']
    if j[0] not in '456':
        satu.append(i)
    elif j.isdigit() == False:
        dua.append(i)
    elif j[5] == ' ':
        satu.append(i)
    elif j[5]=='-':
        dua.append(i)
    elif j[0:len()]
    elif len(j) > 16:
        satu.append(i)
    else:
        dua.append(i)

with open('ccValid.json', 'a') as ccV:
    json.dump(satu, ccV)

with open('ccInvalid.json', 'a') as inV:
    json.dump(dua, inV)

for i in out:
    j = i['noCreditCard']
    if j[0:len(j):4).isdigit == False:
        print(i)
