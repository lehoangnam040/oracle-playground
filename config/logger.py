import logging
import sys  
from datetime import datetime

class ExactLogLevelFilter(object):  
    def __init__(self, level):    
        self.__level = level
        
    def filter(self, logRecord):    
        return logRecord.levelno == self.__level
    
    
def setup_logging(logger_name):  
    utc_now = datetime.utcnow()
    formatter = logging.Formatter('%(levelname)s %(asctime)s %(module)s:%(lineno)s %(message)s', datefmt="%Y/%m/%d %H:%M:%S"  ) 
    
    logging.getLogger(logger_name).setLevel(logging.DEBUG) # This must be as verbose as the most verbose handler  
    
    debug_logging = logging.FileHandler('logs/debug_{:%Y%m%d}.log'.format(utc_now))  
    debug_logging.setLevel(logging.DEBUG)  
    debug_logging.setFormatter(formatter)  
    debug_logging.addFilter(ExactLogLevelFilter(logging.DEBUG))  
    logging.getLogger(logger_name).addHandler(debug_logging)
    
    info_logging = logging.FileHandler('logs/info_{:%Y%m%d}.log'.format(utc_now))  
    info_logging.setLevel(logging.INFO)  
    info_logging.setFormatter(formatter)  
    info_logging.addFilter(ExactLogLevelFilter(logging.INFO))  
    logging.getLogger(logger_name).addHandler(info_logging)
    
    warn_logging = logging.FileHandler('logs/warn_{:%Y%m%d}.log'.format(utc_now))  
    warn_logging.setLevel(logging.WARN)  
    warn_logging.setFormatter(formatter)  
    warn_logging.addFilter(ExactLogLevelFilter(logging.WARN))  
    logging.getLogger(logger_name).addHandler(warn_logging)
    
    error_logging = logging.FileHandler('logs/error_{:%Y%m%d}.log'.format(utc_now))  
    error_logging.setLevel(logging.ERROR)  
    error_logging.setFormatter(formatter)  
    logging.getLogger(logger_name).addHandler(error_logging)
    
    
    stdout_logging = logging.StreamHandler(sys.stdout)  
    stdout_logging.setLevel(logging.DEBUG)  
    stdout_logging.setFormatter(formatter)  
    logging.getLogger(logger_name).addHandler(stdout_logging)