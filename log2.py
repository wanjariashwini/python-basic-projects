#https://stackoverflow.com/questions/44718204/python-how-to-create-log-file-everyday-using-logging-module
#https://tutorialedge.net/python/python-logging-best-practices/

import logging
import logging.handlers as handl

logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

## Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logHandler = handlers.TimedRotatingFileHandler('normal.log', when='M', interval=1, backupCount=0)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)

errorLogHandler = handlers.RotatingFileHandler('error.log', maxBytes=5000, backupCount=0)
errorLogHandler.setLevel(logging.ERROR)
errorLogHandler.setFormatter(formatter)

logger.addHandler(logHandler)
logger.addHandler(errorLogHandler)

def main():
    while True:
        time.sleep(1)
        logger.info("A Sample Log Statement")
        logger.error("An error log statement")

main()


from logging.handlers import TimedRotatingFileHandler
logname = "my_app.log"
handler = TimedRotatingFileHandler(logname, when="midnight", interval=1)
handler.suffix = "%Y%m%d"
logger.addHandler(handler)



"""