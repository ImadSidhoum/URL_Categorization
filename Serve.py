from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
from transformers import AutoTokenizer
import torch
from tools import *

# Initialisation
app = FastAPI()

# Getting label encoder from file
label_encoder = LabelEncoder()
label_encoder.load('artifacts/label_encoder')
model = torch.load('artifacts/camemBert_model_URLs',map_location=torch.device('cpu'))
# fixed max length 
max_length = 30
# getting the tokenizer
tokenizer = AutoTokenizer.from_pretrained("camembert-base", do_lower_case=True)

#fixed threshold
threshold = 0.50
# requets
class Item(BaseModel):
    data: list


@app.get('/')
async def index():

    return "Server Up"

@app.post('/predict')
async def predict(item:Item):
    URLs = item.data
    print(URLs)

    # preprocessing urls
    preprocessed_data = [preprocess_url(url) for url in URLs]
    # tokenizing the urls
    preprocessed_data = tokenizer.batch_encode_plus(preprocessed_data,max_length=max_length,pad_to_max_length=True)

    # doing the inferencce and geting the logits
    out = model(torch.tensor(preprocessed_data['input_ids']), token_type_ids=None, attention_mask=torch.tensor(preprocessed_data['attention_mask']))[0]
    pred_label = torch.sigmoid(out).detach().numpy()

    # conveting the output to binray vectors
    pred_bools = np.where(pred_label>threshold,1,0)
    labels = label_encoder.decode(pred_bools)
    print(labels)

    return labels
