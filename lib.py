from math import floor

_MAXCOUNT = 13

# Decimal to Binary
def DecToBin(pN0:float):
    c=_MAXCOUNT
    N0 = pN0
    N1 = floor(N0)
    N2 = round(N0 - N1, 12)
    binary = ""
    f=N2
    binlst=[]
    floatLst=[]

    q,r = divmod(N1, 2)
    binlst.append(r)

    while(q!=0):
        q,r = divmod(q, 2)
        binlst.append(r)

    binlst.reverse()

    for i in range(len(binlst)):
        binary += str(binlst[i])

    if(f!=0.0 and c!=0):
        c-=1
        floatLst.append(f)
        binary += ","
        while(f!=0.0):
            f*=2
            fBin=floor(f)
            binary += str(fBin)
            f = round(f - fBin, 12)
            for idx in range(len(floatLst)):
                if f == floatLst[idx]:
                    f = 0.0
                    break
                else:
                    floatLst.append(f)
                    break

    re = str(N0)+" => "+str(binary)
    l="+"+"-"*(len(re)+2)+"+\n"
    c="| "+re+" |\n"
    result = l+c+l

    return binary

# Decimal to Hexadecimal
def DecToHex(pN0:float):
    c=_MAXCOUNT
    N0 = pN0
    N1 = floor(N0)
    N2 = round(N0 - N1, 12)
    hexa = ""
    f=N2
    hexlst=[]
    floatLst=[]

    def hex(pN):
        match pN:
            case 10:
                H = "A"
                return H
            case 11:
                H = "B"
                return H
            case 12:
                H = "C"
                return H
            case 13:
                H = "D"
                return H
            case 14:
                H = "E"
                return H
            case 15:
                H = "F"
                return H
            case _:
                s = '='
                e = ' '
                print(s*12)
                print(e*3,"Erreur",e*3)
                print(s*12)

    q,r = divmod(N1, 16)

    if(9<r):
        r=hex(r)
        hexlst.append(r)
    else:
        hexlst.append(r)


    while(q!=0):
        q,r = divmod(q, 16)
        if(9<r):
            r=hex(r)
            hexlst.append(r)
        else:
            hexlst.append(r)

    hexlst.reverse()

    for i in range(len(hexlst)):
        hexa += str(hexlst[i])

    if(f!=0.0):
        floatLst.append(f)
        hexa += ","
        while(f!=0.0 and c!=0):
            c-=1
            f*=16
            fHex=floor(f)
            if 9 < fHex:
                H=hex(fHex)
                hexa += str(H)
            else:
                hexa += str(fHex)
            f = round(f - fHex, 12)
            for idx in range(len(floatLst)):
                if f == floatLst[idx]:
                    f = 0.0
                    break
                else:
                    floatLst.append(f)
                    break

    re = str(N0)+" => "+str(hexa)
    l="+"+"-"*(len(re)+2)+"+\n"
    c="| "+re+" |\n"
    result = l+c+l

    return hexa