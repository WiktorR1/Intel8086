pamiec = []
for i in range(65536):
    pamiec.append(0)
    #pamiec.append(randint(0, 255))

rejestry = { "AL": None,
             "AH": None,
             "BL": None,
             "BH": None,
             "CL": None,
             "CH": None,
             "DL": None,
             "DH": None,
             }


def wczytanie_uzytkownika():
    for r in rejestry:
        rejestry[r] = hex(int(input(f"Podaj wartość do zapisania w rejestrze {r}: "), 16))

def stan_rejestru():
    print("\nStan rejestrów procesora Intel 8086: \n")
    for rejestr in rejestry:
        print(rejestr, "=", rejestry[rejestr])

def wczytanie_16_i_8_bit():
    try:
        return all(int(value, 16) <= 255 for value in rejestry.values())
    except ValueError:
        return False



def MOV(a, b):
    rejestry[a] = rejestry[b]



def XCHG(x, y):
    rejestry[x], rejestry[y] = rejestry[y], rejestry[x]



def NOT(x):
    temp = int(rejestry[x], 16)
    rejestry[x] = hex(255 - temp)



def INC(x):
    temp = int(rejestry[x], 16)
    temp += 1
    rejestry[x] = hex(temp)


def DEC(x):
    temp = int(rejestry[x], 16)
    temp -= 1
    rejestry[x] = hex(temp)





def AND(x, y):
    rejestry[x] = hex(int(rejestry[x], 16) & int(rejestry[y], 16))



def OR(x, y):
    rejestry[x] = hex(int(rejestry[x], 16) | int(rejestry[y], 16))



def XOR(x, y):
    rejestry[x] = hex(int(rejestry[x], 16) ^ int(rejestry[y], 16))



def ADD(x, y):
    rejestry[x] = hex(int(rejestry[x], 16) + int(rejestry[y], 16))



def SUB(x, y):
    rejestry[x] = hex(int(rejestry[x], 16) - int(rejestry[y], 16))

dalej=True
while dalej:
    stan_rejestru()
    try:
        akcja = int(input(
            "Podaj numer akcji do wykonania:\n1 - Zmiana adresów rejestrów\n2 - Instrukcja między rejestrami do wykonania przez program\n3 - Instrukcja między rejestrem a pamiecią do wykonania przez program\n4 - Wyjście\n>>>"))
        if akcja == 1:
            bledne_wczytanie = True
            while bledne_wczytanie:
                wczytanie_uzytkownika()
                if wczytanie_16_i_8_bit():
                    bledne_wczytanie = False
               
                else:
                    print("\nWczytanie nie jest 8 bitowe!\n")
        elif akcja == 2:
            instrukcja = int(
                input(
                    "\nWybierz instrukcję do symulacji:\nMOV  - 1\nXCHG - 2\nNOT  - 3\nINC  - 4\nDEC  - 5\nAND  - 6\nOR   - 7\nXOR  - 8\nADD  - 9\nSUB  - 10\n\n"))
            if instrukcja == 1:
                reg1 = input("Podaj zawartość pierwszego rejestru dla instrukcji MOV: ").upper()
                reg2 = input("Podaj zawartość drugiego rejestru dla instrukcji MOV: ").upper()
                if reg1 and reg2 in rejestry:
                    MOV(reg2, reg1)
                    print("\n")
              
                else:
                    print("\nBłędny rejestr!")
            elif instrukcja == 2:
                reg1 = input("Podaj zawartość pierwszego rejestru dla instrukcji XCHG: ")
                reg2 = input("Podaj zawartość drugiego rejestru dla instrukcji XCHG: ")
                if reg1 and reg2 in rejestry:
                    XCHG(reg1, reg2)
              
                else:
                    print("\nBłędne rejestry!")
            elif instrukcja == 3:
                reg = input("Podaj zawartość rejestru dla instrukcji NOT: ")
                if reg in rejestry:
                    NOT(reg)
                
                else:
                    print("\nBłędny rejestr!")
            elif instrukcja == 4:
                reg = input("Podaj zawartość rejestru dla instrukcji INC: ")
                if reg in rejestry:
                    INC(reg)
               
                else:
                    print("\nBłędny rejestr!")
            elif instrukcja == 5:
                reg = input("Podaj zawartość rejestru dla instrukcji DEC: ")
                if reg in rejestry:
                    DEC(reg)
              
                else:
                    print("\nBłędny rejestr!")
            elif instrukcja == 6:
                reg1 = input("Podaj zawartość pierwszego rejestru dla instrukcji AND: ")
                reg2 = input("Podaj zawartość drugiego rejestru dla instrukcji AND: ")
                if reg1 and reg2 in rejestry:
                    AND(reg1, reg2)
              
                else:
                    print("\nBłędne rejestry!")
            elif instrukcja == 7:
                reg1 = input("Podaj zawartość pierwszego rejestru dla instrukcji OR: ")
                reg2 = input("Podaj zawartość drugiego rejestru dla instrukcji OR: ")
                if reg1 and reg2 in rejestry:
                    OR(reg1, reg2)
               
                else:
                    print("\nWrong rejestry!")
            elif instrukcja == 8:
                reg1 = input("Podaj zawartość pierwszego rejestru dla instrukcji XOR: ")
                reg2 = input("Podaj zawartość drugiego rejestru dla instrukcji XOR: ")
                if reg1 and reg2 in rejestry:
                    XOR(reg1, reg2)
               
                else:
                    print("\nWrong rejestry!")
            elif instrukcja == 9:
                reg1 = input("Podaj zawartość pierwszego rejestru dla instrukcji ADD: ")
                reg2 = input("Podaj zawartość drugiego rejestru dla instrukcji ADD: ")
                if reg1 and reg2 in rejestry:
                    ADD(reg1, reg2)
               
                else:
                    print("\nBłędne rejestry!")
            elif instrukcja == 10:
                reg1 = input("Podaj zawartość pierwszego rejestru dla instrukcji SUB: ")
                reg2 = input("Podaj zawartość drugiego rejestru dla instrukcji SUB: ")
                if reg1 and reg2 in rejestry:
                    SUB(reg1, reg2)
               
                else:
                    print("\nBłędne rejestry!")
            
            else:
                print("Błędna instrukcja!")
        elif akcja == 3:
            try:
                obiekt_1 = input("Podaj zawartość rejestru lub pamięci dla instrukcji: ")
                if obiekt_1.upper() in rejestry:
                    obiekt_2 = input("Podaj zawartść pamięci dla instrukcji: ")
                    if 255 < obiekt_2 < 65536:
                        rejestry[obiekt_1] = pamiec[int(obiekt_2, 16)]
                 
                    else:
                        print("Błędna komórka pamięci!")
                elif int(obiekt_1, 16) < 65536:
                    obiekt_2 = input("Podaj drugą zawartość rejestru dla instrukcji: ")
                    if obiekt_2.upper() in rejestry:
                        pamiec[int(obiekt_1, 16)] = rejestry[obiekt_2]
                  
                    else:
                        print("Błędny rejestr!")
               
                else:
                    print("Błędny rejestr lub komórka pamięci!")
            except ValueError:
                print("Błąd")
        elif akcja == 4:
            dalej=False
       
        else:
            print("Błędna akcja!")
    except ValueError:
        print("\nBłąd!")

