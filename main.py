from networksecurity.components.data_ingestion import DataIngestion

from networksecurity.exception.exception import NetworkSecurityException

from networksecurity.mylog.logger import logging
import sys

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


if __name__=='__main__':
     try:
           trainingpipelineconfig=TrainingPipelineConfig()
           dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
           data_ingestion=DataIngestion(dataingestionconfig)
           logging.info("initiate the the data ingestion")
           dataingestionartifact=data_ingestion.initiate_data_ingestion()
           print(dataingestionartifact)
         
         
     except Exception as e:
            raise NetworkSecurityException(e,sys)