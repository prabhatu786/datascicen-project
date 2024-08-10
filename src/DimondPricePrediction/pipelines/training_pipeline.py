import os
import pandas as pd
import numpy as np
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.components.data_ingestion import DataIngestion
from src.DimondPricePrediction.exception import customexception

obj=DataIngestion()
obj.Intiated_data_ingestion()

