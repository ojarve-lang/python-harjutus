# Funktsioon, mis leiab nimekirjast kõige pikema sõna pikkuse
def pikim_sona(sonad):
    # sonad on nimekiri sõnadest, näiteks ["mets", "haridus", "niidu"]

    # max() otsib kõige suurema väärtuse
    # len(s) mõõdab iga sõna pikkust (tähtede arvu)
    # for s in sonad käib kõik sõnad läbi
    # kokku tähendab see: leia kõige pikema sõna pikkus
    pikim = max(len(s) for s in sonad)

    # Näitame tulemust ekraanil
    print("Pikima sõna pikkus on:", pikim)

    # Tagastame selle väärtuse, et seda saaks vajadusel edasi kasutada
    return pikim




# Funktsioon, mis leiab nimekirjast kolm kõige pikemat sõna
def kolm_pikimat_sona(sonad):
    # Kontrollime, kas nimekirjas on vähemalt 3 sõna
    # Kui on vähem, siis anname teada ja tagastame tühja nimekirja
    if len(sonad) < 3:
        print("Sõnu on liiga vähe!")
        return []

    # Sorteerime sõnad pikkuse järgi (pikemad ette)
    # key=len tähendab, et sorteerime sõna pikkuse alusel
    # reverse=True tähendab, et alustame kõige pikemast
    # [:3] võtab esimesed kolm sõna sorted-tulemusest
    pikimad = sorted(sonad, key=len, reverse=True)[:3]

    # Prindime kolm pikimat sõna ekraanile
    print("Kolm pikimat sõna on:", pikimad)

    # Tagastame need sõnad, et neid saaks vajadusel edasi kasutada
    return pikimad



# Funktsioon, mis kontrollib, kas kahe sõnaga fraas algab sama tähega
def sarnased_esitahed(sone):
    # split() jagab teksti tühikute järgi osadeks
    # Näiteks 'Vapper Vares' muutub ['Vapper', 'Vares']
    osad = sone.split()

    # Kontrollime, et oleks täpselt kaks sõna
    # Kui on rohkem või vähem, siis ei saa võrrelda
    if len(osad) != 2:
        return False

    # Võtame mõlema sõna esimese tähe ja teeme väikseks (lower()) pythonis "A" ja "a" ei ole samad – nad on erinevad tähed. 
    # Siis võrdleme, kas need tähed on samad
    return osad[0][0].lower() == osad[1][0].lower()

# Testime funktsiooni kahe näitega
print(sarnased_esitahed('Vapper Vares'))     # ➜ True, sest mõlemad algavad V-ga
print(sarnased_esitahed('Lahe Känguru'))     # ➜ False, L ja K on erinevad



# Impordime vajalikud moodulid
import turtle  # graafiline joonistamise tööriist
import random  # juhuslike arvude ja valikute tegemiseks

# Funktsioon ruudu joonistamiseks
def joonista_ruut():
    for _ in range(4):  # ruudul on 4 külge
        turtle.forward(50)  # liigume edasi 50 pikslit
        turtle.right(90)    # pöörame paremale 90 kraadi

# Funktsioon ringi joonistamiseks
def joonista_ring():
    turtle.circle(25)  # joonistame ringi raadiusega 25 pikslit

# Funktsioon viisnurga joonistamiseks
def joonista_viisnurk():
    for _ in range(5):  # viisnurgal on 5 külge
        turtle.forward(50)  # liigume edasi 50 pikslit
        turtle.right(72)    # pöörame paremale 72 kraadi (360 / 5)

# Funktsioon, mis valib juhusliku kujundi nime
def juhuslik_kujund():
    return random.choice(["ruut", "ring", "viisnurk"])  # valib ühe kolmest

# Peamine mängufunktsioon
def kilpkonna_mang():
    while True:  # mäng käib seni, kuni kasutaja lõpetab
        # Küsime kasutajalt, millist kujundit ta soovib
        valik = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? ")
        if valik == "":  # tühi sisend lõpetab mängu
            print("Joonistamine lõpetatud.")
            break

        # Küsime, mitu kujundit joonistada
        try:
            arv = int(input("Mitu kujundit soovid joonistada? "))
        except ValueError:
            print("Palun sisesta arv.")  # kui sisend pole arv
            continue  # hüppame tagasi algusesse

        turtle.speed(0)   # joonistame kiiresti
        turtle.clear()    # puhastame ekraani

        for _ in range(arv):  # kordame nii mitu korda, kui kasutaja soovis
            turtle.penup()  # tõstame pliiatsi üles (ei joonista liikumisel)
            # Liigume juhuslikku kohta ekraanil
            turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
            turtle.pendown()  # paneme pliiatsi alla (hakkame joonistama)

            # Kui valik oli "suvaline", valime juhusliku kujundi
            kujund = valik if valik != "suvaline" else juhuslik_kujund()

            # Joonistame vastava kujundi
            if kujund == "ruut":
                joonista_ruut()
            elif kujund == "ring":
                joonista_ring()
            elif kujund == "viisnurk":
                joonista_viisnurk()
            else:
                print("Tundmatu kujund:", kujund)  # kui sisestus oli vale

        turtle.update()  # uuendame ekraani, et kõik kujundid ilmuksid

# Käivitame mängu ainult siis, kui fail käivitatakse otse
if __name__ == "__main__":
    kilpkonna_mang()









