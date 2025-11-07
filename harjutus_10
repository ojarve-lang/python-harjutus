import random  # Et mängus oleksid juhuslikud arvud

# Siin paneme kõik mängu tulemused (mitu korda arvati enne õiget vastust)loome nurksulgudega listi
tulemused = []

# Mängime seni, kuni kasutaja tahab
while True:
    salajane = random.randint(1, 10)  # Loome juhusliku arvu 1–10
    katseid = 0  # Loendame, mitu korda kasutaja arvab

    print("Arva ära arv vahemikus 1 kuni 10!")

    while True:
        pakkumine = input("Sinu pakkumine: ")
        katseid += 1  # Iga kord kui küsime, tuleb üks katse juurde

        # Kontrollime, kas sisestatud arv on õige
        if not pakkumine.isdigit():
            print("Palun sisesta arv.")
            continue  # Hüppame järgmise katse juurde

        arv = int(pakkumine)

        if arv == salajane:
            print("OK! Õige arv!")
            print(f"Arvasid ära {katseid}. katsel.")
            tulemused.append(katseid)  # Salvestame tulemuse
            break  # Lõpetame selle mängu
        else:
            print("Ei ole õige. Proovi uuesti!")

    # Küsime, kas tahad uuesti mängida
    uuesti = input("Mängid veel? (jah/ei): ").lower()
    if uuesti != "jah":
        print("Aitäh mängimast!")
        print("Sinu tulemused:")
        for i, tulemus in enumerate(tulemused, 1):
            print(f"{i}. mäng: {tulemus} katset")
        break  # Kui ei taha, siis lõpetame mängu

