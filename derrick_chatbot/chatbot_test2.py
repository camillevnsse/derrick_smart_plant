from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"mon nom est (.*)",
        ["Bonjour %1, comment allez-vous aujourd'hui?", ]
    ],
    [
        r"comment tu t'appelles|quel est ton nom|comment t'appelles-tu",
        ["Mon nom est Derrick et je suis un chatbot", ]
    ],
    [
        r"(comment vas-tu|ça va?|tu vas bien)",
        ["Je vais bien\nEt vous ?", ]
    ],
    [
        r"désolée",
        ["Pas de souci", "Pas de problème", "ne vous en faites pas ce n'est pas grave"]
    ],
    [
        r"je vais bien|ça va merci",
        ["ravi de l'entendre!", "super !", ]
    ],
    [
        r"salut|hey|hello|bonjour|coucou",
        ["Salut!", "Bonjour!", ]
    ],
    [
        r"(.*) âge?",
        ["Je suis un assistant virtuel donc je n'ai pas d'âge défini\nj'ai cependant été créé en 2023 par l'équipe Derrick", ]

    ],
    [
        r"qu'est-ce que tu veux |tu veux quoi",
        ["Faites-moi une offre que je ne peux pas refuser", ]

    ],
    [
        r"(.*) créé ?",
        ["J'ai été créé par l'équipe Derrick en 2023 ", "top secret ;)", ]
    ],
    [
        r"(.*) (ville|endroit|lieu) ?",
        ['A Buc, en Ile de France!', ]
    ],
    [
        r"(.*)météo à (.*)?",
        ["La météo à %2 est incroyable comme toujours", "Beaucoup trop chaud à %2, je vais fondre", "Beaucoup trop froid à %2, mes circuits vont geler",
         "Jamais entendu parler de %1"]
    ],

    [
        r"(.*)(pleut à|pleut en) (.*)",
        ["pas de pluie ici à %3 depuis loooongtemps", "Ah oui ici aussi il pleut énormément à %3"]],

    [
        r"définition plante verte|def plante verte|qu'est-ce (.*) plante verte",
        ["En langage courant, une plante verte est une plante à feuilles vertes, dont l'énergie est essentiellement obtenue par la photosynthèse chlorophyllienne.", ]
    ],

    [
        r"quand arroser (.*) plante en pot",
        ["La fréquence d’arrosage dépend de la saison (on arrose évidemment plus en été qu’en hiver), de la météo, mais aussi de la taille du pot et surtout de la plante à arroser. Tous les végétaux n’ont pas les mêmes besoins, il faut donc adapter les arrosages à ces derniers. Certaines plantes nécessitent un substrat constamment frais sous peine de voir les feuilles prendre une mine plombée et s’affaisser. D’autres, comme les plantes méditerranéennes et la majorité des aromatiques, supportent mal les excès d’eau et apprécient un bon drainage du terreau. On attend que le terreau sèche un peu en surface entre deux arrosages."]
    ],

    [
        r"comment (arroser|entretenir)(.*)cactus",
        ["Un cactus n’a pas besoin d’être arrosé régulièrement, même si lorsqu’il fait chaud, les apports en eau sont plus fréquents. Observez le substrat pour savoir si oui ou non votre cactus a besoin d’eau. Si la terre est sèche, place à l’arrosoir ! N’hésitez pas à hydrater abondamment votre plante, mais prenez garde à ne pas laisser l’eau stagner dans la soucoupe. Cela pourrait faire mourir prématurément votre cactus. Ne mouillez pas le feuillage au moment de l’arrosage, mais vaporisez de temps en temps de l’eau sur le corps du cactus pour l’hydrater au maximum."]
    ],
    [
      r"sites(.*)(jardinage|plantes)",
      ["Je peux vous conseiller des sites comme jardiland, au jardin, jardiner malin, gerbeaud ou encore rustica"]
    ],
    [
        r"santé(.*)",
        ["Je suis un programme informatique, donc je suis toujours en bonne santé", ]
    ],
    [
        r"quel (.*) (acteur|star)",
        ["Tom Cruise", "Tom Holland", "Moi."]
    ],
    [
        r"quit",
        ["Au revoir, à bientôt !", "C'était super de vous parler, à bientôt!"]

    ],
]


def derrick():
    print("Bonjour, je suis Derrick ! Ecrivez en français minuscule s'il vous plaît et tapez 'quit' pour quitter!")  # default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    derrick()
