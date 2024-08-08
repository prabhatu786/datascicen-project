import pandas as pd
import numpy as np
from sklearn.model_selection import  train_test_split
from src.DimondPricePrediction.exception import customexception
from src.DimondPricePrediction.logger import logging



class Dataingestion:
    def __init__(self):
        pass


    def Intiated_data_ingestion(self):
        logging.info("Intiated_data_ingestion")   
        try:
            data=pd.read_csv(path(os.path.join("notebook/data","train.csv")))
            logging.info("Data load succefully")
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train_test_split completed")


        except:
            pass 