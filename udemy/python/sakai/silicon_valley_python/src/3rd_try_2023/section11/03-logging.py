import logging

logging.basicConfig(
    filename='test.log',
    level=logging.WARNING
)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')