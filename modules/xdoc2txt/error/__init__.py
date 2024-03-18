class Xdoc2TxtErrorBase(Exception):
    def __init__(self, error: str=""):
        self.error = error[0]

    def __str__(self):
        return f"{self.error}"

class DllNotFoundError(Xdoc2TxtErrorBase):
    pass