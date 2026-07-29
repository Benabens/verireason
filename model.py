import torch
from torch import nn


class TokenEmbedding(nn.Module):

    def __init__(self, vocab_size, d_model):
        # Initialise correctement toute la mécanique interne de PyTorch.
        super().__init__()

        num_embeddings = vocab_size
        embedding_dim = d_model

        self.embedding = nn.Embedding(num_embeddings, embedding_dim)

    def forward(self, input_ids):
        token_vectors = self.embedding(input_ids)
        return token_vectors


class PositionEmbedding(nn.Module):

    def __init__(self, max_sequence_length, d_model):
        super().__init__()
        self.embedding = nn.Embedding(max_sequence_length, d_model)

    def forward(self, input_ids):
        seq_length = input_ids.shape[1]
        position_ids = torch.arange(seq_length, device=input_ids.device)
        position_vectors = self.embedding(position_ids)
        return position_vectors


if __name__ == "__main__":
    token_embedding = TokenEmbedding(15, 32)
    position_embedding = PositionEmbedding(64, 32)

    input_ids = torch.tensor([
        [1, 4, 10],
        [1, 5, 6],
    ])

    token_vectors = token_embedding(input_ids)
    position_vectors = position_embedding(input_ids)
    input_vectors = token_vectors + position_vectors

    print("input_ids:", input_ids.shape)
    print("token_vectors:", token_vectors.shape)
    print("position_vectors:", position_vectors.shape)
    print("input_vectors:", input_vectors.shape)
