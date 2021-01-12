from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import utils as ut

class PubData(BaseModel):
    pub_id: str
    abstract: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/clean/")
async def clean_text(data: PubData):
    clean_abstract = ut.clean_text(data.abstract)

    res = {
        "pub_id": data.pub_id,
        "clean_abstract": clean_abstract
    }
    return res
