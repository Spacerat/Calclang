from language import run, ExecContext
import locale
from IPython.core.magic import Magics, magics_class, line_cell_magic, line_magic
from IPython.core.getipython import get_ipython
from IPython.core.interactiveshell import InteractiveShell

isDebug = False


@magics_class
class CalcMagics(Magics):
    context = ExecContext()

    @staticmethod
    def get_str(line, cell=None):
        return line if cell is None else f"{line}\n\n{cell}"

    @line_cell_magic
    def model(self, line, cell=None):
        str = self.get_str(line, cell)
        new_context = run(str, self.context, isDebug)
        self.context = new_context

    @line_magic
    def ctx(self, line):
        return self.context.values

    @line_cell_magic
    def what_if(self, line, cell=None):
        str = self.get_str(line, cell)
        run(str, self.context, isDebug)


def register(*, debug: bool = False):
    if debug:
        global isDebug
        isDebug = True
    locale.setlocale(locale.LC_ALL, "")
    ip: InteractiveShell = get_ipython()  # type: ignore
    if ip:
        ip.register_magics(CalcMagics)
