import logging
import sys
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

logging.basicConfig(filename="test.log", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)-8s %(name)-15s %(message)s")


# create logger
logger = logging.getLogger("vinay_log")
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
output_file_handler = logging.FileHandler("vinay_output.log")
stdout_handler = logging.StreamHandler()
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to stdout_handler, output_file_handler
stdout_handler.setFormatter(formatter)
output_file_handler.setFormatter(formatter)
logger.addHandler(output_file_handler)
logger.addHandler(stdout_handler)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def div(x, y):
    return x / y


num1 = 20
num2 = 4

add_res = add(num1, num2)
logger.debug("Add: {} + {} = {} ".format(num1, num2, add_res))

add_res = add(num1, num2)
logger.info("Add: {} + {} = {} ".format(num1, num2, add_res))

sub_res = subtract(num1, num2)
logging.warning("Sub: {} - {} = {} ".format(num1, num2, sub_res))

mul_res = multiply(num1, num2)
logging.error("Multiply: {} * {} = {} ".format(num1, num2, mul_res))

div_res = div(num1, num2)
logging.critical("Div: {} * {} = {} ".format(num1, num2, div_res))
