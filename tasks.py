# Premiere etape du projet : construire un générateur de probleme

# fonction qui recoit une valeur min et max , chosit deux entiers dans cet intervalle,
# construit un probleme du type "17+24="
# calcul la bonne réponse
# renvoie le pb et la reponse sous forme de texte

import random


def generate_addition_problem(min_value, max_value):
    x, y = random.randint(min_value, max_value), random.randint(min_value, max_value)

    z = x + y

    problem = f"{x}+{y}="
    answer = f"{z}"

    return problem, answer


def generate_dataset(number_of_problems, min_value, max_value):
    # creer une liste vide, generer plusieurs couples, les ajouter a la liste et les renvoyer
    list_tuples = []

    for i in range(number_of_problems):
        (p, a) = generate_addition_problem(min_value, max_value)
        list_tuples.append((p, a))

    return list_tuples


if __name__ == "__main__":
    random.seed(42)
    dataset = generate_dataset(5, 0, 99)
    print(dataset)
