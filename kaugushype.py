# KAUGUSHÜPPE PROGRAMM
# See programm küsib kasutajalt kolme hüppe tulemused ja leiab parima ning keskmise tulemuse.

# Küsime kasutajalt kolm hüppe tulemust meetrites
hüpe1 = float(input("Sisesta esimese hüppe tulemus (meetrites): "))
hüpe2 = float(input("Sisesta teise hüppe tulemus (meetrites): "))
hüpe3 = float(input("Sisesta kolmanda hüppe tulemus (meetrites): "))

# Paneme kõik tulemused ühte nimekirja (listi)
tulemused = [hüpe1, hüpe2, hüpe3]

# Leiame parima (suurima) tulemuse
parim = max(tulemused)

# Leiame keskmise tulemuse (summa / kogus)
keskmine = sum(tulemused) / len(tulemused)

# Kuvame tulemused ekraanile
print(f"Parim hüpe oli {parim} meetrit.")
print(f"Keskmine hüpe oli {round(keskmine, 2)} meetrit.")  # ümardame kahe komani
# Lõpp
