from typing import Union
from fastapi import FastAPI
from .language import parse_string, analyse_result, Analysis
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Result(BaseModel):
    result: Analysis


app = FastAPI()

origins = [
    "https://calculator-spacerat.vercel.app/",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/compute/")
def read_item(code: str) -> Result | None:
    analysis = analyse_result(parse_string(code).execute().last_result)
    if not analysis:
        return None
    return Result(result=analysis)
