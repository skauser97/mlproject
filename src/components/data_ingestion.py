# Student performer indicator
# Life cycle of ml
# 1. understanding prob statement
# 2. Data collection
# 3. Data checks to perform
# 4. EDA
# 5. Data preprocessing
# 6. Model training
# 7. Choose best model

# understands how students performance is affected by other variables, gender, ethnicity,
#  parental level of education, lunch, test prep curse

import os
import sys 
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # to create class variables

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")
    #op stored in folder, iput will b train.csv
    #inputs given data ingestion component, now this component
    #  knows where to save the train path, test path 
# inputs required in this component(train data, test data, raw data etc)
# will b creating in this class
# output can b anything like numpy array, file etc
# using decorator because u will be able to use class var directly in it, we dont have to use init
# in this component, anything which is req we give through this class
# using @data class cos we only defining var

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        # the above var will consist of the 3 values from dataingestion config
        # all 3 paths will be saved in this variable

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            # can read via api, mongodb etc 
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok= True)
            #inside make directories, combine dir path name ...getting dir name, 
            #exist ok= T,.. if it exists already, we dont have to delete it
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header= True)

            logging.info('Train test split initiated')
            train_set, test_set= train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header= True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header= True)
            # this is being saved in artefacts folder

            logging.info("Ingestion of the data is completed")   
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )                   
        
        except Exception as e:
            raise CustomException(e,sys)
        # if data stored in database, u have to write code to read from db
        # eg , create mongodb client in utils.py and then read it


# initate and run this

if __name__ == "__main__":
    obj= DataIngestion()
    obj.initiate_data_ingestion()


