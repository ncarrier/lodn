from tkinter import IntVar, StringVar


class OrigamiVariables(object):
    def __init__(self):
        self.name = StringVar()
        self.reference = IntVar()
        self.category = StringVar()
        self.comment = StringVar()
        self.paper_size = IntVar()
        self.diameter = IntVar()
        self.height = IntVar()
        self.length = IntVar()
        self.width = IntVar()
        self.materials = []
        self.quotation = IntVar()
