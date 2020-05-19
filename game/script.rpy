define b =  Character("Bob", color="FF3333")
define n =  Character("Nokio", color="00FF1A")
define hero = Character("[Nhero]")

label start:
<<<<<<< HEAD
    "salut bonjour"
=======
    "salut"
>>>>>>> c17da0f6de05b5384bef0e778f69dacdd79a135e
    "Il etait une fois dans un monde les skin fortine existe..."
    "Au debut personne etait au courant du plan des skin"
    "Mais le pire est venue et le monde c'est fait laver des humain"
    "Maintenant il y a plus que des skins fortnite!!!"

    scene sky
    show icon
    with dissolve
    b "Bonjour voyageur qu'elle skin est tu???"
    b "Merci beaucoup de me repondre"

    $ AimeFortnite = False
    $ Vbucks = 0
    $ Nhero = renpy.input("Entrez votre nom")

    menu:
        b "Est-ce que tu aime Fortnite"
        "Oh oui !":
            $ AimeFortnite = True
            b "Super alors on peut continuer"
        "Mouaiii, non !":
            b "Moi non plus mais je suis obliger par des gens"
            jump annif_de_truc

label annif_de_truc:
    scene black
    with dissolve
    show icon

    b "Bonne annif"

    if AimeFortnite == True:
        b "comme tu aime Fortnite je te donne des 990 V-bucks !!!"
        $ Vbucks += 990
    else:
        b "comme Fortnite c'est pas trop ton truc je te donne une carte google play de valeur de 50$ !!!"
