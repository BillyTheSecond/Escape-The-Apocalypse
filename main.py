"""
Nom du Jeu : Escape The Apocalypse 


Inventeurs, Créateurs & développeurs : Clara, Quentin & Louison

Graphismes : Clara


"""

#libraries
import os
import time
import math
from tkinter import *
from tkinter.messagebox import *
from tkinter import PhotoImage
from random import randint
import webbrowser
""" 
NIVEAUX:
  - 1 : Facile, ne demande aucune compétences en programation. Les réponses sont preque données
  - 2 : Normal, demande des compétences en encodage des nombres et en python basiques



note 2 : Le jeu tourne pour le moment dans la console.

note 3 : Les modifications du code pour donner une interface graphique au jeu seront conséquentes et demanderont plus de temps





"""
# INTERFACE GRAPHIQUE

# déclare la fenetre avant le code pour éviter des erreurs avec PhotoImage
fenetre = Tk()

#VARIABLES ET FONCTIONS GENERALES

# global code
code = ""

#Dictionnaires des questions et réponses

#mini-jeu booleen

# pour le niveau 1
questions_bool_1 = {
    1:
    "Oh ! L'ordinateur me propose de travailler ma logique pour trouver le code !\nQue renvoie l'expression Python 'True and True' ?\nFaisons une image mentale de cette expression pour mieux répondre ! Si une porte est verrouillée avec 2 cadenas, et que les deux sont ouverts. S'ouvre-t-elle ? ",
    2:
    "Que renvoie l'expression 'True and False' ?\nFaisons une image contrète. Si une porte est verrouillée avec 2 cadenas, et que un seul d'entre-eux est ouvert. S'ouvre-t-elle ?",
    3:
    "L'ordinateur est programmé en Python et demande le résultat l'expression 'False and False'.\nDeux interrupteurs se succèdent sur un circuit électrique alimenté qui permet d'allumer une lampe.\nLes deux sont éteints (False), c'est à dire ouverts. La lampe est-elle allumée (True) ou éteinte (False) ?",
    4:
    "L'ordinateur du bunker nous demande la solution d'une expression bizarre.\nQue fait 'True or True' ? \nLa solution est soit True, soit False."
}
#réponses aux questions
reponses_bool_1 = {1: True, 2: False, 3: False, 4: True}
#images correspondant aux enigmes (dans le type PhotoImage)
images_bool_1 = {
    1: PhotoImage(file="interface finale/1 jeu booleen/niveau 1/Question 1.png"),
    2: PhotoImage(file="interface finale/1 jeu booleen/niveau 1/Question 2.png"),
    3: PhotoImage(file="interface finale/1 jeu booleen/niveau 1/Question 3.png"),
    4: PhotoImage(file="interface finale/1 jeu booleen/niveau 1/Question 4.png")
}

#pour le niveau 2
questions_bool_2 = {
    1:
    "Il vous est demandé sur l'écran de l'ordinateur ce que donne l'expression 'True or False'. \nVos parents avaient sûrement, tout comme vous, des compétences en langage Python ! ",
    2:
    "Après sa mort, votre mère, Angela, vous a donné son carnet de bord. \nA la page 56, se trouve une étrange expression qu'elle a entouré et qui semble l'avoir beaucoup embêtée. \nIl est inscrit 'True xor True'. Sauriez-vous résoudre ce problème ?",
    3:
    "Oh ! Vous avez ouvert le journal intime de votre père et vous êtes tombé sur une inscription... \nElle a été écrite si intensément que l'inscription traverse la page.\nOn peut y lire '(True or True) and (True and False)'. Que renvoie cette expression?",
    4:
    "Mais quelle est donc cette expression que vous demande l'ordinateur !?\n'(True or False) xor False'\nTrouvez la réponse pour débloquer l'ordinateur !",
    5:
    "Il vous est demandé sur l'écran de l'ordinateur ce que donne l'expression 'True or False'. \nVos parents avaient sûrement, tout comme vous, des compétences en langage Python ! ",
}
reponses_bool_2 = {1: True, 2: False, 3: False, 4: True, 5: True}
images_bool_2 = {
    1: PhotoImage(file="interface finale/1 jeu booleen/niveau 2/Question 1 et 5.png"),
    2: PhotoImage(file="interface finale/1 jeu booleen/niveau 2/Question 2.png"),
    3: PhotoImage(file="interface finale/1 jeu booleen/niveau 2/Question 3.png"),
    4: PhotoImage(file="interface finale/1 jeu booleen/niveau 2/Question 4.png"),
    5: PhotoImage(file="interface finale/1 jeu booleen/niveau 2/Question 1 et 5.png")
}

#mini de jeu conversion

#pour le niveau 1
questions_conversion_1 = {
    1:
    "L'ordinateur du bunker vous demande votre âge. Vous avez 17 ans mais il n'y a pas  de touche 7... \nVous pouvez uniquement appuyer sur les boutons 0 ou 1.",
    2:
    "En fouillant le Bunker, vous remarquez un graffiti sur le mur. Il indique '1010 février 2521'. \nMais à quoi ce nombre peut il bien correspondre ? Il n'y a pourtant pas 1010 jours en février...",
    3:
    "En fouillant le Bunker, vous remarquez un graffiti sur le mur. Il indique '1011'. \nC'est peut-être une partie du code ! Essayons de le convertir en base décimale.",
    4:
    "Votre père, qui ne semble pas très organisé, vous a transmis ses brouillons.\nVous remarquez qu'il a écrit le nombre '1001 1101 1001' sur de nombreuses pages sans indiquer sa signification.\nSauriez-vous traduire ce nombre qui semblait très important pour votre père"
}

