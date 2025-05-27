import typing

class listObject:
    name = None
    checked = None
    tags = []
    def __init__(self, name):
        self.name = name
        self.checked = False
    def check(self):
        self.checked = True
    def unCheck(self):
        self.checked = False


class list:
    name = None
    listobjects = []
    def __init__(self, name: str):
        self.name = name
    def setListObjects(listObjects):
        listobjects = listObjects