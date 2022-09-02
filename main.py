import lib

def Init():
    m1="="
    m2="|"
    m3=" "
    m4="MENU"
    m5=m2+m3*50+m4+m3*50+m2
    
    Title = "\nChoose Converter:\n" 
    Lst=["Quit\n", "Decimal to Binary", "Decimal to Hexadecimal"]

    print(m1*len(m5))
    print(m2+m3*(len(m5)-2)+m2)
    print(m5)
    print(m2+m3*(len(m5)-2)+m2)
    print(m1*len(m5))

    print(Title)

    for i in range(len(Lst)):
        print(i,"|",Lst[i])

    Choice = input("\n")

    match Choice:
        case "0":
            print("*"*len(m5)+"\n")
            exit(0)
        case "1":
            n = input("Entrez un nombre positif:\n")
            if float(n) < 0:
                n = input("Entrez un nombre positif uniquement:\n")
            else:
                bin = lib.DecToBin(float(n))
                re = n+" => "+str(bin)
                l="+"+"-"*(len(re)+2)+"+\n"
                c="| "+re+" |\n"
                result = l+c+l
                print(result)
                print("-"*len(m5)+"\n")
        case "2":
            n = input("Entrez un nombre positif:\n")
            if float(n) < 0:
                n = input("Entrez un nombre positif uniquement:\n")
            else:
                hexa = lib.DecToHex(float(n))
                re = n+" => "+str(hexa)
                l="+"+"-"*(len(re)+2)+"+\n"
                c="| "+re+" |\n"
                result = l+c+l
                print(result)
                print("-"*len(m5)+"\n")
        case _:
            print("#"*len(m5)+"\n")
            exit(0)

while(True):
    Init()