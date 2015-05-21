#!/usr/bin/env python3
import roll as r
import colors as c
stats=['Intelligence:','Strength:','Wisdom:','Agility:','Luck:','Charisma:','Dexterity:','Tenacity:']
print(c.clear+'What is your players name?')
name=input('>').strip().title()
print(c.clear+"{}'s stats are".format(name))
for item in stats:
    print(item,r.parse_roll('2d5'))
