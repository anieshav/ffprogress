""" Author : Aniesh A.V. """
import time
from ff_time import FfTime


class Eta:
    """ Class to calculate ETA.
        Call function start_timer at the start of the task.  """

    def __init__(self):
        self._start_time = None
        self.eta = None

    def start_timer(self):
        self._start_time = time.time()

    def calculate_eta(self, percent_complete):
        time_elapsed = int(time.time() - self._start_time)
        time_remaining = int((time_elapsed * 100 / percent_complete) -
                             time_elapsed)
        ff_time = FfTime()
        ff_time.set_time_in_sec(time_remaining)
        self.eta = ff_time

    @property
    def formatted_eta(self):
        return self.eta.formatted_time

    @property
    def hrs(self):
        return self.eta.hrs

    @property
    def mins(self):
        return self.eta.mins

    @property
    def secs(self):
        return self.eta.secs
