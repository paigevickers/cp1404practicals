class ProgrammingLanguage:
    def __init__(self, typing="", reflection="", year=0):
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
