import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter)

logger.addHandler(ch)
