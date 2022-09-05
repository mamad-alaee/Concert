import random
import time


def create_random_id():
    randome1 = random.randint(1, 9)
    randome2 = random.randint(1, 9)
    randome3 = random.randint(1, 9)
    randome4 = random.randint(1, 9)
    randome5 = random.randint(1, 9)
    randome6 = random.randint(1, 9)
    randome7 = random.randint(1, 9)
    t = time.time()
    randome_text = str(randome1) + "1" + str(randome2) + "2" + str(randome3) + str(+ randome4) + str(randome5) + str(randome6) + str(randome7)
    return int(randome_text)
