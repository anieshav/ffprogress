""" Author : Aniesh A.V. """


class FfTime:
    """ Time object meant to measure time required, time taken etc.
        Hrs, mins and secs must be supplied as numeric. """

    def __init__(self):
        self.hrs = None
        self.mins = None
        self.secs = None

    @property
    def time_in_secs(self):
        return (self.hrs * 60 * 60) + (self.mins * 60) + self.secs

    @property
    def formatted_time(self):
        return '{:0>2}:{:0>2}:{:0>2}'.format(self.hrs, self.mins, self.secs)

    def set_time_in_sec(self, sec):
        self.mins, self.secs = divmod(sec, 60)
        self.hrs, self.mins = divmod(self.mins, 60)
