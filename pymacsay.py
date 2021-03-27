"""pymacsay is a wrapper for the command-line tool `say` in macOS"""

import os

from subprocess import run
from typing import Optional

__version__ = '1.0.0'


class Say:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError('Could not find executable say in ' + path)
        self.path = path

    def _raw_say(self, *arguments, voice='', rate=''):
        outputs = list()

        for arg in arguments:
            cmd_call = [self.path, '-v', voice, '-r', rate] + list(arg)
            output = run(cmd_call)
            outputs.append(output)

        for output in outputs:
            if output.returncode != 0:
                # Something unexpected occured
                return False

        # No errors, return True
        return True

    def say(self, *something: str, voice: Optional[str] = 'samantha', rate: Optional[int] = 250):
        """Say anything in Siri's voice. Wraps around a macOS builtin `say`, and therefore compatible only with macOS
        \nOptionally, an argument `rate: int` could be provided in order to change the speech rate (in words per minute)
        \nReturns a boolean indicating function success."""
        success = self._raw_say(something, voice=voice, rate=str(rate))
        return success