reponses_conversion_1 = {1: 10001, 2: 10, 3: 11, 4: 2521}
#images correspondantes
images_conversions_1 = {
    1: PhotoImage(file="interface finale/2 jeu conversion/niveau 1/Question 1.png"),
    2: PhotoImage(file="interface finale/2 jeu conversion/niveau 1/Question 2.png"),
    3: PhotoImage(file="interface finale/2 jeu conversion/niveau 1/Question 3.png"),
    4: PhotoImage(file="interface finale/2 jeu conversion/niveau 1/Question 4.png")
}

# pour le niveau 2
questions_conversion_2 = {
    1:
    "Au fait ! Savez vous en quelle année nous sommes ? N'y aurait-il pas un moyen de le savoir ? \nL'ordinateur semble tout faire pour nous embêter ! Il dit que nous sommes en l'an 1001 1111 0110 . \nIl va falloir calculer !",
    2:
    "C'est possible que mes parents aient mis ma date de naissance comme code. Je devais être important à leurs yeux ! \nIl est bien possible de connaitre mon année de naissance. \nJe sais que j'ai 17 ans et que nous sommes en 2550. Mais ce fichu ordinateur veut que je la rentre en langage binaire...",
    3:
    "Un message codé est gravé sur la paroi du bunker, au dessus de l'ordinateur. On peut lire ¤##¤ ¤¤¤# #¤#?. \nCe doit surement être un morceau du code ! Vous avez remarqué que le ¤ correspondait à un 1 et que le # correspondait à un 0. \nMais le dernier caractère est indiscernable... Tentez de trouver ce code et rentrez-le dans l'ordinateur en base décimale",
    4:
    "Oh non... L'ordinateur n'arrive pas à décoder un message... Nous allons devoir le faire nous-même. \nIl affiche cette fois un messsage en base hexadécimale: 'A/2/9D9'.\nN'oublions pas de conserver le format d'écriture dans notre réponse"
}

reponses_conversion_2 = {1: 2550, 2: 100111100101, 3: 2533, 4: "10/2/2521"}
images_conversions_2 = {
    1: PhotoImage(file="interface finale/2 jeu conversion/niveau 2/Question 1.png"),
    2: PhotoImage(file="interface finale/2 jeu conversion/niveau 2/Question 2.png"),
    3: PhotoImage(file="interface finale/2 jeu conversion/niveau 2/Question 3.png"),
    4: PhotoImage(file="interface finale/2 jeu conversion/niveau 2/Question 4.png")
}



#mini_jeu couleurs
questions_couleur_1 = {
    1:
    "En fouillant l’ordinateur, vous remarquez que son fond d’écran est constitué de la couleur primaire verte. \nIl y aussi un petit texte qui dit « celui qui donnera le code RGB de la couleur de mon fond d’écran aura une partie du code ».",
    2:
    "En fouillant l’ordinateur, vous remarquez que son fond d’écran est constitué de la couleur primaire bleu. \nIl y aussi un petit texte qui dit « celui qui donnera le code RGB de la couleur de mon fond d’écran aura une partie du code ».",
    3:
    "«Red is rgb(255,0,0), Blue is rgb(0,0,255) so magenta is ..... » \nIl est impossible de lire la suite de ce message trouvé dans le carnet de votre père.\nCela ne nous rapelle-t-il pas un certain principe d'additivité des couleurs ?"
}  #niveau 1
reponses_couleur_1 = {
    1: "rgb(0, 255, 0)",
    2: "rgb(0, 0, 255)",
    3: "rgb(255,0,255)"
}
images_couleurs_1 = {
  1: PhotoImage(file="interface finale/3 jeu couleur/niveau 1/Question 1.png"), 
  2: PhotoImage(file="interface finale/3 jeu couleur/niveau 1/Question 2.png"), 
  3: PhotoImage(file="interface finale/3 jeu couleur/niveau 1/Question 3.png")}
#niveau 2
questions_couleur_2 = {
    1:
    "En fouillant l’ordinateur, vous remarquez que son fond d’écran est constitué de la couleur primaire verte. \nIl y aussi un petit texte qui dit « celui qui donnera la syntaxe hexadécimale de la couleur de mon fond d’écran aura une partie du code ».",
    2:
    "En fouillant l’ordinateur, vous remarquez que son fond d’écran est constitué de la couleur primaire bleu. \nIl y aussi un petit texte qui dit « celui qui donnera la syntaxe hexadécimale de la couleur de mon fond d’écran aura une partie du code ».",
    3:
    "Après avoir consulté l'ordinateur, vous tentez de résoudre l'énigme suivante : \nBleu donne #0000FF, Vert donne #00FF00 mais que donne Cyan ?",
    4:
    "Après avoir consulté l'ordinateur, vous tentez de résoudre l'énigme suivante : \nRouge donne #FF0000, Vert donne #00FF00 mais que donne Jaune ?"
}
#réponses
reponses_couleur_2 = {1: "#00FF00", 2: "#0000FF", 3: "#00FFFF", 4: "#FFFF00"}
#images
images_couleurs_2 = {
  1: PhotoImage(file="interface finale/3 jeu couleur/niveau 2/Question 1.png"), 
  2: PhotoImage(file="interface finale/3 jeu couleur/niveau 2/Question 2.png"), 
  3: PhotoImage(file="interface finale/3 jeu couleur/niveau 2/Question 3.png"), 
  4: PhotoImage(file="interface finale/3 jeu couleur/niveau 2/Question 4.png")}

#mini-jeu message codé

