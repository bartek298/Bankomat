import os
pin_bankomatu=3456
stan_konta=open("stan.txt","r")
plik=open("stan.txt","r")
stan_konta=int(plik.read())
plik.close()
proby=3


def poprawny_pin(pin,pin_bankomatu):
    return pin==pin_bankomatu
def logowanie_sukces():
    os.system("cls")
    print("Zalogowales sie pomyslnie")
def wyswietl_menu():
    print("Witaj w systemie bankomatu.")
    print("Co chcesz zrobic?")
    print("""
    ####################
    1.Sprawdz stan konta
    2.Wypłać
    3.Wpłać
    4.Wyloguj się
    ####################
    
    """)
def wyswietl_stan_konta():
    os.system("cls")
    print(f"Twój stan konta to:{stan_konta}")
def wyplac_pieniadze():
    global stan_konta
    os.system("cls")
    ile=int(input("podaj ile chcesz wyplacic:"))
    while ile>stan_konta:
        print("nie masz tyle na koncie")
        ile=int(input("ile chcesz wyplacic:"))
    stan_konta-=ile
    plik=open("stan.txt","w")
    plik.write(str(stan_konta))
    plik.close()
    print(f"po wyplaceniu masz:{stan_konta} na swoim koncie. ")
def wplac_pieniadze():
    global stan_konta
    os.system("cls")
    ile2=int(input("ile chcesz wplacic:"))
    stan_konta+=ile2
    print(f"po operacji masz:{stan_konta} na koncie.")
    plik=open("stan.txt","w")
    plik.write(str(stan_konta))
    plik.close()

while True:
    pin=int(input("podaj pin: "))
    if poprawny_pin(pin,pin_bankomatu) and proby>0:
        logowanie_sukces()
        while True:
            wyswietl_menu()
            opcja=int(input("Wybierz numer operacji od 1 do 4:"))
            if opcja== 1:
                wyswietl_stan_konta()
            elif opcja==2:
                wyplac_pieniadze()
            elif opcja==3:
                wplac_pieniadze()
            elif opcja==4:
                os.system("cls")
                print("zostales wygolowany")
                
                break
            else:
                os.system("cls")
                print("wpisales zla opcje:")
                continue
                


    else:
        os.system("cls")
        print("Wpisales bledny pin, spróbuj ponownie.")
        proby-=1
        print(f"masz {proby} prob")
        if proby==0:
            break



