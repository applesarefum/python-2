import random as r
import colors as c

sides=[None]

sides.append(''' -------
|       |
|   •   |
|       |
 -------''')

sides.append(''' -------
| •     |
|       |
|     • |
 -------''')

sides.append(''' -------
| •     |
|   •   |
|     • |
 -------''')

sides.append(''' -------
| •   • |
|       |
| •   • |
 -------''')

sides.append(''' -------
| •   • |
|   •   |
| •   • |
 -------''')

sides.append(''' -------
| •   • |
| •   • |
| •   • |
 -------''')

sides.append(''' -------
| •   • |
| • • • |
| •   • |
 -------''')

sides.append(''' -------
| • • • |
| •   • |
| • • • |
 -------''')

sides.append(''' -------
| • • • |
| • • • |
| • • • |
 -------''')
dice=1
last_dice=1
print(c.red+c.clear)

print('To quit, press Ctrl+C at any time.')
def roll(dice,sides):
    try:
        while True:
            try:
                for c in range(int(dice)):
                    print(sides[r.randint(1,int(sides))])
            except ValueError:
                print('Invalid Number!')
    except KeyboardInterrupt:
        print('Buh-Bye')
