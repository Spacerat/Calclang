from dataclasses import dataclass
from typing import List
from dataclasses import dataclass
from typing import Dict, List
import networkx as nx


@dataclass
class ExecContext:
    values: Dict[str, int]
    graph: nx.DiGraph

    def add_assignment(self, target: str, deps: List[str]):
        # invalidate the target and everything which depends on it

        self.values[target] = None

        if target in self.graph:
            for nodes in nx.dfs_predecessors(self.graph.reverse(copy=False), target):
                for node in nodes:
                    self.values[node] = None

            # replace this assignment's dependencies

            for successor in self.graph.successors(target):
                self.graph.remove_edge(target, successor)

        self.graph.add_node(target)
        for dep in deps:
            self.graph.add_edge(target, dep)

    def get_invalid_nodes_from_leaves(self):
        for node in nx.topological_sort(self.graph.reverse(copy=False)):
            if self.values[node] is None:
                yield node
