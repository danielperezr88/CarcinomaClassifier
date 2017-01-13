from os import path, remove, getpid, popen
import inspect
import subprocess
import logging
from sys import executable as python_path


def save_pid():
    """Save pid into a file: filename.pid."""
    try:
        pidfilename = inspect.getfile(inspect.currentframe()) + ".pid"
        logging.info('PID ' + str(getpid()) + ' in ' + pidfilename)
        f = open(pidfilename, 'w')
        f.write(str(getpid()))
        f.close()
    except BaseException as e:
        logging.error('Failed to create pid file: ' + str(e))


def check_pid(pid):
    return int(popen("ps -p %d --no-headers | wc -l" % (int(pid) if len(pid) > 0 else 0,)).read().strip()) == 1


def launch_py(process):
    return str(subprocess.Popen([python_path, process]).pid)


def launch_py_if_stop(process):
    pidfile = process + ".pid"
    if path.exists(pidfile):
        pid_data = ''
        # check if pid is running
        with open(pidfile, 'r') as f:
            pid_data = f.read()
        if not check_pid(pid_data):
            pid = launch_py(process)
            remove(pidfile)
            with open(pidfile, 'w') as f:
                f.write(pid)
    else:
        pid = launch_py(process)
        with open(pidfile, 'w') as f:
            f.write(pid)


def stop_py(pid):
    popen("kill %s" % (pid,))
    return True


def keep_processes_alive(processes):
    for process in processes:
        launch_py_if_stop(process)


if __name__ == '__main__':

    logfilename = inspect.getfile(inspect.currentframe()) + ".log"
    logging.basicConfig(filename=logfilename, level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info("Started")

    save_pid()
    folderpath = path.dirname(path.realpath(__file__))
    processes = [path.join(folderpath, 'TF-img-API', 'TFWorker-API.py'), path.join(folderpath, 'APIConsumer', 'APIConsumer.py')]
    end = False

    while not end:
        keep_processes_alive(processes)

