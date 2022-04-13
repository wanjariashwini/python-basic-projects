
import logging

logging.basicConfig(filename ="log.txt", level = logging.WARNING, filemode = "a")

print("Logging information started")
logging.debug('debug information')
logging.error('error information')
logging.critical('critical information')
logging.warning('warning information')
logging.info('info information')

