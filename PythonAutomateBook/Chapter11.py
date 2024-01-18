#! python
import logging
# raise Exception("This is a test to see what kind of error message that will display here.")

ages = [1,2,3,4,5,6,7,8,9,10]
assert ages[0] < ages[-1] # nothing happens here

# assert ages[0] > ages[-1] # stops the program and returns the following traceback

# Traceback (most recent call last):
#   File "c:\Users\richa\OneDrive\Documents\Python\PythonAutomateBook\Chapter11.py", line 4, in <module>
#     assert ages[0] > ages[-1]
# AssertionError
logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s- %(message)s')
logging.debug('start')

# for items in ages:
#     print(items)
#     logging.debug(f'items is {items}')
# any log messages after this will not be shown
logging.disable(logging.CRITICAL)

logging.debug('this is a debug message')
logging.info("this is a log info")
logging.warning('this is a warning message')
logging.error('this is an error message')
logging.critical('this is a critical message')

