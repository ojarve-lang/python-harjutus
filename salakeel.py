# See programm teeb salakeelt, lisades igale "silbi" vahele "pii". 🤫

# Defineerime kõik täishäälikud (vokaalid). Need on meie "silbi tuumad".
TAISHÄÄLIKUD = "aeiouõäöüAEIOUÕÄÖÜ"

def loo_pii_keel(sõna):
    """
    Funktsioon, mis muudab tavalise sõna "pii-keeleks".
    Me lihtsustame: lisame 'pii' igale täishäälikuga algavale osale.
    """
    uus_sõna = ""
    i = 0  # Indeks, mis näitab, kus me sõnas oleme
    
    # Liigume sõnas edasi, kuni jõuame lõpuni
    while i < len(sõna):
        täht = sõna[i]
        
        # 1. Kontrollime, kas täht on täishäälik
        if täht in TAISHÄÄLIKUD:
            # See on silbi algus (vokaal). Lisame sellele kohale 'pii'.
            uus_sõna += "pii"
            # Lisame ka täishääliku
            uus_sõna += täht
            i += 1  # Liigume edasi järgmisele tähele
        else:
            # 2. See on kaashäälik. Jätame selle muutmata.
            uus_sõna += täht
            i += 1
            
    return uus_sõna

def tõlgi_pii_keel(pii_keelne_sõna):
    """
    Funktsioon, mis tõlgib "pii-keele" tagasi normaalseks.
    Kõik "pii" lühendid eemaldatakse ja alles jääb vaid originaalsõna.
    """
    # Kõige lihtsam viis tagasi tõlkimiseks on asendada kõik "pii" jada nulliga.
    # Muudame sõna väiketäheliseks, et asendus töötaks alati
    väike_sõna = pii_keelne_sõna.lower()
    
    # Asendame kõik "pii" stringid tühja stringiga ""
    tõlgitud_sõna = väike_sõna.replace("pii", "")
    
    return tõlgitud_sõna

def pii_keele_programm():
    """
    Põhifunktsioon, mis küsib kasutajalt valiku (loo või tõlgi).
    """
    
    # 1. Küsime kasutajalt valiku (1p)
    print("-----------------------------------------")
    print("Tere tulemast Pii-Keele Mängu! 🗣️")
    print("Mida sa soovid teha?")
    print("Valik 1: **Loo salakeel** (Tavaline sõna -> Pii-keelne sõna)")
    print("Valik 2: **Tõlgi salakeel** (Pii-keelne sõna -> Tavaline sõna)")
    
    valik = input("Sisesta valiku number (1 või 2): ")
    print("-----------------------------------------")
    
    if valik == '1':
        # 2. Kasutaja valis salakeele loomise
        tavaline_sõna = input("Sisesta tavaline sõna: ")
        # Loo 'pii'-keel
        tulemus = loo_pii_keel(tavaline_sõna)
        print(f"✅ Sinu **Pii-keelne** sõna on: **{tulemus}**")
        
    elif valik == '2':
        # 3. Kasutaja valis salakeele tõlkimise
        pii_keelne_sõna = input("Sisesta Pii-keeles sõna, mida soovid tõlkida: ")
        # Tõlgi 'pii'-keel tagasi normaalseks
        tulemus = tõlgi_pii_keel(pii_keelne_sõna)
        print(f"✅ Tõlgitud sõna on: **{tulemus}**")
        
    else:
        # Viga, kui valik ei olnud 1 ega 2
        print("❌ Viga! Palun vali kas 1 (loo) või 2 (tõlgi).")

# Kutsume põhifunktsiooni käima
pii_keele_programm()

# Lõpp