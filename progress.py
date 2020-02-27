""" Author Aniesh A.V. """
#  import sys
from tqdm import tqdm
from stdout_analyser import StdoutAnalyzer


class Progress:
    """ Shows progress of the encoding task.
        Stdout of ffmpeg must be fed into this class
        line by line. """

    def __init__(self):
        self.analyzer = StdoutAnalyzer()
        self.percent_complete = 0
        self.pbar = tqdm(total=100)
        #self.pbar = tqdm(total=100,ascii=True)
        self.verbose = False
        self.stdout_log = ''

    @staticmethod
    def calculate_percent_complete(result):
        duration_in_seconds = result['duration'].time_in_secs
        if duration_in_seconds == 0:
            return 100
        curr_time_in_seconds = result['time'].time_in_secs
        percent_complete = int(
            curr_time_in_seconds * 100 / duration_in_seconds)
        return percent_complete

    @staticmethod
    def _estimate_total_size(curr_size, percent_complete):
        if curr_size == 0:
            return 0
        return curr_size * 100 // percent_complete

    def show_progress(self, line):
        """ Shows a progress bar. """
        self.stdout_log += line + '\n'
        result = self.analyzer.analyze(line)
        if 'duration' in result and 'time' in result:
            percent_complete = self.calculate_percent_complete(result)
            if percent_complete > self.percent_complete:
                self._update_pbar(percent_complete, result)
                self.percent_complete = percent_complete
        elif self.verbose:
            print(line, flush=True)

    def _update_pbar(self, percent_complete, result):
        curr_sz = result.get('size', 0) // 1024
        total_sz = self._estimate_total_size(curr_sz, percent_complete)
        fps = result.get('fps', 0)
        self.pbar.set_postfix(size='{}/{}'.format(curr_sz, total_sz), fps=fps)
        self.pbar.update(percent_complete - self.percent_complete)

    def cleanup(self):
        self.pbar.close()

    def clear(self):
        self.pbar.clear()


if __name__ == '__main__':
    P = Progress()
    P.show_progress(
        'Duration: 00:00:50.45, start: 0.000000, bitrate: 102374 kb/s')

    LINE = ('frame= 1285 fps= 41 q=27.0 size=    5185kB'
            ' time=00:00:05.50 bitrate= 824.8kbits/s speed=1.64x')
    P.show_progress(LINE)
