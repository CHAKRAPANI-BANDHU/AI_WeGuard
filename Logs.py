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
    backup_file_count = 5  # Number of backup log files to keep (adjust as needed)
    max_bytes_goes_into_file = 10 * 1024 * 1024  # About 10 MB (adjust as needed)

    # Ref for all logging params: https://docs.python.org/3/library/logging.html#logging.Formatter
    formatter = logging.Formatter(
        '%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} {%(lineno)s} [%(funcName)s] %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S')

    handler = RotatingFileHandler(log_file_to_rotate, mode='a', maxBytes=max_bytes_goes_into_file,
                                  backupCount=backup_file_count, encoding='utf-8')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if logLevel == 0:
        logger.setLevel(logging.CRITICAL)
    elif logLevel == 1:
        logger.setLevel(logging.ERROR)
    elif logLevel == 2:
        logger.setLevel(logging.WARNING)
    elif logLevel == 3:
        logger.setLevel(logging.INFO)
    elif logLevel == 4:
        logger.setLevel(logging.DEBUG)

    logger.error("Logger error initialization complete")
    logger.warning("Logger warning initialization complete")
    logger.info("Logger info initialization complete")
    logger.debug("Logger initialization complete")


if __name__ == "__main__":
    log_file = "WeGuard_" + time.strftime("%d-%m-%Y_%H:%M:%S") + ".log"
    rotate_log_file(log_file, globalsvar.loglevel)
    