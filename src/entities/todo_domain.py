from dataclasses import dataclass


@dataclass
class TodoDomain:
    name: str
    description: str
    id: str = 'ABC0001'
    