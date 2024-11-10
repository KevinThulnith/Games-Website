from faker import Faker
from random import randint


def generateRandom():
    fg = f'{randint(1, 9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}'
    return fg


f = Faker()
for i in range(25):
    print(
        f"{ generateRandom() }/{f.unique.name()}/{f.unique.user_name()}/{f.unique.password()}/077 {randint(0, 10000000)} "
    )