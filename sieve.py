# ref : https://m.blog.naver.com/dsz08082/22174314569

import time
import tkinter as tk
import tkinter.ttk as ttk


def main():
    s = Sieve()


class Sieve:

    def __init__(self, m:int=20, n:int=10, sleep_sec:float=0.5) -> None:
        self.m = m
        self.n = n
        self.sleep_sec = sleep_sec

        self.column_width = 50
        self.row_height = 25

        self.root = tk.Tk()
        self.root.title("Sieve of Eratosthenes")
        self.root.geometry(f"{self.column_width*(self.n+1)}x{self.row_height*self.m}+100+100")
        self.root.resizable(False, False)

        self.columns = [f"col{i:02d}" for i in range(self.n)]

        self.table = ttk.Treeview(
            self.root,
            height=self.m,
            columns=self.columns,
            displaycolumns=self.columns,
            show="tree",    # https://stackoverflow.com/a/51763444
        )
        self.table.pack()

        for col in range(self.n):
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

    def init_sieve(self):
        self.sieve = ['',] + list(range(2, self.m * self.n + 1))
        self.p = 0

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

        self.add_table_rows()

    def find_next_p(self) -> int:
        b_found = False
        for p in range(self.p+1, len(self.sieve)):
            if isinstance(self.sieve[p], int):
                result = p
                b_found = True
                break
        if not b_found:
            result = len(self.sieve) + 1

        return result

    def handle_spacebar(self, event):
        self.p = self.find_next_p()
        if self.p < len(self.sieve):

            pivot = self.sieve[self.p]

            self.sieve[self.p] = f"[{pivot}]"

            self.update()

            assert isinstance(pivot, int)

            # remove multiples of self.sieve[self.p]
            for k in range(self.p+1, self.m * self.n):
                if isinstance(self.sieve[k], int):
                    if not self.sieve[k] % pivot:
                        self.sieve[k] = ''
                        time.sleep(self.sleep_sec)
                        self.update()

        else:
            self.init_sieve()
            self.update()

    def update(self):
        self.update_table()
        # https://stackoverflow.com/questions/59845767
        self.root.update()



if "__main__" == __name__:
    main()
