"""
Kujundite joonistamise programm

Programm joonistab ekraanile juhuslikke kujundeid:
- ruudu
- ringi
- viisnurga
- suvalise kujundi

Valikus mitu kujundit joonistada ja millist tüüpi.
Kujundid ilmuvad juhuslikku kohta ja on juhuslikult värvitud.

Märkus:kasutasin programmi tegemisel abi.
Sõbranna juhendas, kuidas teha suvalisi koordinaate, valida värve
ja joonistada täidetud kujundeid.
"""

import turtle
import random

# ekraan ja kilpkonn
aken = turtle.Screen()
aken.setup(800, 600)
aken.title("Kujundite joonistamine")
kilp = turtle.Turtle()
kilp.speed(0)


def joonista_kujund(tyyp, suurus):
    """
    Joonistab ühe kujundi ekraanile.

    Argumendid:
    tyyp (str): "ruut", "ring", "viisnurk" või "suvaline"
    suurus (int): kujundi külje pikkus või ringi raadius

    """
    # kilpkonna viimine juhuslikku kohta
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    kilp.penup()
    kilp.goto(x, y)
    kilp.pendown()
    kilp.setheading(random.randint(0, 360))

    # värvi valimine juhuslikult ja kujundite joonistamine
    kilp.color(random.random(), random.random(), random.random())
    kilp.begin_fill()

    if tyyp == "ruut":
        for _ in range(4):
            kilp.forward(suurus)
            kilp.right(90)
    elif tyyp == "ring":
        kilp.circle(suurus)
    elif tyyp == "viisnurk":
        for _ in range(5):
            kilp.forward(suurus)
            kilp.right(72)
    elif tyyp == "suvaline":

        joonista_kujund(random.choice(["ruut", "ring", "viisnurk"]), suurus)

    kilp.end_fill()


while True:
    tyyp = input(
        "Millist kujundit joonistada (ruut, ring, viisnurk, suvaline)? ")
    if tyyp.strip() == "":
        break
    arv = input("Mitu kujundit? ")
    if arv.strip() == "":
        break
    arv = int(arv)

    kilp.clear()
    for _ in range(arv):
        suurus = random.randint(30, 100)
        joonista_kujund(tyyp.lower(), suurus)

    j = input("Soovid jätkata? (Enter lõpetab) ")
    if j.strip() == "":
        break

turtle.bye()
