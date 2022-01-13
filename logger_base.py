import logging

logger = logging

logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%I:%M:%S %p',
                   handlers=[
                       logging.FileHandler('logFile.log'),
                       # logging.StreamHandler()
                   ])

if __name__ == '__main__':
    logging.warning('warning level message')
    logging.info('info level message')
    logging.debug('debug level message')
    logging.error('error level message')
