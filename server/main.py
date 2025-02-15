from fastapi import FastAPI
import os
import pandas as pd
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(BASE_DIR, 'cache')

dataset = os.path.join(CACHE_DIR, 'movies-box-office-dataset-cleaned.csv')
app = FastAPI()

@app.get('/')
def read_root():
    return {"hello": "world"}

@app.get('/box-office')
def read_box_office_numbers():
    df = pd.read_csv(dataset)
    return df.to_dict("Rank")
