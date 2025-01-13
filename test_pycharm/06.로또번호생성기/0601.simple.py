import random

lotto = []

rand_num = random.randint(1,40)

for i in range(6) :
    while rand_num in lotto :
        rand_num = random.randint(1, 40)
    lotto.append(rand_num)

lotto.sort()

print("로또 번호 : {} ".format(lotto))