# Programm, mis kontrollib, kas arv on paaris või paaritu
print("Arvu paarisuse kontroll")

# Küsime kasutajalt arvu
sisend = input("Palun sisesta täisarv: ")

try:
    # Proovime kasutaja sisestatud teksti arvuks muuta
    arv = int(sisend)

    # Kontrollime, kas arv jagub 2-ga (jääk on 0)
    if arv % 2 == 0:
        # Kui jääk on 0, on arv paaris
        print(f"Arv {arv} on paaris.")
    else:
        # Kui jääk ei ole 0, on arv paaritu
        print(f"Arv {arv} on paaritu.")

except ValueError:
    # See kood käivitub siis, kui kasutaja ei sisestanud arvu (nt tähed)
    print("Viga: sa ei sisestanud korrektset täisarvu!")
