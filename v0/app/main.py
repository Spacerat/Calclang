from typing import Union
from fastapi import FastAPI
from .language import parse_string, analyse_result, Analysis
from pydantic import BaseModel


class Result(BaseModel):
    result: Analysis


app = FastAPI()


@app.get("/compute/")
def read_item(code: str) -> Result | None:
    analysis = analyse_result(parse_string(code).execute().last_result)
    if not analysis:
        return None
    return Result(result=analysis)
