import logging

try:
    import logtest
except ModuleNotFoundError:
    from configAndLogging import logtest


logging.basicConfig(level=logging.INFO)

logging.info('info')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('debug')

logtest.do_something()
