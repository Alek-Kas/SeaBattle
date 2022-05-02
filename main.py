#  Основной код
from dot import Dot
from messages import Greeting, Clr_Scr
from ship import Ship

print(Greeting())
print(Clr_Scr())
ship_1 = Ship(3, 1, Dot(2, 2))
ship_2 = Ship(2, 0, Dot(3, 4))
ship_3 = Ship(1, 1, Dot(0, 0))

print(ship_1.dots)
print(ship_2.dots)
print(ship_3.dots)

print(ship_1.hitten(Dot(0, 3)))
