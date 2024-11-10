from faker import Faker
from random import randint

f = Faker()
for i in range(10):
    print(
        f" {f.unique.name()}   {f.unique.email()}  {f.unique.user_name()} {f.unique.password()} 077 {randint(0, 10000000)} "
    )

for n in range(10):
    print(f" {randint(2000, 2015)}-{ randint(0, 12) }-{ randint(0, 30) } ")
