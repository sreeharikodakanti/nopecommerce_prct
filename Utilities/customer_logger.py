import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation_1.log",format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt= "%d-%m-%Y : %I%M%S  :%P")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger