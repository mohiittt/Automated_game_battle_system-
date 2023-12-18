# Automated_game_battle_system

Welcome to your first video game creation in python. You will create a video game that creates a character's health and attack stats...along with an epic name for your character.

**Part 1 - **

1. Write a subroutine that generates a character: first name and character type (human, imp, wizard, elf, etc.).
2. Write a subroutine that multiplies a bunch of random dice rolls together to generate the character's health stats. Use this formula:
      (6-sided-roll * 12-sided-roll) / 2 + 10

3. Write a second subroutine that multiplies a bunch of random dice rolls together to generate the character's strength stats. Use this formula:
      (6-sided-roll * 12-sided-roll) / 2 + 10

4. Present the data in a menu with time.sleep and os.system("clear") to make it appealing.
5. Wrap it in a loop so the user has the option to create another character.

That was first part of the game. save it and move on to part 2 to make it more intresting.

** Part 2 -**

1. Add return functions to your character's health and strength statuses from Day 27's project.
2. Generate two different characters and store their data (health and strength stats, character type, name, etc.).
3. Use a while True loop to simulate those two characters battling.
4. Roll one six-sided dice for both characters. The character who rolls the higher amount wins that round.
5. The winner of that round (the one who rolled the higher number) will give damage to the other character by doing the following:
6. Find the difference between the strength of both opponents and add one.
7. Take that amount away from the loser's health.
8. At the end of each round, check the stats of each character to ensure neither of them have died yet.
9. When one character dies (they run out of health), declare a winner of the battle!
10. To keep this battle from looking hideous between rounds use time.sleep to pause between rounds os.system("clear") to ensure the screen clears between battles.

Follow for more - https://twitter.com/mohittt_p
