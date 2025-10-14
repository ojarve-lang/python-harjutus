# See programm teeb meist täringumängu meistrid! 🎲

import random # Impordime "random", mis aitab meil täringut veeretada (saamejuhuslikud numbrid)

# Panus, mille mängu alguses lauale paneme (kõik on lihtne ja fikseeritud!)
LAUA_RAHA = 10 

def veereta_taringut():
    """
    Funktsioon, mis simuleerib kahe täringu viskamist.
    Iga täring annab numbri 1 ja 6 vahel.
    """
    # Esimene täring: juhuslik number 1st kuni 6ni
    taring1 = random.randint(1, 6)
    # Teine täring: juhuslik number 1st kuni 6ni
    taring2 = random.randint(1, 6)
    
    # Täringute kogusumma
    summa = taring1 + taring2
    
    # Tagastame nii täringute summad kui ka üksikud tulemused (et oleks huvitavam)
    return summa, taring1, taring2 

def taringu_mangu_kalkulaator():
    """
    Mängu põhifunktsioon, kus toimub kogu võistlus.
    """
    
    # 1. Küsime kasutajalt, kas ta on valmis mängima
    print("-----------------------------------------")
    print("🌟 Tere tulemast Täringumängu! 🌟")
    print(f"Iga mängu panus (raha laual) on **{LAUA_RAHA} eurot**.")
    
    # Küsib, kas mängija tahab mängida. 
    input("Vajuta 'Enter', et oma kahe täringuga visata ja mängida... ") 
    print("-----------------------------------------")

    # 2. Kasutaja viskab täringuid
    # Anname teada, et nüüd veeretab täringut kasutaja
    print("👉 Sinu kord visata täringuid...")
    sinu_summa, sinu_t1, sinu_t2 = veereta_taringut()
    
    # Näitame kasutaja tulemusi
    print(f"Sinu täringud: {sinu_t1} ja {sinu_t2}.")
    print(f"**Sinu kogusumma on: {sinu_summa}**")
    
    print("\n---") # Väike eraldaja

    # 3. Arvuti viskab täringuid
    # Anname teada, et nüüd veeretab täringut arvuti (vastane!)
    print("🤖 Arvuti kord visata täringuid...")
    arvuti_summa, arvuti_t1, arvuti_t2 = veereta_taringut()
    
    # Näitame arvuti tulemusi
    print(f"Arvuti täringud: {arvuti_t1} ja {arvuti_t2}.")
    print(f"**Arvuti kogusumma on: {arvuti_summa}**")
    
    print("-----------------------------------------")

    # 4. Teeme võrdluse ja kuulutame võitja
    
    # Kui sinu summa on suurem kui arvuti summa
    if sinu_summa > arvuti_summa:
        # Võitja saab laual oleva raha endale
        print(f"🎉 PALJU ÕNNE! **Sina võitsid**! {sinu_summa} > {arvuti_summa}")
        print(f"Võitsid laualt {LAUA_RAHA} eurot!")
        
    # Kui arvuti summa on suurem kui sinu summa
    elif arvuti_summa > sinu_summa:
        # Arvuti saab raha endale
        print(f"😭 Kahjuks **võitis arvuti**! {arvuti_summa} > {sinu_summa}")
        print(f"Arvuti võitis laualt {LAUA_RAHA} eurot.")
        
    # Kui summad on võrdsed
    else:
        # Jääb viigiks ja raha läheb uueks mänguks
        print(f"🤝 VIK! Mõlemad saite {sinu_summa} punkti. Raha (panus) jääb lauale järgmise mänguni.")

# Kutsume funktsiooni käima, et mäng algaks
taringu_mangu_kalkulaator()

# Lõpp
