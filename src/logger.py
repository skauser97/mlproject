# any execution happens will be logged in files, so that it may be tracked in files

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # text file
logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(logs_path, exist_ok= True) #says even though there is a file , it will keep on appending files

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

#override functionality of logging
# set up in basic config

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO, #print specific msgs
    # #logging setup. wherever u use logging.info, import logging
    # write out any print msg..will this basic config
    # and is ging to create this file path
)

# whenever we get exception we log it with logger file and use logging logging.INFO to put it inside file
'''
if __name__ == "__main__":
    logging.info("Logging has started")
    # was done to check if its working 
    python src/logger.py

'''