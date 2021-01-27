"""
Level	NumericValue	Function	Used to
DEBUG	10	logging.debug()	Diagnose problems, show detailed information
INFO	20	logging.info()	Confirm that things are working as expected
WARNING	30	logging.warning()	Indicate something unexpected happened, or could happen (default)
ERROR	40	logging.error()	Show a more serious problem
CRITICAL 50	logging.critical()	Show a serious error, the program may be unable to continue running

The logging module sets the default level at WARNING, so WARNING, ERROR,
and CRITICAL will all be logged by default. In the example above,
we modified the configuration to include the DEBUG level with the following code:


a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)

output_file_handler = logging.FileHandler("output.log")
stdout_handler = logging.StreamHandler(sys.stdout)

a_logger.addHandler(output_file_handler)
a_logger.addHandler(stdout_handler)

"""

https://www.toptal.com/python/in-depth-python-logging

https://www.datadoghq.com/blog/python-logging-best-practices/