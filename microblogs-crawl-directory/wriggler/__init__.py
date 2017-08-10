"""
Wriggler crawler module.
"""

import sys

class Error(Exception):
    """
    All exceptions returned are subclass of this one.
    """

class Logger(object):
    """
    Mock logger class
    """

    def log(self, level, msg, *args, **kwargs): # pylint: disable=no-self-use
        sys.stderr.write(level + " " + msg.format(*args, **kwargs) + "\n")
        sys.stderr.flush()

    def critical(self, msg, *args, **kwargs):
        return self.log("CRITICAL", msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return self.log("ERROR", msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        return self.log("WARNING", msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        return self.log("INFO", msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        pass
        # return self.log("DEBUG", msg, *args, **kwargs)

log = Logger()
