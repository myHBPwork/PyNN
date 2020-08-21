import logging
import moose

#logger = logging.getLogger("PyNN")
#name = "MOOSE"  # for use in annotating output data


class _Initializer(object):
    """Manage initialization of MOOSE cells."""
    def __init__(self):
        self.clear()

    def register(self, *items):
        pass

    def _initialize(self):
        pass

    def clear(self):
        self.cell_list = []
        self.population_list = []

# --- Initialization, and module attributes ------------------------------------
#state = _State()  # a Singleton, so only a single instance ever exists
#del _State
initializer = _Initializer()
del _Initializer
