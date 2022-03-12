import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, MetaData, Sequence
import sqlalchemy
from sqlalchemy import create_engine
from config.db import ENGINE_PATH_WIN_AUTH
_metadata = MetaData()
engine = create_engine(ENGINE_PATH_WIN_AUTH)
    
AppID = Table(
    'app_id', _metadata, 
    sqlalchemy.Column('id', sqlalchemy.Integer,  sqlalchemy.schema.Identity(start=1), primary_key=True ),
    Column('export_date_time', String(256), nullable=True),
    Column('application_id', String(256), nullable=True),
    Column('account_id', String(256), nullable=True),
    Column('customer_name', String(256), nullable=True),
    autoload=True,
    autoload_with=engine,
    schema='SYSTEM',
)