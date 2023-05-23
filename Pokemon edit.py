from random import randint
import time

"""class Element:
    def __init__(self, elemental_type: str):
        self.elemental_type = elemental_type"""


def print_slow(string):
    for letter in string:
        print(letter, end='')
        time.sleep(0.009)
    print("\n")


class Pokemon:
    def __init__(self, name: str, health_points: int, moves: [(str, int)]):
        self.name = name
        self.hp = health_points
        self.moves = moves


class Battlefield:
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon, automan: str):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.automan = automan
        self.turn = 0

    def attack(self, pokemonA: Pokemon, pokemonB: Pokemon):
        spec1 = randint(0, len(pokemonA.moves) - 1)
        pokemonB.hp = pokemonB.hp - pokemonA.moves[spec1][1]
        print_slow(
            "{} used {} and {} has {} health points".format(pokemonA.name,
                                                            pokemonA.moves[
                                                                spec1][0],
                                                            pokemonB.name,
                                                            pokemonB.hp))
        self.turn += 1

    def battle(self):
        if self.automan == "automatic":
            while (self.pokemon1.hp > 0) and (self.pokemon1.hp > 0):
                if self.pokemon1.hp <= 0:
                    return "{} is the winner with {} health points".format(self.pokemon2.name, self.pokemon2.hp)

                elif self.pokemon2.hp <= 0:
                    return "{} is the winner with {} health points".format(self.pokemon1.name, self.pokemon1.hp)

                elif (self.turn % 2) == 0:
                    self.attack(self.pokemon1, self.pokemon2)

                else:
                    self.attack(self.pokemon2, self.pokemon1)


if __name__ == "__main__":
    charmander = Pokemon("charmander", 100,
                         [("flame thrower", 10), ("earthquake", 50),
                          ("instant win", 5)])
    piplup = Pokemon("piplup", 100,
                     [("bubble beam", 10), ("surf", 50), ("instant win", 5)])
    gym = Battlefield(charmander, piplup, "automatic")
    print(gym.battle())