#niveau 1
questions_message_code_1 = {
    1:
    "On dirait qu'il y a un post'it sur l'ordinateur avec écrit '42 55 47'. \nIl se trouve qu'il y a un tableau pour convertir ce code sur le mur. Que veut il dire ?",
    2:
    "On dirait qu'il y a un post'it sur l'ordinateur avec écrit '42 4f 55 4d'. \nIl se trouve qu'il y a un tableau pour convertir ce code sur le mur. Que veut il dire ?",
    3:
    "Une notification vient d'arriver sur l'ordinateur, elle indique '47 41 5a'\nIl se trouve qu'il y un fichier joint avec un tableau qui pourrait servir à convertir ce code. Que veut dire ce code ?",
    4:
    "Une notification vient d'arriver sur l'ordinateur, elle indique '4c 41 42 4f'\nIl se trouve qu'il y un fichier joint avec un tableau qui pourrait servir à convertir ce code.Que veut dire ce code ?",
    5:
    "On dirait qu'il y a un post'it sur l'ordinateur avec écrit '53 4f 53'. \nIl se trouve qu'il y a un tableau pour convertir ce code sur l' ordinateur. Que veut-il dire ?"
}
reponses_message_code_1 = {1: "BUG", 2: "BOUM", 3: "GAZ", 4: "LABO", 5: "SOS"}
images_message_code_1 = {
  1: PhotoImage(file="interface finale/4 jeu message/niveau 1/Question 1.png"), 
  2: PhotoImage(file="interface finale/4 jeu message/niveau 1/Question 2.png"),  
  3: PhotoImage(file="interface finale/4 jeu message/niveau 1/Question 3.png"), 
  4: PhotoImage(file="interface finale/4 jeu message/niveau 1/Question 4.png"), 
  5: PhotoImage(file="interface finale/4 jeu message/niveau 1/Question 5.png"), 
  }

#niveau 2
questions_message_code_2 = {
    1:
    "Après avoir fouillé dans les papiers qui se trouvaient sur le bureau, vous tombez sur un étrange code '42 4f 4d 42 45'. \nEn dessous de ce code il y a tableau. \nQue veut dire ce code ? ",
    2:
    "Après avoir fouillé dans les papiers qui se trouvaient sur le bureau, vous tombez sur un étrange code '44 41 4e 47 45 52'. \nEn dessous de ce code il y a tableau. \nQue veut dire ce code ?",
    3:
    "Je crois avoir trouvé un journal datant d'avant l'apocalypse. A la fin, il y a un code marquant '4d 45 4e 41 43 45'. \nPeut-être serait il pour devenir du danger ? \nGrâce au tableau au début du journal, je vais essayer de le décripter"
}
reponses_message_code_2 = {1: "BOMBE", 2: "DANGER", 3: "MENACE"}
images_message_code_2 = {
  1: PhotoImage(file="interface finale/4 jeu message/niveau 2/Question 1.png"),  
  2: PhotoImage(file="interface finale/4 jeu message/niveau 2/Question 2.png"), 
  3: PhotoImage(file="interface finale/4 jeu message/niveau 2/Question 3.png"), 
  }


#images génériques
repertoire_images_générales = {
  "fond":PhotoImage(file="interface finale/0 image de fond.png"),
  "fond_code_secret": PhotoImage(file="interface finale/5 fond code secret.png"),
  "fond_de_fin": PhotoImage(file="interface finale/6 fond de fin.png")
}

# PARTIE DE CLARA + Toutes les illustrations


# fonction qui lance le mini jeu booleen
def mini_jeu_booleen():
    nb_aleatoire = randint(
        1, len(questions_et_reponses[1][1])
    )  # choisi un nombre aléatoire compris entre 1 et le nombre total de questions du mini jeu booléen
    print(f"numéro de questioon : {nb_aleatoire}")
    os.system("clear")
    print(f"numéro de l'image : {nb_aleatoire}")
    global level
    print("Niveau choisi :", level)
    creer_interface_minijeux(1, nb_aleatoire)

# fonction qui lance le mini jeu conversions
def mini_jeu_conversions():
    nb_aleatoire = randint(
        1, len(questions_et_reponses[2][1])
    )  # choisi un nombre aléatoire compris entre 1 et le nombre total de questions du mini jeu conversions
    print(f"numéro de question : {nb_aleatoire}")
    os.system("clear")
    print(f"numéro de l'image : {nb_aleatoire}")
    global level
    print("Niveau choisi :", level)
    creer_interface_minijeux(2, nb_aleatoire)

# fonction qui lance le mini-jeu couleurs
def mini_jeu_couleurs():
    nb_aleatoire = randint(
        1, len(questions_et_reponses[3][1])
    )  # choisi un nombre aléatoire compris entre 1 et le nombre total de questions du mini jeu couleurs
    print(f"numéro de  question : {nb_aleatoire}")
    os.system("clear")
    print(f"numéro de l'image : {nb_aleatoire}")
    global level
    print("Niveau choisi :", level)
    creer_interface_minijeux(3, nb_aleatoire)

# fonction qui lance le mini-jeu message codé
def mini_jeu_message_code():
    nb_aleatoire = randint(
        1, len(questions_et_reponses[4][1])
    )  # choisi un nombre aléatoire compris entre 1 et le nombre total de questions du mini jeu message codé
    print(f"numéro de la question : {nb_aleatoire}")
    os.system("clear")
    print(f"numéro de l'image : {nb_aleatoire}")
    global level
    print("Niveau choisi :", level)
    creer_interface_minijeux(4, nb_aleatoire)


