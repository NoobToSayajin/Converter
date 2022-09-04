import lib

def Init():
    m1="="
    m2="|"
    m3=" "
    m4="MENU"
    m5=m2+m3*50+m4+m3*50+m2
    
    Title = "\nChoose Converter:\n" 
    Lst=["Quit\n", "Decimal to Binary", "Decimal to Hexadecimal", "Binary to Decimal", "Hexadecimal to Decimal", "Binary to Hexadecimal", "Hexadecimal to Binary"]

    def printResult(pInput,pType):
        re = pInput+" => "+str(pType)
        l="+"+"-"*(len(re)+2)+"+\n"
        c="| "+re+" |\n"
        result = "\n"+l+c+l
        print(result+"\n"+"-"*len(m5)+"\n")

    def callFunc(pCase):
        choice = pCase
        match choice:
            case "0":
                print("*"*len(m5)+"\n")
                exit(0)
            case "1":
                n = input("Entrez un nombre positif:\n")
                if float(n) < 0:
                    callFunc("1")
                else:
                    bin = lib.DecToBin(float(n))
                    printResult(n,bin)
            case "2":
                n = input("Entrez un nombre positif:\n")
                if float(n) < 0:
                    callFunc("2")
                else:
                    hexa = lib.DecToHex(float(n))
                    printResult(n,hexa)
            case "3":
                s = input("Entrez un nombre binaire positif:\n")
                sLst = list(s)
                isBin = False
                for idx in range(len(sLst)):
                    if (sLst[idx]=="0" or sLst[idx]=="1" or sLst[idx]=="."):
                        isBin = True
                    else:
                        isBin = False
                        callFunc("3")
                if (isBin):
                    dec = lib.BinToDec(s)
                    printResult(s,dec)
            case "4":
                s = input("Entrez un nombre binaire positif:\n")
                sLst = list(s)
                isHex = False
                for idx in range(len(sLst)):
                    match sLst[idx]:
                        case "0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"|"A"|"B"|"C"|"D"|"E"|"F"|"a"|"b"|"c"|"d"|"e"|"f"|".":
                            isHex = True
                        case _:
                            isHex = False
                            callFunc("4")
                if (isHex):
                    dec = lib.HexToDec(s)
                    printResult(s,dec)
            case "5":
                s = input("Entrez un nombre binaire positif:\n")
                sLst = list(s)
                isBin = False
                for idx in range(len(sLst)):
                    if (sLst[idx]=="0" or sLst[idx]=="1" or sLst[idx]=="."):
                        isBin = True
                    else:
                        isBin = False
                        callFunc("5")
                if (isBin):
                    hex = lib.BinToHex(s)
                    printResult(s,hex)
            case "6":
                s = input("Entrez un nombre binaire positif:\n")
                sLst = list(s)
                isHex = False
                for idx in range(len(sLst)):
                    match sLst[idx]:
                        case "0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"|"A"|"B"|"C"|"D"|"E"|"F"|"a"|"b"|"c"|"d"|"e"|"f"|".":
                            isHex = True
                        case _:
                            isHex = False
                            callFunc("6")
                if (isHex):
                    bin = lib.HexToBin(s)
                    printResult(s,bin)
            case _:
                err="HIC DRACONIS"
                msg=str(" "*int((len(m5)/2)-len(err)/2))+err
                print("#"*len(m5))
                print(msg)
                print("#"*len(m5)+"\n")
                Init()

    print(m1*len(m5))
    print(m2+m3*(len(m5)-2)+m2)
    print(m5)
    print(m2+m3*(len(m5)-2)+m2)
    print(m1*len(m5))

    print(Title)

    for i in range(len(Lst)):
        print(i,"|",Lst[i])

    Choice = input("\n")
    callFunc(Choice)
    



while(True):
    Init()