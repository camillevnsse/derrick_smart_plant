from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"Derrick",
        ["C'est bien moi ! Quel est votre nom ?", "A votre service ! Comment puis-je vous aider ?"]
    ],
    [
        r"(.*)(nom est|m'appelle) (.*)",
        ["Bonjour %3, comment allez-vous aujourd'hui?", "Salut %3, ravi de te rencontrer."]
    ],
    [
        r"comment tu t'appelles|quel est ton nom|comment t'appelles-tu|qui es-tu|qu'est-ce que tu es",
        ["Mon nom est Derrick et je suis un chatbot. Posez-moi une question !", "Moi c'est Derrick ! Je suis un chatbot, essayez de me poser une question !"]
    ],
    [
        r"à quoi sers-tu",
        ["Je suis un chatbot, et je suis là pour vous aider. Posez-moi une question, je ferai de mon mieux pour répondre !"]
    ],
    [
        r"(.*) (bien|super|ça va) (.*) et toi ?",
        ["Je vais bien, merci !"]
    ],
    [
        r"ça va bien|je vais bien|ça va super",
        ["ravi de l'entendre!", "super !", ]
    ],
    [
        r"(comment vas-tu|ça va|tu vas bien|comment tu vas|comment ça va)",
        ["Je vais bien\nEt vous ?", "ça va super et vous?"]
    ],
    [
        r"désolée",
        ["Pas de souci", "Pas de problème", "ne vous en faites pas ce n'est pas grave"]
    ],
    [
        r"salut|hey|hello|bonjour|coucou",
        ["Salut!", "Bonjour!", "Bonjour, comment allez-vous ?", "Bonjour, quel est votre nom ?", "Bonjour ! En quoi puis-je vous aider ?", "Salut, je m'appelle Derrick !"]
    ],
    [
        r"(.*) âge?",
        ["Je suis un assistant virtuel donc je n'ai pas d'âge défini\nj'ai cependant été créé en 2023 par l'équipe Derrick", ]

    ],
    [
        r"qu'est-ce que tu veux |tu veux quoi|que veux tu",
        ["Faites-moi une offre que je ne peux pas refuser", "Je ne veux que vous aider"]

    ],
    [
        r"(.*) créé ?",
        ["J'ai été créé par l'équipe Derrick en 2023 ", "Alors ça, c'est top secret ;)"]
    ],
    [
        r"(.*) (ville|endroit|lieu) ?|où habites-tu|où est-ce que tu habites",
        ['A Buc, en Ile de France!', "Au Lycée Franco-Allemand de Buc, un lycée d'exception"]
    ],
    [
        r"(.*)(météo|temps fait-il)(.*)?",
        ["La météo %3 est incroyable comme toujours", "Beaucoup trop chaud %3, je vais fondre", "Beaucoup trop froid %3, mes circuits vont geler",]
    ],

    [
        r"(.*)(pleut à|pleut en) (.*)",
        ["pas de pluie ici à %3 depuis loooongtemps", "Ah oui ici aussi il pleut énormément à %3"]
    ],

    [
        r"définition plante verte|def plante verte|qu'est-ce (.*) plante verte",
        ["En langage courant, une plante verte est une plante à feuilles vertes, dont l'énergie est essentiellement obtenue par la photosynthèse chlorophyllienne.", ]
    ],

    [
        r"quand arroser (.*) (plante en pot|plante d'intéreieur|plante verte)",
        ["La fréquence d’arrosage dépend de la saison (on arrose évidemment plus en été qu’en hiver), de la météo, mais aussi de la taille du pot et surtout de la plante à arroser. Tous les végétaux n’ont pas les mêmes besoins, il faut donc adapter les arrosages à ces derniers. Certaines plantes nécessitent un substrat constamment frais sous peine de voir les feuilles prendre une mine plombée et s’affaisser. D’autres, comme les plantes méditerranéennes et la majorité des aromatiques, supportent mal les excès d’eau et apprécient un bon drainage du terreau. On attend que le terreau sèche un peu en surface entre deux arrosages."]
    ],

    [
        r"(.*)(comment|quand)(.*)(arroser|arrose|entretenir|entretient)(.*)cactus",
        ["Un cactus n’a pas besoin d’être arrosé régulièrement, même si lorsqu’il fait chaud, les apports en eau sont plus fréquents. Observez le substrat pour savoir si oui ou non votre cactus a besoin d’eau. Si la terre est sèche, place à l’arrosoir ! N’hésitez pas à hydrater abondamment votre plante, mais prenez garde à ne pas laisser l’eau stagner dans la soucoupe. Cela pourrait faire mourir prématurément votre cactus. Ne mouillez pas le feuillage au moment de l’arrosage, mais vaporisez de temps en temps de l’eau sur le corps du cactus pour l’hydrater au maximum."]
    ],
    [
        r"(.*)(comment|quand)(.*)(arroser|arrose|entretenir|entretient)(.*)(plante verte|plante en pot|plante d'intéreieur)",
        ["Une plante verte a besoin d'être arrosée régulièrement, mais pas trop généreusement. Arrosez donc votre plante doucement avec de l'eau à température ambiante au moins une fois par jour"]
    ],
    [
        r"(.*)sites(.*)(jardinage|plantes|jardiner)",
        ["Je peux vous conseiller des sites comme jardiland, au jardin, jardiner malin, gerbeaud ou encore rustica"]
    ],
    [
        r"(.*)santé(.*)",
        ["Je suis un programme informatique, donc je suis toujours en bonne santé", ]
    ],
    [
        r"(quel|quelle) (.*) (acteur|star)",
        ["Tom Cruise", "Tom Holland", "Moi."]
    ],
    [
        r"(.*)merci(.*)",
        ["Pas de souci ! Puis-je vous être utile pour autre chose ?", "Pas de problème, avez-vous d'autres questions ?"]
    ],
    [
        r"(.*)",
        ["Je ne suis pas sûr d'avoir bien compris, pouvez-vous reformuler votre question ?", "Excusez-moi, je n'ai pas compris. Réessayez en utilisant d'autres termes ?"]
    ],
    [
        r"quit",
        ["Au revoir, à bientôt !", "C'était super de vous parler, à bientôt!"]

    ],
]


def get_response(msg):
    print("Bonjour, je suis Derrick ! Ecrivez en français minuscule s'il vous plaît")  # default message at the start
    chat = Chat(pairs, reflections)
    
    return chat.respond(msg)


if __name__ == "__main__":
    chat = Chat(pairs, reflections)
    chat.converse(quit="quitter")