import json
import random


def gen_citation():
    with open("data.json",'r',encoding="utf-8") as file:
        citations = json.load(file)

    random_index = random.randint(0, len(citations) - 1)

    random_citation = citations[random_index]

    print(f'"{random_citation["citation"]}" ~ {random_citation["auteur"]}')


def main():
    while True:
        print("\n----- Menu: -----")
        print("| 1. Générer une citation")
        print("| 0. Quitter")
        print("-------------------")

        choice = input("Entrez votre choix : ")
        if choice == "1":
            gen_citation()
        elif choice == "0":
            break

if __name__ == "__main__":
    main()