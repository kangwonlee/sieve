# ref : https://m.blog.naver.com/dsz08082/22174314569

import tkinter as tk
import tkinter.ttk as ttk


def main():
    s = Sieve()


class Sieve:
    def __init__(self, m:int=3, n:int=10) -> None:

        self.m = m
        self.n = n

        self.column_width = 50

        self.root = tk.Tk()
        self.root.title("Sieve of Erastosthenes")
        self.root.geometry(f"{self.column_width*(self.n+1)}x{100*self.m}+100+100")
        self.root.resizable(False, False)

        self.columns = [f"col{i:02d}" for i in range(10)]

        self.table = ttk.Treeview(
            self.root,
            columns=self.columns,
            displaycolumns=self.columns,
            show="tree",    # https://stackoverflow.com/a/51763444
        )
        self.table.pack()

        for col in range(10):
            self.table.column(
                f"#{col}",
                width=self.column_width
            )

        self.sieve = ['',] + list(range(2, self.m * self.n + 1))

        # pivot
        self.p = 0

        self.root.bind("<space>", self.handle_spacebar)

        self.add_table_rows()

        self.root.mainloop()

    def iter_rows(self):
        for i in range(0, len(self.sieve), self.n):
            j = i + self.n
            yield self.sieve[i:j]

    def add_table_rows(self):
        for i, row in enumerate(self.iter_rows()):
            self.table.insert('', 'end', text='', values=row, iid=f"row{i:02d}")

    def update_table(self):
        # https://stackoverflow.com/questions/53468581
        for row in self.table.get_children():
            self.table.delete(row)

        for i, row in enumerate(self.iter_rows()):
            self.table.insert('', 'end', text='', values=row, iid=f"row{i:02d}")

    def handle_spacebar(self, event):
        # https://stackoverflow.com/questions/59845767

        # find next int element in self.sieve
        while not isinstance(self.sieve[self.p], int):
            self.p += 1

        pivot = self.sieve[self.p]

        assert isinstance(pivot, int)

        # remove multiples of self.sieve[self.p]
        for k in range(self.p+1, self.m * self.n):
            print(f"p = {pivot} self.sieve[{k}] = ", end='')
            print(repr(self.sieve[k]))
            if isinstance(self.sieve[k], int):
                if not self.sieve[k] % pivot:
                    self.sieve[k] = ''
                    print(f"self.sieve[{k}] = {self.sieve[k]!r}")

        self.update_table()
        self.root.update()

        self.p += 1


if "__main__" == __name__:
    main()
