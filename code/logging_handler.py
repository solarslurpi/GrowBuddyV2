import inspect
import logging
import sys



class LoggingHandler:

    def __init__(self,log_level=logging.DEBUG):

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


    def debug(self,message):
        f = inspect.currentframe()
        i = inspect.getframeinfo(f.f_back)        
        self.logger.debug(f'{i.filename}:{i.lineno}  {i.function}   ...{message}')


    def info(self,message):
        f = inspect.currentframe()
        i = inspect.getframeinfo(f.f_back)
        self.logger.info(f'{i.filename}:{i.lineno}  {i.function}   ...{message}')