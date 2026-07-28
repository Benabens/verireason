# 1. Demande des problemes a tasks.py
# 2. les encode avec tokenizer.py
# 3. Construit pour chaque probleme :
#
#.    dataset.py
#.    → sait transformer un couple en
#  (input_ids, target_ids, loss_mask)
#
#
# on code une fonction capbale de transformer un tuple
# (problem, answer) en ces trois listes ( vecteurs)


from tokenizer import encode
from tasks import generate_dataset

from torch.utils.data import Dataset, DataLoader
import torch


def build_training_sample(problem, answer):

    l1 = encode(problem, True)
    l2 = encode(answer, False, True)

    full_seq = l1 + l2

    #  full_sequence = toute l’histoire complète
    #   input_ids      = toute l’histoire sauf le dernier token
    #   target_ids     = toute l’histoire sauf le premier token

    input_ids = full_seq[:-1]
    target_ids = full_seq[1:]

    mask1 = [0] * (len(l1) - 1)
    mask2 = [1] * (len(l2))
    loss_mask = mask1 + mask2

    return input_ids, target_ids, loss_mask



#  PRÉPARATION DES DONNÉES
#
#   dataset.py
# ├── construit un exemple d’entraînement  --V
# ├── gère plusieurs exemples              ← NOUS SOMMES ICI
# ├── convertit en tenseurs
# └── ajoute padding et batches



#Classe AdditionDataset
#├── données : liste des problèmes
#├── comportement : dire combien il y en a
#└── comportement : préparer le problème numéro i
#
#
## Puis on pourra créer différents objets :
#
#
# train_dataset      → problèmes d’entraînement
# validation_dataset → problèmes de validation
# ood_dataset        → problèmes plus difficiles
#
#

class AdditionDataset(Dataset):

    def __init__(self, number_of_problems, min_value, max_value):

        tuples_problem_answer = generate_dataset(number_of_problems, min_value, max_value)
        self.samples = tuples_problem_answer

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, i):
        problem = self.samples[i][0]
        answer = self.samples[i][1]

        list1, list2, list3 = build_training_sample(problem, answer)
        input_ids_tensor = torch.tensor(list1, dtype=torch.long)
        target_ids_tensor = torch.tensor(list2, dtype=torch.long)
        loss_mask_tensor = torch.tensor(list3, dtype=torch.bool)

        return input_ids_tensor, target_ids_tensor, loss_mask_tensor



 # **********************************************************************
 # collate_batch reçoit quelque chose comme :
 #
 #  samples = [
 #   (
  #      input_ids_tensor_exemple_1,
   #     target_ids_tensor_exemple_1,
#    loss_mask_tensor_exemple_1
#),
    #(
    #    input_ids_tensor_exemple_2,
    #    target_ids_tensor_exemple_2,
    #    loss_mask_tensor_exemple_2
    #)
def collate_batch(samples):

    max_length = max(len(sample[0]) for sample in samples)

    padded_input_ids = []
    padded_target_ids = []
    padded_loss_masks = []

    for sample in samples:
        input_ids, target_ids, loss_mask = sample

        padded_input = pad_tensor(input_ids, max_length, 0)
        padded_target = pad_tensor(target_ids, max_length, 0)
        padded_mask = pad_tensor(loss_mask, max_length, False)

        padded_input_ids.append(padded_input)
        padded_target_ids.append(padded_target)
        padded_loss_masks.append(padded_mask)

    batch_input_ids = torch.stack(padded_input_ids)
    batch_target_ids = torch.stack(padded_target_ids)
    batch_loss_masks = torch.stack(padded_loss_masks)

    return batch_input_ids, batch_target_ids, batch_loss_masks


def pad_tensor(tensor_init, target_length, padding_value):

    missing_elements = target_length - len(tensor_init)

    t1 = torch.full((missing_elements,), padding_value, dtype=tensor_init.dtype)

    t2 = torch.cat((tensor_init, t1))

    return t2


if __name__ == "__main__":
    addition_dataset = AdditionDataset(10, 0, 99)

    dataloader = DataLoader(
        addition_dataset,
        batch_size=4,
        shuffle=True,
        collate_fn=collate_batch
    )

    dataloader_iterator = iter(dataloader)
    batch = next(dataloader_iterator)

    print(type(batch))
    print(len(batch))
    batch_input_ids, batch_target_ids, batch_loss_masks = batch
    print(batch_input_ids.shape)
    print(batch_target_ids.shape)
    print(batch_loss_masks.shape)
