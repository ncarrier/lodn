from tkinter import Frame, ttk
from tkinter.filedialog import askdirectory


class ExportTab(Frame):
    def __init__(self, parent, catalog):
        Frame.__init__(self, parent)
        self.__catalog = catalog
        self.__parent = parent
        self.__button = button = ttk.Button(self, text="Export",
                                            command=self.__export)
        button.grid(column=0, row=0, pady=3, padx=3)

    def __export(self):
        folder_path = askdirectory(
            parent=self,
            title="Choose website folder"
        )
        if not folder_path:
            return

        self.__catalog.export(folder_path)
