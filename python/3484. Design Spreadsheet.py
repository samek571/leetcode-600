class Spreadsheet:
    def __init__(self, rows: int):
        self.hsh: dict[str, int] = {}

    def setCell(self, cell: str, value: int) -> None:
        self.hsh[cell] = value

    def resetCell(self, cell: str) -> None:
        self.hsh[cell] = 0

    def getValue(self, formula: str) -> int:
        idx = formula.find('+')
        if formula[1].isalpha():
            x = self.hsh.get(formula[1:idx], 0)
        else:
            x = int(formula[1:idx])

        if formula[idx+1].isalpha():
            y = self.hsh.get(formula[idx+1:], 0)
        else:
            y = int(formula[idx+1:])

        return x + y
