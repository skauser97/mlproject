# exception handling

# common for entire code. we going to use in try catch block

import sys
#import logging
from src.logger import logging
# sys lib  =manipulates diff part in runtime
# ie will have info on exceptions

def error_message_detail(error, error_detail:sys): # error_detail will be within sys
    _,_,exc_tb = error_detail.exc_info()
    # exc_tb gives info in which file and line we r getting exception
    file_name = exc_tb.tb_frame.f_code.co_filename # in documentation custom exception handling

    error_message = 'Error occured in python script name [{0}] line [{1}] error msg{2}'.format
    (
        file_name, exc_tb.tb_lineno, str(error))

    return error_message
    

class CustomException( Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message) # inheriting from the parent exception
        self.error_message = error_message_detail(error_message, error_detail=error_detail)# error detail traced by sys

    def __str__(self): #inheriting another function in custom exception
        return self.error_message # when we raise exception we will print here
    
    # when we print this, we will get error msg




# whenever we get exception , we tae that exceptionlogging it logger file and 
# use logging.info to put inside file
'''
if __name__ == "__main__":
    try:
        a =1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys)

      '''  





