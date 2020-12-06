import json
import os

import colorlog
from colorlog import ColoredFormatter


def get_root_dir():
    root = os.path.dirname(os.path.abspath(__file__))
    for i in range(1):
        root = os.path.dirname(root)
    return root


def get_logger():
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )
    handler = colorlog.StreamHandler()
    handler.setFormatter(formatter)

    logger = colorlog.getLogger('logger')
    logger.addHandler(handler)
    return logger


def get_questions(index=0):
    questions_file = os.path.join(get_root_dir(), "res", "questions.json")
    if not os.path.isfile(questions_file):
        raise IOError(questions_file + " not found!")

    fd = open(questions_file, "r")
    questions_json = fd.read()
    fd.close()

    questions = json.loads(questions_json)
    return questions[index]

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