# vérifier les réponses pour l'interface avec une Entry() et un Button() de validation
def verifier_reponses(numero_de_minijeu, numero_de_la_question, level,
                      reponse):
    global nombre_de_tentatives
    # si il reste des tentatives
    nb_de_tentatives = ajouter_une_tentative()
    print('Tentative n°', nombre_de_tentatives)
    if 3 - nombre_de_tentatives >= 0:
        #si la réponse est bonne (en supprimant tous les espaces pour eviter toute erreur de validation due à un espace en trop)
        if str(reponse).upper().replace(" ", "") == str(
                questions_et_reponses[numero_de_minijeu][2]
            [numero_de_la_question]).upper().replace(" ", ""):
            detruire_interface()
            ajouter_au_code(
                str(questions_et_reponses[numero_de_minijeu][2]
                    [numero_de_la_question]).replace(" ", ""))
            nb_rep_aleatoire = randint(1,4)
            if nb_rep_aleatoire == 1:
                changer_le_script(f"Super, c'est bien ça : ({str(questions_et_reponses[numero_de_minijeu][2][numero_de_la_question]).replace(' ','')}) !")
            elif nb_rep_aleatoire == 2:
                changer_le_script(f"Bien joué!  : {str(questions_et_reponses[numero_de_minijeu][2][numero_de_la_question]).replace(' ','')} est bien la bonne réponse !")
            elif nb_rep_aleatoire == 3:
                changer_le_script(f"Hoho, quelle satisfaction ! L'ordinateur a validé {str(questions_et_reponses[numero_de_minijeu][2][numero_de_la_question]).replace(' ','')} !")
            elif nb_rep_aleatoire == 4:
                changer_le_script(f"Vous avez réussi ! Votre réponse est correcte ({str(questions_et_reponses[numero_de_minijeu][2][numero_de_la_question]).replace(' ','')})")


            if numero_de_minijeu == 1:
                fenetre.after(3000, mini_jeu_conversions)
            elif numero_de_minijeu == 2:
                fenetre.after(3000, mini_jeu_couleurs)
            elif numero_de_minijeu == 3:
                fenetre.after(3000, mini_jeu_message_code)
            elif numero_de_minijeu == 4:
                # lier la fonction qui créée l'interface pour saisir le code (à faire)
                creer_interface_saisie_code()
        elif 3 - nb_de_tentatives == 0:
            rejouer_le_mini_jeu(numero_de_minijeu)
        else:
            if numero_de_minijeu == 2:
                global entry_text
                entry_text.set("")
            if numero_de_minijeu == 3:
                if level == 1:
                    entry_text.set(
                        "rgb(...)"
                    )  # réinitialise la case 'champ de texte' à chaque réponse fausse
                elif level == 2:
                    entry_text.set("#")

    # s'il ne reste plus de tentatives
    else:
        rejouer_le_mini_jeu(numero_de_minijeu)


#fonction complémentaire de verifier_reponses() qui permet d'éviter les répétitions
def rejouer_le_mini_jeu(numero_de_minijeu):
    detruire_interface()
    nb_aleatoire_phrase = randint(
        1, 3
    )  # permet de varier les phrases : en choisi une de manière aléatoire entre 3 phrases
    print("nb alea = ", nb_aleatoire_phrase)
    if nb_aleatoire_phrase == 1:
        phrase_perte = "Mince, ce n'est pas la bonne réponse... \nPeut être qu'un autre indice nous aidera à trouver la solution d'une autre manière!"
    elif nb_aleatoire_phrase == 2:
        phrase_perte = "Zut! On dirait que ce n'est pas ça... Il doit sûrement y avoir d'autres pistes !"
    elif nb_aleatoire_phrase == 3:
        phrase_perte = "Et... c'est peut-être ça ? Oh non... Ce n'est pas correct."
    changer_le_script(phrase_perte)
    if numero_de_minijeu == 1:
        fenetre.after(3000, mini_jeu_booleen)
    elif numero_de_minijeu == 2:
        fenetre.after(1000, mini_jeu_conversions)
    elif numero_de_minijeu == 3:
        fenetre.after(3000, mini_jeu_couleurs)
    elif numero_de_minijeu == 4:
        fenetre.after(3000, mini_jeu_message_code)


def verifier_le_code(entry_text):
    global code
    reponse_utilisateur = entry_text
    changer_le_script(
        "Il semble que nous ayons assez d'éléments pour rentrer le code dans l'ordinateur !"
    )
    if reponse_utilisateur.replace(" ", "").upper() == code.replace(";", "").replace(" ", "").upper():
        detruire_interface()
        changer_image_fond(repertoire_images_générales["fond_de_fin"])

        nb_fin_aleatoire = randint(1,2)
        if nb_fin_aleatoire == 1:
          changer_le_script("Bravo ! Nous avons réussi à trouver le code. La porte du bunker s'ouvre enfin! [bruit assourdissant de porte rouillée]")
          fenetre.after(5000, lambda: changer_le_script("Voyons voir ce qui se cache derrière cette porte ! "))
          fenetre.after(9000, lambda: changer_le_script("[Vous passez la porte et êtes ébloui(e) par la lumière vive du soleil]"))
          fenetre.after(14000, lambda: changer_le_script("Waouh ! Ce paysage est impressionnant !\nIl y a des arbres partout !\nOh ! là-bas ! Un animal inconnu mais magnifique vient de surgir! "))
          fenetre.after(21000, lambda: changer_le_script("Il ne semble y avoir aucune trace d'humain... \nPeut être qu'en marchant, j'en trouverais plus loin... [...]"))
        if nb_fin_aleatoire == 2:
          changer_le_script("Okay, donc, d'après l'ordinateur, j'ai rentré le bon code.\nMais rien ne se passe.. Allons voir la porte.\n Oh ! Mais...je ne l'ai même pas entendue s'ouvrir!")
          fenetre.after(5000, lambda: changer_le_script("Voyons voir ce qui se cache derrière cette porte ! "))
          fenetre.after(9000, lambda: changer_le_script("[Vous passez la porte mais ne voyez rien]\nTout est noir, Fait il nuit? Sommes nous encore dans le bunker ?\nLa Terre a-t-elle vraiment eut le temps de se réparer?"))
          fenetre.after(15000, lambda: changer_le_script("Tout est étrange. Vous commencez à appercevoir des formes sombres en mouvement, au loin.\n Il fait très froid, c'est effrayant."))
          fenetre.after(21000, lambda: changer_le_script("La Terre pourra-t-elle vraiment retrouver sa santé un jour ?\nSommes-nous condamnés pour l'éternité à rester dans ce bunker ? [...]"))
        if nb_fin_aleatoire == 3:
          changer_le_script("Ouïe! Mes oreilles! Quel est donc cet énorme bruit métallique ?\nOh ! Mais c'est le bon code !\nLa porte s'ouvre !")
          fenetre.after(5000, lambda: changer_le_script("Voyons voir ce qui se cache derrière cette porte ! "))
          fenetre.after(9000, lambda: changer_le_script("[Vous passez la porte et êtes attiré(e) par un bruit lointain]\nMais !: Qu'est-ce que c'est que cette blaque ?\n Is it a joke ?\nIl y a, en face de nous, une ville peuplée d'humains !"))
          fenetre.after(15000, lambda: changer_le_script("Il semble y avoir un marché sur la place. Comment est-ce possible qu'il y ait autant de survivants ? \n Depuis combien de temps sont-ils là ?"))
          fenetre.after(21000, lambda: changer_le_script("Vos parents vous auraient menti ? Il n'y aurait jamais eu de catastrophe ?\nNon! Ce n'est pas possible...)"))
        fenetre.after(
          28000, lambda: changer_le_script(
            "Nous espérons que ce jeu vous a plu ! Vous pouvez relancer le jeu pour trouver de nouvelles énigmes !")
            )
        fenetre.after(
            35000, lambda: changer_le_script(
                "Les développeurs, inventeurs et créateurs de Escape The Apocalypse vous remercient\nClara - Quentin - Louison"
            ))
        return True
    else:
        global entry_code_text
        entry_code_text.set("")
        changer_le_script("Code Faux")
        fenetre.after(
            2000, lambda: changer_le_script(
                "Entrez le code pour déverrouiller la porte fortifiée."))

