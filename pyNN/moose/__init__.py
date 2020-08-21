from pyNN.common.control import DEFAULT_MAX_DELAY, DEFAULT_TIMESTEP, DEFAULT_MIN_DELAY
from pyNN import common
#from pyNN.moose import simulator
#from pyNN.moose.populations import Population
#from pyNN.moose.projections import Projection


# =============================================================================
#   Utility functions
# =============================================================================

def list_standard_models():
    pass

# =============================================================================
#   Functions for simulation set-up and control
# =============================================================================

def setup(timestep=DEFAULT_TIMESTEP, min_delay=DEFAULT_MIN_DELAY, **extra_params):
    """Called at the very beginning of a script."""
    common.setup(timestep, min_delay, **extra_params)
    #simulator.initializer.clear()

def end(compatible_output=True):
    """Any necessary clean up before exiting."""
    pass

#run, run_until = common.build_run(simulator)
#run_for = run

#reset = common.build_reset(simulator)

#initialize = common.initialize

# =============================================================================
#   Functions returning information about the simulation state
# =============================================================================

#get_current_time, get_time_step, get_min_delay, get_max_delay, \
#            num_processes, rank = common.build_state_queries(simulator)

# =============================================================================
#   Low-level API for creating, connecting and recording individual neurons
# =============================================================================

#create = common.build_create(Population)

#connect = common.build_connect(Projection, FixedProbabilityConnector, StaticSynapse)

#set = common.set

#record = common.build_record(simulator)

#record_v = lambda source, filename: record(['v'], source, filename)

#record_gsyn = lambda source, filename: record(['gsyn_exc', 'gsyn_inh'], source, filename)
