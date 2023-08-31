import logging
from logging.handlers import RotatingFileHandler
import time
import globalvariables as globalsvar

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client

logger = logging.getLogger("requests.packages.urllib3")


def rotate_log_file(log_file_to_rotate, logLevel):
    backup_file_count = 99  # keep files with extensions .1, .2 .. to .99. After that discard the last and rename recursively etc.
    max_bytes_goes_into_file = 99999999  # About 100 mb

    # Ref for all logging params: https://docs.python.org/2/library/logging.html
    formatter = logging.Formatter(
        '%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} {%(lineno)s} [%(funcName)s] %(message)s')

    handler = RotatingFileHandler(log_file_to_rotate, mode='a', maxBytes=max_bytes_goes_into_file,
                                  backupCount=backup_file_count, encoding=None, delay=False)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if logLevel == 0:
        logger.setLevel(logging.CRITICAL)
        logging.basicConfig(
            format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
            datefmt='%d-%m-%Y_%H:%M:%S', level=logging.CRITICAL)
    if logLevel == 1:
        logger.setLevel(logging.ERROR)
        logging.basicConfig(
            format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
            datefmt='%d-%m-%Y_%H:%M:%S', level=logging.ERROR)
    if logLevel == 2:
        logger.setLevel(logging.WARNING)
        logging.basicConfig(
            format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
            datefmt='%d-%m-%Y_%H:%M:%S', level=logging.WARNING)
    if logLevel == 3:
        logger.setLevel(logging.INFO)
        logging.basicConfig(
            format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
            datefmt='%d-%m-%Y_%H:%M:%S', level=logging.INFO)
    if logLevel == 4:
        logger.propagate = True
        logger.setLevel(logging.DEBUG)
        logging.basicConfig(
            format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
            datefmt='%d-%m-%Y_%H:%M:%S', level=logging.DEBUG)
    logger.error("Logger error initalization complete")
    logger.warning("Logger warning initalization complete")
    logger.info("Logger info initalization complete")
    logger.debug("Logger initalization complete")


if __name__ == "__main__":
    log_file = "WeGuard" + format(time.strftime("%d-%m-%Y_%H:%M:%S")) + ".log"
    rotate_log_file(log_file, globalsvar.loglevel)
