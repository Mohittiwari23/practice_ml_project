import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    message = "Error occured in python script name [{0}] line no [{1}] error message [{2}] ".format(file_name, exc_tb.tb_lineno, str(error))
    return message

class CustomException(Exception):
    def __init__(self,message, error_detail:sys):
        super().__init__(message)
        self.error_detail = error_message_detail(message, error_detail=error_detail)

    def __str__(self):
        return self.error_detail

if __name__ == '__main__':
    try:
        a=1/0
    except Exception as e:
        logging.info("Division by Zero")
        raise CustomException(e,sys)
