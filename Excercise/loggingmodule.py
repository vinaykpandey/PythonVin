#!/usr/bin/python
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
