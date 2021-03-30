#!/usr/bin/env python3

name = input("Which character do you want to know about? (wolverine, harry potter, or agent fitz) ")
stat = input("What statistic do you want to know about? (real name, powers,  or archenemy) ")

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},
"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}
    }

char_name = name
char_stat = stat

print(f"{char_name}'s {char_stat} is: {heroes[char_name][char_stat]}")
