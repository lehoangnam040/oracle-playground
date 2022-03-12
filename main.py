import sys
import getopt
from config import logger
import logging
import csv
import pandas as pd
import argparse

from db.appid import AppID, _metadata, engine


def main(argv):
    
    
    # read excel to iterator
    # df = pd.read_excel(argv['inputfile'], sheet_name='User Report Template', dtype=str, header=[0], 
    #                            usecols=['ExportDateTime', 'ApplicationID', 'AccountID', 'Name'])
    
    with engine.connect() as connection:
        
        
        
        # for index, row in df.iterrows():
        #     row_dict = row.to_dict()
        #     # print(row_dict)
        #     connection.execute(
        #         AppID.insert().values(
        #             # id=index+1,
        #             export_date_time=row_dict.get('ExportDateTime'),
        #             application_id=row_dict.get('ApplicationID'),
        #             account_id=row_dict.get('AccountID'),
        #             customer_name='namlh',
        #         )
        #     )
            
    # for loop and run each item to save on DB

if __name__ == '__main__':
    logger.setup_logging(__name__)
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--inputfile', metavar='i', type=str,
                    help='an integer for the accumulator', required=True)
    
    main(vars(parser.parse_args()))
