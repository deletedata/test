import random
import string


def ran_numi(num1, num2, cnt):
    for i in range(cnt):
        num3 = random.randint(num1, num2)
        print(num3)
def ran_numf(num1, num2, cnt):
    for i in range(cnt):
        num3 = random.uniform(num1, num2)
        print(num3)

def ran_str( cnt ):
    for x in range(cnt):
        print(''.join(random.choice(string.ascii_letters ) for _ in range(3)))
        print(''.join(random.choice(string.digits) for _ in range(10)))
        print(''.join(random.choice(string.digits) for _ in range(2)))

cnt = 10
ran_str(10)


