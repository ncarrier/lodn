"""
TTKScrolledText is the same as tkinter's ScrolledText, but with the vertical
scrollbar supporting themes.
"""
import tkinter as tk
import tkinter.ttk as ttk


class TTKScrolledText(tk.Text):
    GEOMETRY_METHODS = [
        m for m in (vars(tk.Pack) | vars(tk.Grid) | vars(tk.Place))
        if m not in (set(vars(tk.Text)) | {"config", "configure"})
        and m[0] != "_"
    ]

    def __setup_geometry_methods(self):
        """
        Override the geometry methods with that of the Pack, Grid and Place
        layout managers
        """
        for m in TTKScrolledText.GEOMETRY_METHODS:
            setattr(self, m, getattr(self.__frame, m))

    def __init__(self, master=None, **kw):
        """
        Constructor.
        Creates a frame in which to place the tk.Text and its vertical
        scrollbar.
        Also connects the scrollbar to the text widget.
        """
        self.__frame = ttk.Frame(master)

        self.__vbar = ttk.Scrollbar(self.__frame)
        self.__vbar.pack(side=tk.RIGHT, fill=tk.Y)
        kw.update({'yscrollcommand': self.__vbar.set})
        self.__vbar['command'] = self.yview

        tk.Text.__init__(self, self.__frame, **kw)
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.__setup_geometry_methods()

    def __str__(self):
        "String representation of the TTKScrolledText"
        return str(self.__frame)


if __name__ == "__main__":
    tst = TTKScrolledText()
    tst.insert(tk.END, __doc__)
    tst.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    tst.mainloop()
