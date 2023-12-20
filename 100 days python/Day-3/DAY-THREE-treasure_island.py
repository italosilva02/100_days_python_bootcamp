print('Welcome to Treasure Island\nYour mission is to find the treasure')

aswer = input('Left or right\n')

aswer = aswer.lower()

if aswer == 'right':
    print('Fall into a hole.\nGame Over')
    exit()

aswer = input('swim or wait\n')
aswer = aswer.lower()

if aswer == 'swim':
    print('Attacked by trout\nGame Over.')
    exit()

aswer = input('Whick door? (Red, Yellow Blue) \n')
aswer = aswer.lower()

if aswer == 'yellow':
    print('You Win!!')
elif aswer == 'blue':
    print('Eaten by beasts.\nGame Over')
elif aswer == 'red':
    print('Burned by fire\nGame Over')
else:
    print('Game Over.')