#fonction des boutons suppr, 0 et 1 (mini_jeu_conversions)
def supprimer_dernier_caractere():
    global entry_text
    str = entry_text.get()
    str = str[0:len(str) - 1]
    if str[-1] == " ":
        str = str[0:len(str) - 1]
    entry_text.set(str)


# fonction qui ajoute le caractere a input ( au clic du bouton 0 ou 1, mini jeu conversions)
def ajouter_carcatere(caractere):
    global entry_text
    if len(entry_text.get().replace(" ", "")) % 4 == 0:
        str = entry_text.get() + " " + caractere
    else:
        str = entry_text.get() + caractere
    entry_text.set(str)













# PARTIE DE QUENTIN


# fonction qui créé un dictionnaire organisé comprenant toutes les questins, réponses et images du niveau sélectionné.
def create_level_dictionary(niveau_selectionne):
    global level
    level = niveau_selectionne
    if level == 1:
        menubar = Menu(fenetre)
        fenetre["menu"] = menubar
        """     
        sousMenu = Menu(menubar)
        menubar.add_cascade(label='Aide', menu=sousMenu)
        """
        sous_menu = Menu(menubar)
        menubar.add_cascade(label='Aide', menu=sous_menu)

        sous_menu.add_command(label='Expressions booléennes', command=lambda: webbrowser.open("https://apcpedagogie.com/les-booleens-en-python/"))
        sous_menu.add_command(label='Conversions entre bases de données', command=lambda: webbrowser.open("https://wims.univ-cotedazur.fr/wims/fr_tool~number~baseconv.fr.html"))
        sous_menu.add_command(label='Codes couleurs', command=lambda: webbrowser.open("https://www.dessinemoiunsite.com/mieux-comprendre-les-couleurs-hexadecimales/"))
        sous_menu.add_command(label='Encodage des caractères', command=lambda: webbrowser.open("https://geoma-sig.com/wp-content/uploads/2020/07/69.encodage-iso-1.png"))

        global questions_et_reponses  # cette variable est accessible partout

        questions_et_reponses_bool = {
            1: questions_bool_1,
            2: reponses_bool_1,
            3: images_bool_1
        }

        questions_et_reponses_conversion = {
            1: questions_conversion_1,
            2: reponses_conversion_1,
            3: images_conversions_1
        }
        questions_et_reponses_couleur = {
            1: questions_couleur_1,
            2: reponses_couleur_1,
            3: images_couleurs_1
        }
        questions_et_reponses_message_code = {
            1: questions_message_code_1,
            2: reponses_message_code_1,
            3: images_message_code_1
        }

        questions_et_reponses = {
            1: questions_et_reponses_bool,
            2: questions_et_reponses_conversion,
            3: questions_et_reponses_couleur,
            4: questions_et_reponses_message_code
        }
        print(questions_et_reponses)
        lancer_mini_jeux(0)
    elif level == 2:
        questions_et_reponses_bool = {
            1: questions_bool_2,
            2: reponses_bool_2,
            3: images_bool_2
        }
        questions_et_reponses_conversion = {
            1: questions_conversion_2,
            2: reponses_conversion_2,
            3: images_conversions_2
        }
        questions_et_reponses_couleur = {
            1: questions_couleur_2,
            2: reponses_couleur_2,
            3: images_couleurs_2
        }
        questions_et_reponses_message_code = {
            1: questions_message_code_2,
            2: reponses_message_code_2,
            3: images_message_code_2
        }

        questions_et_reponses = {
            1: questions_et_reponses_bool,
            2: questions_et_reponses_conversion,
            3: questions_et_reponses_couleur,
            4: questions_et_reponses_message_code
        }
        print(questions_et_reponses)
        lancer_mini_jeux(0)
    else:
        #indique la localisation de l'erreur si elle survient
        error("create_level_dictionnary()",
              "Le niveau sélectionné est " + str(level) + ".")
        return False


