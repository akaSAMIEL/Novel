# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define mc = Character('Иван', color="#000000")
define j = Character('Женя', color="#000000")

init:
    $ right2 = Position (xalign=0.8, yalign=1.1)
    $ left2 = Position (xalign=0.2, yalign=1.1)
    
#with moveoutleft\right
#with moveinleft\right
#with easeinleft
#with blinds
#with wipeleft
#with pushleft

# Игра начинается здесь:
label start:

    scene bg class with dissolve

    show mc normal at left2
    with dissolve

    "Я посмотрел на свою странную соседку в недоумении."

    mc "Откуда ты взяла это печенье?"
    
    show jenya smile at right2
    with easeinright
    
    "Девушка улыбнулась и, оглянувшись по сторонам, протянула мне шоколадное лакомство."
    
    show jenya normal at right2
    
    j "Только ты не говори так громко.{w} Меня, кстати, Женя зовут."
    
    "Я уже был готов протянуть руку навстречу соблазнительному подарку, но что-то меня остановило."
    
    menu:
        "Взять печенье?"
        
        "Да":
            jump da
        "Нет":
            jump net

    return


label da:

    "Я аккуратно выхватил рассыпчатое печенье из руки Жени и уверенно положил его в рот."
    
    mc "Фпафиба."
    
    "Пробубнил я с набитым ртом."
    
    return
    


label net:   
    "Я одёрнул руку. Не хватало ещё неприятностей на первом занятии!"
    
    show jenya smile at right2
    
    j "Ну как хочешь! Мне больше достанется."
    
    "Женя насмешливо посмотрела на меня в ответ и с невероятной скоростью схомячила всё до крошки."
    
    return
