import random
def flip ():
    return random.randint(0,1)

def cointoss ():
    results = {"heads ": 0, "tails ": 0}
    for i in range(100):
        if flip() == 0:
            results["heads "] += 1
        else:
            results["tails "] += 1
    print(results)
flip()
cointoss()