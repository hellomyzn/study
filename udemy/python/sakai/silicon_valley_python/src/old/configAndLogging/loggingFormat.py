import logging


formatter = '%(levelname)s:%(message)s'

logging.basicConfig( level=logging.INFO, format=formatter)
logging.info('info %s %s', 'test', 'test2')

formatter = '%(asctime)s:%(message)s'

logging.basicConfig( level=logging.INFO, format=formatter)
logging.info('info %s %s', 'test', 'test2')
