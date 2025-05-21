from dataclasses import dataclass
@dataclass
class Person:
    name:str
    age:int

p=Person("Kinza",19)
print(p)    




from typing import TypeVar, Generic

T = TypeVar('T')  # T can be any type

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content

    def get_content(self) -> T:
        return self.content

box_int = Box(123)       # Box[int]
box_str = Box("hello")   # Box[str]
