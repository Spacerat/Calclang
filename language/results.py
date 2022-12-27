from dataclasses import dataclass
from typing import Union, List
from dataclasses import dataclass
from typing import Dict, Union, List
import numpy as np
from itertools import groupby
import networkx as nx
from .ExecContext import ExecContext


@dataclass
class StatementResult:
    text: str
    value: Union[int, float]


@dataclass
class AssignmentResult:
    text: str
    target: str
    value: Union[int, float]


@dataclass
class ProgramResults:
    statements: List[StatementResult]
    context: ExecContext
    lastResult: Union[StatementResult, AssignmentResult]
