###
# Main
###

import argparse
import sys
import inspect

from src import __version__, __project__, __author__
from src import tasks


def parse_arguments():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser(__project__)
    parser.add_argument('--version', '-v', action='version', version=f'%(prog)s: {__version__}, '
                                                                     f'Author: {__author__}')
    all_functions = [x for x, a in inspect.getmembers(sys.modules['src.tasks']) if inspect.isclass(a)]
    parser.add_argument('--task-class', '-tc', type=str,
                        help=f'choose class {all_functions}')
    args = parser.parse_args()
    if args.task_class not in all_functions:
        raise Exception(f'task_class not in {all_functions}')
    return args


def main():
    args = parse_arguments()

    print('###############################################')
    print(f'Scrapper: Task Initiated ------- {args.task_class}')
    print('###############################################')

    getattr(tasks, args.task_class)()\
        .process().output()

    print('###############################################')
    print(f'Task completed -------- {args.task_class}')
    print('###############################################')


if __name__ == '__main__':
    main()
