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

import sys
from .ui.main_window import MainWindow


def usage(status):
    print(_("Usage: lodn [/path/to/tree/structure]"))
    sys.exit(status)


def main():
    if len(sys.argv) not in [1, 2]:
        usage(1)

    if len(sys.argv) == 2 and sys.argv[1] in ["-h", "--help", "-?"]:
        usage(0)

    window = MainWindow(None if len(sys.argv) == 1 else sys.argv[1])

    window.loop()


if __name__ == '__main__':
    main()
