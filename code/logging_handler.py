import inspect
import logging
import os
import sys



class LoggingHandler:

    def __init__(self,log_level=logging.DEBUG):
        # set DEBUG for everything
        # In the docs: https://docs.python.org/3/library/logging.html
        # 16.6.7 Talks about LogRecord Attributes.  I am using this to
        # provide date/time info...i tried a few others to get stack
        # info, however returned info on this module.  So used inspect.
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        # next line is for reference.
        # logging.basicConfig(filename=logfile, level=logging.DEBUG,
        #                     format='%(asctime)s %(levelname)s  %(message)s',
        #                     datefmt='%b %-d,%Y %H:%M:%S')

    # def _make_message(self, message):
    #     # getting to the caller's caller since
    #     # this function is called from within
    #     (filepathname, line_number, name, lines, index) = inspect.getframeinfo(sys._getframe(2))
    #     code_info_str = ": {} - {} - {} : ".format(os.path.basename(filepathname), line_number, name)
    #     return (code_info_str + message)

    # def debug(self, message):
    #     self.logger.debug(self._make_message(message))

    def debug(self,message):
        f = inspect.currentframe()
        i = inspect.getframeinfo(f.f_back)        
        self.logger.debug(f'{i.filename}:{i.lineno}  {i.function}   ...{message}')

    # def info(self, message):
    #     self.logger.info(self._make_message(message))

    def info(self,message):
        f = inspect.currentframe()
        i = inspect.getframeinfo(f.f_back)
        self.logger.info(f'{i.filename}:{i.lineno}  {i.function}   ...{message}')