"""
DETAILS DU DICTIONNAIRE :

questions_et_reponses[1][1][1] — — — — — — numéro de la question/réponse/image que l'on souhaite obtenir
  |                   |  |                                        
  |                   |  |
  |                   |  |
nom du dict.          |  |
                      |  |
                      |  |
                      |  type de requete:
                      |   [1] : questions du mini-jeu demandé
                      |   [2] : réponses du mini-jeu demandé
                      |   [3] : images du mini-jeu demandé
                      |
                      |
                      |
                      numéro du mini-jeu : 
                      [1] : Mini jeu Booleen
                      [2] : Mini-jeu Conversions
                      [3] : Mini-jeu Couleurs
                      [4] : Mini-jeu message codé


exemple : 

questions_et_reponses[2][1][2]
--> Permet d'obtenir la question n°2 du mini jeu Conversions

"""
#fonction qui ajoute une suite de caracteres à la variable qui stocke le code
def ajouter_au_code(caracteres_a_ajouter):
    global code
    if len(code) >= 1:  # si le code a déjà une valeur,
        code = code + ";" + str(
            caracteres_a_ajouter
        )  #ajouter la nouvelle valeur a l'ancienne. le point virgule permet de retrouver le co de trouvé a chaque mini jeu
    else:
        code = str(caracteres_a_ajouter)

# fonction qui demande le niveau souhaité à l'utilisateur
def ask_for_level():
    #supprimme le script
    changer_le_script("")
    #supprimme l'affichage précédent
    detruire_interface()
    creer_interface()
    #creer un bouton pour le niveau 2 qui lance la fonction create_level_dictionnary() pour le niveau 2
    btn_select_level_2 = Button(interface_enigmes,
                                text="Niveau 2",
                                background="#2f3640",
                                activebackground="#212a33",
                                bd=0,
                                font="Sylfaen 20",
                                fg="#f4af03",
                                activeforeground="#f4af03",
                                highlightcolor="blue",
                                cursor="hand2",
                                command=lambda: create_level_dictionary(2))
    # empaqueter le bouton (le relier à la fenetre et l'afficher)
    btn_select_level_2.pack(side=BOTTOM, padx=20, pady=10, ipadx=10, ipady=2)
    
    #creer un bouton pour le niveau 1 qui lance la fonction create_level_dictionnary() pour le niveau 1
    btn_select_level_1 = Button(interface_enigmes,
                                text="Niveau 1",
                                background="#2f3640",
                                activebackground="#212a33",
                                bd=0,
                                font="Sylfaen 20",
                                fg="#f4af03",
                                activeforeground="#f4af03",
                                highlightcolor="blue",
                                cursor="hand2",
                                command=lambda: create_level_dictionary(1))
    # empaqueter le bouton (le relier à la fenetre et l'afficher)
    btn_select_level_1.pack(side=BOTTOM, padx=20, pady=10, ipadx=10, ipady=2)
    # Détaille les différents niveaux dans le script
    changer_le_script(
        "Niveau 1 : Easy, Si vous n'avez jamais programmé ou entendu parlé de bases de données, ce niveau est fait pour vous!\nNiveau 2: Nécessite des compétences en codage des nombres et en python basiques"
    )

#fonction principale de l'interface graphique. EN cours de développement
def lancer_mini_jeux(arg):
    detruire_interface()
    afficher_contexte_histoire()

# créé le texte qui indique le nombre de tentatives restantes
def creer_label_tentatives_restantes():
    global nombre_de_tentatives
    global interface_enigmes
    global label_tentatives_restantes
    global text_tentatives_restantes
    text_tentatives_restantes = StringVar()
    text_tentatives_restantes.set(
        f"Tentatives restantes : {3-nombre_de_tentatives}")
    label_tentatives_restantes = Label(
        interface_enigmes,
        textvariable=text_tentatives_restantes).pack(side=BOTTOM)

#met à jour le nombre de tentatives restantes sur l'interface graphique
def update_label_tentatives_restantes():
    global nombre_de_tentatives
    global interface_enigmes
    global label_tentatives_restantes
    global text_tentatives_restantes
    text_tentatives_restantes.set(
        f"Tentatives restantes : {3-nombre_de_tentatives}")

# fonction qui ajouter 1 au nombre de tentatives a chaque exécution et qui renvoie ce nombre
def ajouter_une_tentative():
    global nombre_de_tentatives
    nombre_de_tentatives = nombre_de_tentatives + 1
    global label_tentatives_restantes
    update_label_tentatives_restantes(
    )  #met à jour le label nombre de tentatives
    return nombre_de_tentatives

# fonction qui affiche l'histoire du jeu
def afficher_contexte_histoire():
  #dictionnaire qui contient toute l'histoire découpée en morceaux lisibles en 5 secondes.
    histoire = ["En 2521, une effroyable apocalypse toucha la Terre détruisant toute trace de vie à sa surface. ",
              "Mais, deux chercheurs (Mme Angela John et Michel Jack) se sont réfugiés dans un bunker souterrain ultra-protégé. ",
              "Malgré les difficultés qu’ils ont rencontrées, ils parvinrent à survivre et vous ont donné la vie.",
              "Vous vous réveillez en l’an 2550 sur la planète Terre. ",
              "Vous avez alors 17 ans et vous retrouvez dans ce bunker. ",
              "En consultant les ordinateurs qui analysent l’Etat de la Terre, vous constatez que celle-ci est à nouveau viable.",
              "Mais, vous ne pouvez sortir à l’extérieur car un code étrange vous est demandé pour ouvrir la porte.",
              "Sauriez-vous trouver le code et sortir du bunker ?\n[Notre p'tite astuce : Retenez bien vos réponses !😉]"]
#change le script toutes les 5 sceondes
    changer_le_script(histoire[0])
    fenetre.after(10000,lambda: changer_le_script(histoire[1]))
    fenetre.after(15000,lambda: changer_le_script(histoire[2]))
    fenetre.after(20000,lambda: changer_le_script(histoire[3]))
    fenetre.after(25000,lambda: changer_le_script(histoire[4]))
    fenetre.after(30000,lambda: changer_le_script(histoire[5]))
    fenetre.after(35000,lambda: changer_le_script(histoire[6]))
    fenetre.after(35000,lambda: changer_le_script(histoire[7]))

    fenetre.after(9*5000,lambda:mini_jeu_booleen())















# PARTIE DE LOUISON

