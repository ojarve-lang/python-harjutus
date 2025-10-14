# EMAILI KONTROLL
# See programm küsib kasutajalt emaili, kontrollib seda ja väljastab info selle põhjal.

# Küsime kasutajalt tema emaili
email = input("Palun sisesta oma email (nt enimi.pnimi@server.com): ")

# Kontrollime, kas emailis on olemas @ märk
if "@" in email:
    # Kui on, siis tükeldame emaili osadeks
    # Esiteks jagame emaili kaheks: vasak (enne @) ja parem (pärast @)
    vasak, parem = email.split("@")
    
    # Vasak pool sisaldab ees- ja perekonnanime
    # Jagame selle veel kord, et saada eesnimi ja perenimi
    enimi, pnimi = vasak.split(".")
    
    # Parem pool sisaldab serverit ja domeeni (nt server.com)
    server, domeen = parem.split(".")
    
    # Nüüd kuvame tulemuse sõbralikus lauses
    print(f"Tere {enimi}, sinu email on {server} serveris ja domeeniks on sul {domeen}.")
else:
    # Kui @ märki pole, siis anname kasutajale teada, et email on valesti sisestatud
    print("Viga! Email peab sisaldama @ märki. Proovi uuesti.")
# Lõpp