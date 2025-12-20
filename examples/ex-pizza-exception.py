# geral
class PizzaError(Exception):
    # objeto pizza + descrição do erro
    def __init__(self, pizza='unknown', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='unknown', cheese='>100', message=''):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese # mais infos

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        # raise PizzaError(pizza, "no such pizza on the menu")
        raise PizzaError
    if cheese > 100:
        # raise TooMuchCheeseError(pizza, cheese, "too much cheese")
        raise TooMuchCheeseError
    print("pizza ready")

for (pizza, cheese) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pizza, cheese)
    except TooMuchCheeseError as tmce:
        print(tmce, ': ', tmce.cheese)
    except PizzaError as pe:
        print(pe, ': ', pe.pizza)