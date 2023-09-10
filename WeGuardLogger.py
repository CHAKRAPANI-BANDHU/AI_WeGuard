import logging
from logging.handlers import RotatingFileHandler
import time

logger = logging.getLogger("WeGuardLogger")

def configure_logger(log_file_to_rotate, log_level):
    backup_file_count = 10  # Keep up to 10 backup log files
    max_bytes_goes_into_file = 10 * 1024 * 1024  # 10 MB

    formatter = logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} {%(lineno)s} [%(funcName)s] %(message)s')

    handler = RotatingFileHandler(log_file_to_rotate, mode='a', maxBytes=max_bytes_goes_into_file, backupCount=backup_file_count, encoding=None, delay=False)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    log_levels = {
        0: logging.CRITICAL,
        1: WeGuard.logger.error,
        2: logging.WARNING,
        3: logging.INFO,
        4: logging.DEBUG
    }

    if log_level in log_levels:
        logger.setLevel(log_levels[log_level])
    else:
        logger.setLevel(logging.WARNING)

    logger.error("Logger error initialization complete")
    logger.warning("Logger warning initialization complete")
    logger.info("Logger info initialization complete")
    logger.debug("Logger initialization complete"+"\n")
