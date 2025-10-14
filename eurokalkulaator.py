# See on Eurokalkulaator! 
# See programm aitab meil kroone eurodeks või eurosid kroonideks muuta.

# Euro ametlik kurss Eesti krooni suhtes on 15.6466
# Allikas: https://www.eestipank.ee/valuuta-kursid
KURSS = 15.6466 

def euro_kalkulaator():
    """
    Peamine funktsioon, mis juhib kogu kalkulaatori tööd.
    """
    # 1. Küsime kasutajalt, mida ta soovib teha
    print("Tere tulemast Eurokalkulaatorisse! 🇪🇺")
    print("Mida sa soovid arvutada?")
    print("Valik 1: Eurod (EUR) -> Eesti kroonid (EEK)")
    print("Valik 2: Eesti kroonid (EEK) -> Eurod (EUR)")
    
    # Küsime kasutajalt numbrit (1 või 2)
    valik = input("Sisesta valiku number (1 või 2): ")
    
    # 2. Kontrollime, kas valik on õige (1 või 2)
    if valik not in ('1', '2'):
        # Kui valik on vale (ei ole '1' ega '2'), näitame veateadet ja lõpetame programmi
        print("-----------------------------------------")
        print(f"❌ Viga! Sa sisestasid '{valik}'. Palun vali kas 1 või 2.")
        print("Proovi palun uuesti!")
        return # Lõpetame programmi töö
    
    # 3. Küsida valuuta kogust
    try:
        # Küsida kasutajalt, kui palju raha ta soovib muuta
        kogus = float(input("Sisesta summa, mida soovid vahetada (kasuta koma asemel punkti!): "))
    except ValueError:
        # Veateade, kui sisestatud summa pole number
        print("-----------------------------------------")
        print("❌ Viga! See pole number. Palun sisesta summa numbrina.")
        return

    # 4. Teeme arvutused vastavalt valikule (1 või 2)
    
    if valik == '1':
        # Eurod kroonideks: summa * kurss
        tulemus = kogus * KURSS
        
        # Näitame korrektset vastust 
        print("-----------------------------------------")
        # Funktsioon 'round(arv, 2)' näitab ainult 2 numbrit pärast punkti
        print(f"✅ Vastus: {kogus:.2f} eurot (EUR) on {tulemus:.2f} Eesti krooni (EEK).")
        print("Arvutus: summa korda kurss (15.6466)")

    elif valik == '2':
        # Kroonid eurodeks: summa / kurss
        tulemus = kogus / KURSS
        
        # Näitame korrektset vastust 
        print("-----------------------------------------")
        print(f"✅ Vastus: {kogus:.2f} Eesti krooni (EEK) on {tulemus:.2f} eurot (EUR).")
        print("Arvutus: summa jagada kursiga (15.6466)")

# Kutsume funktsiooni esmakordselt käima, et programm alustaks
euro_kalkulaator()
# Lõpp


