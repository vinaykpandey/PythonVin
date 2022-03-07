from log_in_file import logger


class Car:

    def __init__(self):
        self.name = "Audi"
        self.model = "A4"


car = Car()
logger.info(f" car name is {car.name}")