# fonction qui signale une erreur et la localise
def error(nom_de_la_fonction, details_du_probleme):
    os.system("clear")
    print(f"Une erreur s'est produite dans la fonction {nom_de_la_fonction}.")
    if details_du_probleme:
        print("Détails : " + details_du_probleme)
    changer_le_script(
        f"Une erreur s'est produite dans la fonction {nom_de_la_fonction}.")
    showerror(
        "Une erreur s'est produite",
        f"Une erreur s'est produite dans la fonction {nom_de_la_fonction} . {details_du_probleme} ",
        default="ok")



# fonction qui créé l'interface graphiques (boutons, zones de textes...) du mini jeu conversions
def creer_interface_minijeux(numero_de_minijeu, numero_de_question):
    global nombre_de_tentatives
    nombre_de_tentatives = 0
    global level
    print("nom image : ",
          questions_et_reponses[numero_de_minijeu][3][numero_de_question])
    changer_image_fond(
        questions_et_reponses[numero_de_minijeu][3][numero_de_question])
    changer_le_script(
        questions_et_reponses[numero_de_minijeu][1][numero_de_question])
    creer_interface()  # créé la frame "interface_enigmes"
    creer_label_tentatives_restantes()
    if numero_de_minijeu == 1:  #si le jeu est "tests booléens"
        # Bouton "False"
        global bouton_false
        bouton_false = Button(interface_enigmes,
                              text="False",
                              background="#2f3640",
                              activebackground="#212a33",
                              bd=0,
                              font="Sylfaen 20",
                              fg="#f4af03",
                              activeforeground="#f4af03",
                              highlightcolor="blue",
                              cursor="hand2",
                              command=lambda: verifier_reponses(
                                  1, numero_de_question, level, False),
                              width=5)
        bouton_false.pack(anchor=SE,
                          padx=20,
                          pady=10,
                          ipadx=10,
                          ipady=2,
                          expand=YES)
        # Bouton "True"
        bouton_true = Button(interface_enigmes,
                             text="True",
                             background="#2f3640",
                             activebackground="#212a33",
                             bd=0,
                             font="Sylfaen 20",
                             fg="#f4af03",
                             activeforeground="#f4af03",
                             highlightcolor="blue",
                             cursor="hand2",
                             command=lambda: verifier_reponses(
                                 1, numero_de_question, level, True),
                             width=5)
        bouton_true.pack(anchor=SE, padx=20, pady=10, ipadx=10, ipady=2)

        #Créé une interface avce une zone d'entrée de texte et un bouton de validation
    elif (numero_de_minijeu == 4) or (numero_de_minijeu == 3) or (
        (numero_de_minijeu == 2) and (level == 1) and
        (numero_de_question in [2, 3, 4])) or ((numero_de_minijeu == 2) and
                                               (level == 2) and
                                               (numero_de_question in [1, 3])):
        global entry_text
        entry_text = StringVar()
        if (numero_de_minijeu == 3) and (level == 1):
            entry_text.set(
                "rgb(...)")  # indique le format rgb() pour la réponse
        if (numero_de_minijeu == 3) and (level == 2):
            entry_text.set("#")  # indique le format de la réponse

        champ_de_texte = Entry(interface_enigmes,
                               textvariable=entry_text,
                               width=15,
                               font="Sylfaen 20",
                               fg="#f4af03",
                               bd=0,
                               background="#2f3640",
                               insertbackground="#f4af03",
                               justify="center").pack(anchor=SE,
                                                      expand=YES,
                                                      padx=20,
                                                      pady=10,
                                                      ipadx=10,
                                                      ipady=2)
        bouton_validation = Button(interface_enigmes,
                                   text="Valider",
                                   background="#2f3640",
                                   activebackground="#212a33",
                                   bd=0,
                                   font="Sylfaen 20",
                                   fg="#f4af03",
                                   activeforeground="#f4af03",
                                   highlightcolor="blue",
                                   cursor="hand2",
                                   width=14,
                                   command=lambda: verifier_reponses(
                                       numero_de_minijeu, numero_de_question,
                                       level, entry_text.get())).pack(
                                           anchor=SE,
                                           padx=20,
                                           pady=10,
                                           ipadx=10,
                                           ipady=2,
                                           expand=NO)
    elif (numero_de_minijeu == 2) and (((level == 1) and
                                        (numero_de_question == 1)) or
                                       ((level == 2) and
                                        (numero_de_question == 2))):
        entry_text = StringVar()
        bouton_validation = Button(interface_enigmes,
                                   text="Valider",
                                   background="#2f3640",
                                   activebackground="#212a33",
                                   bd=0,
                                   font="Sylfaen 20",
                                   fg="#f4af03",
                                   activeforeground="#f4af03",
                                   highlightcolor="blue",
                                   cursor="hand2",
                                   width=14,
                                   command=lambda: verifier_reponses(
                                       numero_de_minijeu, numero_de_question,
                                       level, entry_text.get())).pack(
                                           side=BOTTOM,
                                           padx=20,
                                           pady=10,
                                           ipadx=10,
                                           ipady=2,
                                           expand=NO)
        champ_de_texte = Entry(interface_enigmes,
                               textvariable=entry_text,
                               width=15,
                               font="Sylfaen 20",
                               disabledforeground="#f4af03",
                               bd=0,
                               disabledbackground="#2f3640",
                               insertbackground="#f4af03",
                               justify="center",
                               state="disabled").pack(side=BOTTOM,
                                                      expand=NO,
                                                      padx=20,
                                                      pady=10,
                                                      ipadx=10,
                                                      ipady=2)
        bouton_suppression = Button(interface_enigmes,
                                    text="Suppr.",
                                    background="#2f3640",
                                    activebackground="#212a33",
                                    bd=0,
                                    font="Sylfaen 20",
                                    fg="#f4af03",
                                    activeforeground="#f4af03",
                                    highlightcolor="blue",
                                    cursor="hand2",
                                    width=6,
                                    command=supprimer_dernier_caractere).pack(
                                        anchor=SE,
                                        padx=20,
                                        pady=10,
                                        ipadx=10,
                                        ipady=2,
                                        expand=NO)
        bouton_ajout_zero = Button(
            interface_enigmes,
            text="0",
            background="#2f3640",
            activebackground="#212a33",
            bd=0,
            font="Sylfaen 20",
            fg="#f4af03",
            activeforeground="#f4af03",
            highlightcolor="blue",
            cursor="hand2",
            width=6,
            command=lambda: ajouter_carcatere("0")).pack(anchor=SE,
                                                         padx=20,
                                                         pady=10,
                                                         ipadx=10,
                                                         ipady=2,
                                                         expand=NO)
        bouton_ajout_un = Button(interface_enigmes,
                                 text="1",
                                 background="#2f3640",
                                 activebackground="#212a33",
                                 bd=0,
                                 font="Sylfaen 20",
                                 fg="#f4af03",
                                 activeforeground="#f4af03",
                                 highlightcolor="blue",
                                 cursor="hand2",
                                 width=6,
                                 command=lambda: ajouter_carcatere("1")).pack(
                                     anchor=SE,
                                     padx=20,
                                     pady=10,
                                     ipadx=10,
                                     ipady=2,
                                     expand=NO)


