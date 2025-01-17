import faiss
import numpy as np
from transformers import BertTokenizer, BertModel
import torch

documents = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "The early bird catches the worm.",
    "A picture is worth a thousand words.",
    "You miss 100% of the shots you don't take.",
    "In the middle of difficulty lies opportunity.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Life is 10% what happens to us and 90% how we react to it."
]

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).numpy()

document_embeddings = np.vstack([get_embedding(doc) for doc in documents])

dimension = document_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(document_embeddings)

faiss.write_index(index, "faiss_index.index")
print("FAISS index created and saved as 'faiss_index.index'")
