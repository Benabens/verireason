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

    for _ in range(number_of_problems):
        p, a = generate_addition_problem(min_value, max_value)
        list_tuples.append((p, a))

    return list_tuples


#********************************************************************************************************

# on a dans deja une focntion qui genere des problemes
# on prend ce probleme on l'encode pour pouvoir le donner au transformer
# le transformer predit le prochain bon token
# on verifie la reponse avec cette prochaine fonction verify_addtition

# cette fonction doit recevoir le probleme et la reponse , et dire si c juste


def verify_addition(problem, answer):

    # problem ca peut etre "17+23="
    list_operand = problem.removesuffix("=").split("+")
    # j'ai une liste de deux string ["17", "23"]

    x = int(list_operand[0])
    y = int(list_operand[1])

    z = x + y

    to_verify = int(answer)

    if z == to_verify:
        return True
    else:
        return False


#main guard
if __name__ == "__main__":
    random.seed(42)
    dataset = generate_dataset(5, 0, 99)
    print(dataset)
    print(verify_addition("17+23=", "40"))
    print(verify_addition("17+23=", "31"))
