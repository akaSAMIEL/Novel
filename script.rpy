# Начало игры

label start:

    scene bg class with dissolve

    show mc normal at left2
    with dissolve

    "Главный герой обрисовывает обстановку."
# Ввод имени
    $ mcname = renpy.input("Ваше имя:", length=18, default="Антон", allow="йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ").strip()
    
    if mcname == "":
        $ mcname = "Антон"

    "По пути [mcname] засыпает и видит сон с Евой."
    
    "[mcname] прибывает на первую пару и выбирает к кому сесть."
    
    menu:
        "К кому сесть?"
        
        "Староста в первом ряду":
            jump alexander
        "Знакомый сосед по комнате":
            jump timur
        "Дружелюбная однокурсница":
            jump jenya_cp1
