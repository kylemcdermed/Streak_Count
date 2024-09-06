import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    list = [] 
    streak_count = 1
    result = ['H' if random.randint(0,1) == 0 else 'T' for i in range(100)]
    
    streak_count = 1 
    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            streak_count += 1 
        else :
            streak_count = 1 
        
        if streak_count == 6:
            numberOfStreaks += 1 
            break;
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
