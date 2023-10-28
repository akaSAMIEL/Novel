# Персонажи

define mc = Character('[mcname]', color="#000000", image='mc')
define j = Character('Женя', color="#000000", image='jenya')
define t = Character('Тимур', color="#000000")
define a = Character('Александр Сергеевич', color="#000000")
define e = Character('Ева', color="#000000")
define g = Character('Призрак', color="#000000")

# Переменные

init:
    $ right2 = Position (xalign=0.8, yalign=1.1)
    $ left2 = Position (xalign=0.2, yalign=1.1)
    
default maxrelate = 60
default minrelate = 0

default relate_jenya = 30
default relate_timur = 30
default relate_alex = 30
default relate_eve = 30


#with moveoutleft\right
#with moveinleft\right
#with easeinleft
#with blinds
#with wipeleft
#with pushleft