#!/usr/bin/python3

import os
import random
import sys

arguments = sys.argv
if len(arguments) > 1:
    child_process_num = int(arguments[1])
    list_of_pids = []
    for i in range(child_process_num):
        pid = os.fork()
        if pid > 0:
            list_of_pids.append(pid)
            print(f"Parent[{os.getpid()}]: I ran children process with PID {pid}.")
        else:
            os.execl("./child.py", "child.py", str(random.randint(5, 10)))
    while len(list_of_pids) > 0:
        pid, exit_status = os.wait()
        exit_status = exit_status//256
        if pid > 0:
            print(f"Parent[{os.getpid()}]: Child with PID {pid} terminated. Exit Status {exit_status}.")
            list_of_pids.remove(pid)
else:
    print("There is no number of child processes")