# affiche la zone de texte pour rentrer le code
def creer_interface_saisie_code():
    detruire_interface()
    creer_interface()
    changer_image_fond(repertoire_images_générales["fond_code_secret"])
    global interface_enigmes
    global entry_code_text
    entry_code_text = StringVar()
    description_texte = Label(interface_enigmes,
                              text="Entrez le code pour dévérouiller la porte",
                              font="Sylfaen 20").pack(pady=60)
    champ_texte_code = Entry(interface_enigmes,
                             textvariable=entry_code_text,
                             width=30,
                             font="Sylfaen 35",
                             fg="#f4af03",
                             bd=0,
                             background="#2f3640",
                             insertbackground="#f4af03",
                             justify="center")
    champ_texte_code.pack(expand=YES, ipady=20, ipadx=20)
    bouton_validation = Button(
        interface_enigmes,
        text="Valider",
        background="#2f3640",
        activebackground="#212a33",
        bd=0,
        font="Sylfaen 20",
        fg="#f4af03",
        activeforeground="#f4af03",
        highlightcolor="blue",
        cursor="hand2",
        width=14,
        command=lambda: verifier_le_code(entry_code_text.get())).pack(
            anchor=CENTER, padx=20, pady=10, ipadx=10, ipady=2, expand=NO)


#permet de  supprimer l'image de fond, à utiliser le moins possible
def supprimer_image_fond():
    canvas_arriere_plan.delete(fenetre, image_fond)


# permet de changer l'arrière plan en applicant l'image sélectionnée.
def changer_image_fond(img):  #L'argument fourni doit être de type PhotoImage
    canvas_arriere_plan.itemconfig(image_fond, image=img)

# fonction pour mettre à jour le script sans avoir à le remettre en forme à chaque fois
def changer_le_script(texte_a_ecrire):
    if "script" in globals(
    ):  # si un script existe déja dans les variables globales, alors le supprimer
        global script
        script.destroy()
    script = Label(script_box,
                   text=texte_a_ecrire,
                   height=3,
                   font=("Sylfaen", 12),
                   fg="black",
                   justify="left")
    script.pack(fill=BOTH, ipady=5)


# PAGE INTERFACE
def creer_interface():
    global interface_enigmes
    interface_enigmes = Frame(scene_box, height=600, width=1100,
                              bg="")  # déclare le widget (Frame)
    interface_enigmes.pack(anchor=NW, expand=YES, fill=BOTH)


# supprime l'interface sans toucher au script et à l'arrière plan
def detruire_interface():
    interface_enigmes.destroy()



# INTERFACE GRAPHIQUE

# nom de la fenetre
fenetre.title("Escape The Apocalypse")

# autres caractéristiques de la fenetre
fenetre.configure(background="black")

# taille minimale fenetre
fenetre.geometry("1100x682")
fenetre.resizable(0, 0)

# logo de la fenetre
fenetre.iconbitmap("logo.ico")
"""
l'icone ne fonctionne pas sur repl
"""

#image implémentation
# gestion de l'arrière plan



canvas_arriere_plan = Canvas(
    fenetre, bg="black", width=1100, height=600
)  # enlever la couleur pour uniformiser les couleurs entre script et bords colorés éventuels
canvas_arriere_plan.place(x=0, y=0)
image_fond = canvas_arriere_plan.create_image(1100 / 2, 600 / 2, image=repertoire_images_générales["fond"])
frame_canvas = canvas_arriere_plan.create_window(0, 0)
changer_image_fond(repertoire_images_générales["fond"])


# boites de la fenetre
scene_box = Frame(fenetre, bg="white").pack(side=TOP, expand=NO, fill=BOTH)

script_box = Frame(fenetre)
script_box.pack(side=BOTTOM, expand=NO, fill=BOTH)
script_box.configure(bg="")


creer_interface()


# destroy_button = Button(interface_enigmes, text="destroy(self)", command=detruire_interface).pack(expand=YES)  # test
bouton_lancer_jeu = Button(interface_enigmes,
                           text="Lancer le jeu !",
                           background="#2f3640",
                           activebackground="#212a33",
                           bd=0,
                           font="Sylfaen 20",
                           fg="#f4af03",
                           activeforeground="#f4af03",
                           highlightcolor="blue",
                           cursor="hand2",
                           command=ask_for_level).pack(side=BOTTOM,
                                                       pady=20,
                                                       ipadx=10)

# développeurs du jeu dans le script
changer_le_script("Bienvenue dans Escape The Apocalypse")
fenetre.mainloop()
