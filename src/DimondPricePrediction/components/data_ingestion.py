import os
import pandas as pd
import numpy as np
import sys
from sklearn.model_selection import  train_test_split
from src.DimondPricePrediction.exception import customexception
from src.DimondPricePrediction.logger import logging

class DataIngestionConfig:
    raw_data_path:str= os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config =DataIngestionConfig()
        


    def Intiated_data_ingestion(self):
        logging.info("Intiated_data_ingestion")   
        try:
            data=pd.read_csv(os.path(os.path.join("notebook/data","train.csv")))
            logging.info("Data load succefully")

            os.makedirs(os.path.join(self.ingestion_config.raw_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("raw data save succefully  in artifacts folder")

            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train_test_split completed")

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("Data Ingestion part succefully completed")



        except Exception as e:
            logging.info(" Exceptin has been occured during Data Ingestion Stage")
            raise customexception(e,sys)
