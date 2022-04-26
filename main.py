import json
import os

def import_languages(selection):
    english = {}
    spanish = {}
    if selection == 1:
        with open("languages/english.json") as file:
            english = json.load(file)
            return english
    if selection == 2:
        with open("languages/spanish.json") as file:
            spanish = json.load(file)
            return spanish


def main():
    z = int(input("Select language: \n[1] Inglés\n[2] Español\n"))
    text = import_languages(z)
    while (True):
        print(text["menu"])
        print("[1] ", text["fibonacci"])
        print("[2] ", text["pi"])
        i = input()

main()