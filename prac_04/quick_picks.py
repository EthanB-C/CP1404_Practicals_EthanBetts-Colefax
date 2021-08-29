import random

quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    quick_pick = [random.randint(0, 45) for number in range(6)]
    for x in range(len(quick_pick)):
        print(quick_pick[x], end='\t')
    print("")
