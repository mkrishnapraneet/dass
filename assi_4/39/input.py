# import sys
# import select
# import time
# import tty
from __future__ import print_function
import signal
import time
# lots of lava flow

# class input:
  
#     __time=0.1
#     def __call__(self):
#         tty.setcbreak(sys.stdin.fileno())

#         time.sleep(self.__time)
#         if self.is_data():
#             return sys.stdin.read(1)
#         else:
#             return ""

#     def is_data(self):
#         return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

#     def SetTime(self,ti):
#         self.__time=ti


class  getChUnix:

    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
        fedvar = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fedvar)
        try:
            tty.setraw(sys.stdin.fileno())
            charvar = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
        return charvar


class AlarmException(Exception):
    pass