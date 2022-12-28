from language import run, ExecContext
import locale
from IPython.core.magic import Magics, magics_class, line_cell_magic
from IPython import get_ipython, InteractiveShell


@magics_class
class CalcMagics(Magics):
    context = ExecContext()

    @staticmethod
    def get_str(line, cell=None):
        return line if cell is None else f"{line}\n\n{cell}"

    @line_cell_magic
    def model(self, line, cell=None):
        str = self.get_str(line, cell)
        new_context = run(str, self.context)
        self.context = new_context

    @line_cell_magic
    def whatif(self, line, cell=None):
        str = self.get_str(line, cell)

        run(str, self.context)


def register():
    locale.setlocale(locale.LC_ALL, "")
    ip: InteractiveShell = get_ipython()  # type: ignore
    if ip:
        ip.register_magics(CalcMagics)
