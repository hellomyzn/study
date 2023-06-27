import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

h = logging.FileHandler('logtest3.log')
logger.addHandler(h)

def do_something():
    logging.info('from logtest info')
    logger.info('from logtest')
    logger.debug('from logtest debug')
