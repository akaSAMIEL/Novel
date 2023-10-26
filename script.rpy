# Начало игры

label start:

    scene bg class with dissolve

    show mc normal at left2
    with dissolve

    "Главный герой обрисовывает обстановку."

    "По пути он засыпает и видит сон с Евой."
    
    "Он прибывает на первую пару и выбирает к кому сесть."
    
    menu:
        "К кому сесть?"
        
        "Староста в первом ряду":
            jump alexander
        "Знакомый сосед по комнате":
            jump timur
        "Дружелюбная однокурсница":
            jump jenya
