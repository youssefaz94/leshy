import enum

class StateWorker(enum.Enum):
    running = 0 # worker in a running state
    pending = 1 # worker in a failed state pending instructions
    aborted = 2 # failure without resolution