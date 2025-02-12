
# -------------------------------------------------------------
# ANISSE ARTADJI
#        --------------- EXPLICATION DE TOUS LES CODES----------------

# Premierement Vous devez installer le module verbecc dont la commande est la suivate:
# pip install verbecc.

#  *   Le etoile signifie Importer Tous.

from verbecc import Conjugator
from tkinter import Text
import tkinter as tk
from tkinter import ttk

def conjuguer():
    verbe = entryVerbe.get()
    temps = listeVerbes.get()
    cg = Conjugator(lang='fr')
    conjugation = cg.conjugate(verbe)
    conj = conjugation['moods']['indicatif'][temps]
    result = ""
    for element in conj:
        result = result + element + '\n'
    T.insert(1.0 , "CONJUGAIS LE VERBE: " + verbe + ' AU/A  ' + temps + '\n\n' + result)

# --------------------
# fenetre principale
# -------------------
root = tk.Tk()
root.title("DEVELOPPEUR ANNIX_ART")
root.geometry("600x400")
# création du titre de la fenêtre
lblTitle = tk.Label(root ,
                    text = "Apprendre la conjugaison avec AnnixApp" ,
                    font = ("Arial" , 20) ,
                    foreground='aqua',
                    background='black')
lblTitle.place(x=0 , y= 0 , width=600 )

# -----------------------------------------------------
# label qui demande à l'utilisateur de saisir le verbe
# -----------------------------------------------------
lblVerbe = tk.Label(root , text = "Ecris un verbe")
lblVerbe.place( x = 20 , y = 50,)

entryVerbe = tk.Entry(root)
entryVerbe.place(x = 100 , y = 50 , width = 200 , height = 30 )

# -----------------
# liste verbes
# -----------------
listeTemps = ["présent",  "passé-composé", "passé-simple",
              "imparfait", "plus-que-parfait", "futur-simple",
              "futur-antérieur",  "passé-antérieur" ,]
listeVerbes = ttk.Combobox(root , values = listeTemps)
listeVerbes.place(x = 350 , y = 50 , width = 200,height = 30,)

listeVerbes.current(0)
# -----------------------------------------------------
# zone de texte pour afficher les verbes conjugaisués
# -----------------------------------------------------
T = Text( root )
T.place(x = 100 , y = 100 , width = 566 , height = 620,)


# ------------------
# Creation de Bouton conjuguer.
# -----------------
bConjug = tk.Button(root , text = "( Cliquer ici pour conjugais le verbe )" , command = conjuguer,
font = ("Arial" ,14) ,
foreground='aqua',
background='#FF1493')
bConjug.place(x = 100 , y = 78 , width = 566, height =23)

root.mainloop()
