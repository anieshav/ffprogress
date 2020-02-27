""" Author : Aniesh A.V. """

import re
from ff_time import FfTime


class StdoutAnalyzer:
    """ Analyzes stdout of ffmpeg and gathers various details.
        the gathered details are stored in a dict named result"""

    def __init__(self):
        self._time = FfTime()
        self.result = {}
        self._duration = None

    def analyze(self, line):
        self._extract_time(line)
        self._extract_progress_details(line)
        if self._duration is None:
            self._extract_duration(line)
        return self.result

    def _extract_time(self, line):
        p = re.compile(r'time=(\d+):(\d+):(\d+)')
        m = p.search(line)
        if m:
            self._time.hrs = int(m.group(1))
            self._time.mins = int(m.group(2))
            self._time.secs = int(m.group(3))
            self.result['time'] = self._time

    def _extract_progress_details(self, line):
        # Analyses the same line which extract time method analyses.
        # Wrote this as a seperate function since it is not critical
        p = re.compile((
            r'fps=\s*(\d+).*?size=\s*(\d+).*?bitrate=\s*(\d*)'
        ))
        m = p.search(line)
        if m:
            self.result['fps'] = m.group(1)
            self.result['size'] = int(m.group(2))
            self.result['bitrate'] = m.group(3)

    def _extract_duration(self, line):
        p = re.compile(r'Duration: (\d{2}):(\d{2}):(\d{2})')
        m = p.search(line)
        if m:
            self._duration = FfTime()
            self._duration.hrs = int(m.group(1))
            self._duration.mins = int(m.group(2))
            self._duration.secs = int(m.group(3))
            self.result['duration'] = self._duration
