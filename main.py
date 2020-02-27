""" The entry point module.
    Run this module with ffmpeg's arguments, they will be passed
    on to Ffmpeg. """

import sys
import subprocess
from progress import Progress


def run_command(command):
    """ Run the command, capture output and send it to the
        Progress Object. """
    progress = Progress()
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        encoding='utf-8'
        )
    for line in process.stdout:
        # line = line.decode('utf-8')
        progress.show_progress(line.strip())
    exit_code = process.wait()
    if exit_code:
        progress.clear()
        if not progress.verbose:
            print(progress.stdout_log)
    progress.cleanup()

if __name__ == "__main__":
    #  run_command("ping -n 5 google.com")
    #  run_command((
        #  r'ffmpeg -y -i "D:\\temp\\test\\WrongDar.mp4"'
        #  ' -c:v libx264 -preset slow -crf 22'
        #  ' -c:a aac -b:a 128k D:\\temp\\test\\output.mkv'))
    run_command(['ffmpeg', '-nostdin'] + sys.argv[1:])
