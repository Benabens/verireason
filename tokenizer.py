# Définir le vocabulaire, c'est-à-dire tous les symboles que notre
# transformer est autorisé à manipuler.

# On va représenter les 15 tokens dans une liste ordonnée.
# On utilise une liste et pas un set, car l'ordre détermine les identifiants.

special_tokens = ["<PAD>", "<BOS>", "<EOS>"]
digits = list("0123456789")
symbols = ["+", "="]

vocabulary = special_tokens + digits + symbols

# Création du dictionnaire token -> identifiant.
token_to_id = {}

for index, token in enumerate(vocabulary):
    token_to_id[token] = index  # dictionnaire[clé] = valeur

id_to_token = {}

for index, token in enumerate(vocabulary):
    id_to_token[index] = token


# La fonction encode remplace chaque caractère par son identifiant.
# Exemple : "42+97=" -> [7, 5, 13, 12, 10, 14].

def encode(text, add_bos=False, add_eos=False):
    output = []

    if add_bos:
        output.append(token_to_id["<BOS>"])

    for char in text:
        output.append(token_to_id[char])

    if add_eos:
        output.append(token_to_id["<EOS>"])

    return output


def decode(token_ids):
    output = ""

    for token_id in token_ids:
        output += id_to_token[token_id]

    return output
