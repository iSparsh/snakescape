# Created By: Sparsh Mishra
# License: GPLv3.0

from turtle import *
import mountains

# Greetings
print("""
                                                                                                       
. . .     |                            |              ,---.          |         ,---.                    
| | |,---.|    ,---.,---.,-.-.,---.  --|---  ,---.    `---.,---.,---.|__/ ,---.`---.,---.,---.,---.,---.
| | ||---'|    |    |   || | ||---'    |     |   |        ||   |,---||  \ |---'    ||    ,---||   ||---'
`-'-'`---'`---'`---'`---'` ' '`---'    `---' `---'    `---'`   '`---^`   ``---'`---'`---'`---^|---'`---'
--- Created By Sparsh Mishra                                                                  |
""")

print("""This is a place where you can generate your own 2D Landscapes.
Answer the Snake's questionss and you will get your landssscapesss.
""")

# Questions Begin
print("----\n")
print("""🐍: Hello traveller! I sssee you are looking for a landssscape.
Just ansswer my questionss below and I will guide you to the treasssure myssself!
""")

## Q1)

print("""1) Early Morning
2) Mid day
3) Evening
4) Night
""")

time_of_day = ""
while (time_of_day == ""):

	time_of_day = str(input("> Choose wisely and type 1, 2, 3 or 4: "))

	if time_of_day == "1" or time_of_day.lower() == "one":
		print("🐍: Good choice!")
		time_of_day = "turquoise"

	elif time_of_day == "2" or time_of_day.lower() == "two":
		print("🐍: Good choice!")
		time_of_day = "skyblue"

	elif time_of_day == "3" or time_of_day.lower() == "three":
		print("🐍: Good choice!")
		time_of_day = "blue"

	elif time_of_day == "4" or time_of_day.lower() == "four":
		print("🐍: Good choice!")
		time_of_day = "darkblue"
	else:
		time_of_day = ""
		print("🐍: You have ssselected something I cannot understand, pleassee type 1, 2, 3 or 4")


print("🐍: Now let'sss make a landscape!")
mountains.start(time_of_day)

#EOF