#!/usr/bin/python3

import os
import sys
import time
import random

argument = sys.argv[1]
pid = os.getpid()
print(f"Сhild[{pid}]: I am started. My PID {pid}. Parent PID [{os.getppid()}]")
time.sleep(int(argument))
print(f"Child[{pid}]: I am ended. PID {pid}. Parent PID {os.getppid()}")
exit_status = random.randint(0, 1)
os._exit(exit_status)