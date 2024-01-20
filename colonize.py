import platform

from spain.config import namespace, parse_arguments
from spain.tasks import schedule, task1

if __name__ == "__main__":
    parse_arguments()

    task = int(namespace.task[-1])

    if task == 1:
        assert platform.system() == "Windows"
        task1()
    else:
        schedule(task == 3)
