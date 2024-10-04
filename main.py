"""
Diese Datei ist der gesamte einfache Passwortgenerator.
"""

import tkinter
from string import ascii_lowercase, ascii_uppercase
import random
from random import sample



def passwortgenerator():
    laenge = 10
    zufall = []
    zufall_bearbeitet = []
    passwort = []
    menge = random.randint(3, 9)
    gross = ascii_uppercase
    klein = ascii_lowercase
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    sonderzeichen = "[@_><!#$%^&*()<>?/|}{~:]\\\'"
    for element in gross, klein, zahlen, sonderzeichen:
        zufall.append(sample(element, menge))           # hier wird eine Liste mit dem zufälligen Zeichenpool erstellt.
    for element in zufall:                              # In den Zeilen darunter wird alles zusammengeführt.
        teil = sample(element, 3)
        zufall_bearbeitet.append(teil)
    passwortpool = list(vereinfachen(zufall_bearbeitet))
    passwort_liste = sample(passwortpool, laenge)   # Diese Zeile gibt ein Passwort aus dem erstellten Zeichenpool aus.
    for element in passwort_liste:
        element = str(element)
        passwort.append(element)
    passwort = "".join(passwort)               # Hier wird das Passwort in seine finale Form gebracht.
    passwort_feld.delete(0, tkinter.END)  # TKinter-Feld beim Generieren leeren.
    passwort_feld.insert(0, passwort)    # Für die Anzeige in TKinter.


def vereinfachen(liste):
    for element in liste:
        if isinstance(element, list):
            yield from vereinfachen(element)
        else:
            yield element

# Ab hier beginnt die GUI-Komponente.

fenster = tkinter.Tk()
fenster.title("Passwortgenerator")
fenster.geometry("350x150")
fenster.resizable(False, False)

fenster.configure(bg="#C39BD3")  # Hintergrund

passwort_feld = tkinter.Entry(fenster, width=30, font=('Arial', 14), justify='center', bd=3, bg='white')
passwort_feld.pack(pady=20)

button = tkinter.Button(fenster, text="Neues Passwort erstellen", font=('Arial', 12),
                        command=passwortgenerator, bg='#ADD8E6')
button.pack(pady=10)


fenster.mainloop()
