# This file is part of lodn.

# lodn is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# lodn is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# lodn. If not, see <https://www.gnu.org/licenses/>.

from tkinter import Tk, ttk
import tkinter
from lodn.ui.catalog_tab import CatalogTab
from lodn.ui.export_tab import ExportTab
from lodn.catalog.catalog import Catalog

appname = "lodn"

import gi  # noqa F401
from gi.repository import GObject  # noqa F401


class MainWindow(object):
    '''
    classdocs
    '''

    def __init__(self, tree_structure):
        '''
        Constructor
        '''
        self.__tree_structure = tree_structure
        self.__root = Tk(className=appname)
        self.__catalog = Catalog(tree_structure)
        self.__loop = GObject.MainLoop()
        GObject.idle_add(self.__refresh)
        self.__close_event_observers = []
        self.__root.protocol('WM_DELETE_WINDOW', self.__close_event_handler)
        rceo = self.__register_close_event_observer
        rceo(self.__root.destroy)
        rceo(self.__loop.quit)
        self.__setup_window()

    def __close_event_handler(self):
        for ceo in reversed(self.__close_event_observers):
            ceo()

    def __register_close_event_observer(self, close_event_observer):
        self.__close_event_observers.append(close_event_observer)

    def __setup_window(self):
        self.__root.title(appname.capitalize())
        self.__setup_notebook()

    def __setup_notebook(self):
        self.__notebook = notebook = ttk.Notebook(self.__root)
        notebook.pack(
            side=tkinter.TOP,
            anchor=tkinter.NW,
            fill=tkinter.BOTH,
            expand=1,
            padx=(6, 6),
            pady=(6, 6)
        )
        self.__setup_tabs()

    def __setup_catalog_tab(self, notebook):
        self.__catalog_tab = catalog_tab = CatalogTab(notebook, self.__catalog)
        catalog_tab.pack(fill=tkinter.BOTH, expand=True)
        catalog_tab.columnconfigure(0, weight=1)
        self.__register_close_event_observer(catalog_tab.close_catalog)
        notebook.add(catalog_tab, text="Catalog")
        notebook.pack(expand=1, fill="both")

    def __setup_export_tab(self, notebook):
        self.__export_tab = export_tab = ExportTab(notebook, self.__catalog)
        export_tab.pack(fill=tkinter.BOTH, expand=True)
        export_tab.columnconfigure(0, weight=1)
        notebook.add(export_tab, text="Export")
        notebook.pack(expand=1, fill="both")

    def __setup_tabs(self):
        notebook = self.__notebook
        self.__setup_catalog_tab(notebook)
        self.__setup_export_tab(notebook)

    def __refresh(self):
        self.__root.update()
        return True

    def loop(self):
        self.__loop.run()
