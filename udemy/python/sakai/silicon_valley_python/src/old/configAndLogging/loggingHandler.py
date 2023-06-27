import logging

try:
    import logtest2
except ModuleNotFoundError:
    from configAndLogging import logtest2


logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.debug('debug')

logtest2.do_something()
