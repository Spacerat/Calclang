from typing import Union
from fastapi import FastAPI
from .language import parse_string, analyse_result, Analysis
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import logging
from typing import TypedDict

logger = logging.getLogger(__name__)


app = FastAPI()

origins = [
    "https://calculator-spacerat.vercel.app",
    "http://calculator-spacerat.vercel.app",
    "http://localhost",
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Result(TypedDict):
    analysis: Analysis


@app.get("/compute", response_model=Result)
def read_item(code: str) -> Result | None:
    last_result = parse_string(code).execute().last_result
    if last_result:
        analysis = analyse_result(last_result)
        if analysis:
            return Result(analysis=analysis)

    return None
