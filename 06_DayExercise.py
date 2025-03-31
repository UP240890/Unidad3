# Exercises: Level 1#
#exercise1#
lista = tuple()
#exercise2#
hermanos= ("Jose", "Karol")
hermanas= ("Juana", "Ana")
#exercise3#
sibling = hermanos + hermanas
print(sibling)
#exercise4#
print(f"I have {len(sibling)} siblings")
#exercise5#
family_members = sibling + ("Jose de Jesus","Rita")
print(family_members)
# Exercises: Level 2#
frutas = ("Mango", "Platano", "Uvas")
vege = ("Zanahoria", "Cebollines", "Papas")
animal_product = ("Tocinos", "Huevos", "Mantequilla")

food_stuff_tp = frutas + vege + animal_product
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

mid = int(len(food_stuff_tp)/2)
food_stuff_tp = food_stuff_tp[:mid]
print(food_stuff_tp)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)