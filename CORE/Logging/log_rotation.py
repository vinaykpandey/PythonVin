import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

logFile = 'log_rotation.log'

my_handler = RotatingFileHandler(
    logFile,
    mode='a',
    maxBytes=5 * 1024 * 1024,
    backupCount=10,
    encoding=None,
    # delay=0
)
stdout_handler = logging.StreamHandler()
stdout_handler.setFormatter(log_formatter)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.DEBUG)
app_log = logging.getLogger("log_rotation")
app_log.setLevel(logging.DEBUG)
app_log.addHandler(my_handler)
app_log.addHandler(stdout_handler) # print on screeen

i = 1
while True:
    i *= 100000000000000000000
    app_log.debug("debug data  {}".format(i))
    # app_log.info("info data {}".format(i))
    # app_log.warning("warning data {}".format(i))
    # app_log.error("warning data {}".format(i))
    # app_log.critical("warning data {}".format(i))
