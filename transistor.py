class Transistor:
    def __init__(self, type: str, mark: str, i_max: int, u_max: int) -> None:
        self.type = type
        self.mark = mark
        self.i_max = i_max
        self.u_max = u_max

    def __str__(self) -> str:
        return f"Transistor: [{self.type}], mark: {self.mark}, Imax = {self.i_max}, Umax = {self.u_max}"

    def __lt__(self, other) -> bool:
        return self.type < other.type or (self.type == other.type and self.i_max < other.i_max)

    def __gt__(self, other) -> bool:
        return other < self
