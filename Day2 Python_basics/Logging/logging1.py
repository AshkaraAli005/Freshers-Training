import logging
logging.basicConfig(level=logging.DEBUG, filename='new.log',filemode='w',format='%(levelname)s : %(name)s : %(asctime)s : %(message)s', datefmt='%d-%m-%y %H:%M:%S')
a=10
b=7
c=a+b
logging.debug(f'Addition of {a} and {b} is {c}')

logging.info('User has logged out.. ')

logging.warning('Warning Message....')
try:
    10/0
except Exception as e:
    logging.error('"This is Error message.."',exc_info=e)
    
logging.critical('This is a Critical Message')