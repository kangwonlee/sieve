# ref : https://m.blog.naver.com/dsz08082/22174314569

import tkinter as tk
import tkinter.ttk as ttk


def main():

    m = 3
    n = 10

    width = 100

    root = tk.Tk()
    root.title("Erasthotenes Sieve")
    root.geometry(f"{width*(n+1)}x{100*m}+100+100")
    root.resizable(False, False)

    columns = [f"col{i:02d}" for i in range(10)]

    treeview = ttk.Treeview(
        root,
        columns=columns,
        displaycolumns=columns,
        show="tree",    # https://stackoverflow.com/a/51763444
    )
    treeview.pack()

    for col in range(10):
        treeview.column(f"#{col}", width=width)
        treeview.heading(f"#{col}", text="")

    treelist = [
        tuple(range( 1, 10+1)),
        tuple(range(11, 20+1)),
        tuple(range(21, 30+1)),
    ]

    for i, row in enumerate(treelist):
        treeview.insert('', 'end', text='', values=row, iid=f"row{i:02d}")

    root.mainloop()


if "__main__" == __name__:
    main()
