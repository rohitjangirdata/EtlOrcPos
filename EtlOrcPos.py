import pandas as pd
import cx_Oracle
import psycopg2 as pg2
from sqlalchemy import create_engine
import numpy as np
from datetime import date
from datetime import datetime


def copytable_orcpsg_getlog():
    print('****Oracle DB details****')
    user_name_orc = input(str('User name: '))
    password_orc = input(str('Password: '))
    service_name = input(str('Service name: '))
    port_orc = input(str('Port: '))
    host_name_orc = input(str('Host: '))
    table_name_of_orcle = input(str('Table name want to copy: '))
    print('****Postgresql DB details****')
    user_name_pos = input(str('User name: '))
    password_pos = input(str('Password: '))
    data_base_name_pos = input(str('DataBase: '))
    port_pos = input(str('Port: '))
    host_name_pos = input(str('Host: '))
    print('----------------Processing-----------------')
    
    dsn = cx_Oracle.makedsn(host_name_orc, port_orc,service_name,)
    conn = cx_Oracle.connect(user= user_name_orc, password= password_orc, dsn=dsn)
    engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(user_name_pos,password_pos,host_name_pos,port_pos,data_base_name_pos))
    df_ora = pd.read_sql('SELECT * FROM {}'.format(table_name_of_orcle), con= conn)
    df_ora = df_ora.to_sql(table_name_of_orcle, engine, index = False, if_exists = 'append', chunksize=1000)
    
    table_copy = 'Table secessfully copy to postgresql Database'
    
    df_ora_count = pd.read_sql('SELECT COUNT(*) FROM {}'.format(table_name_of_orcle), con= conn)
    df_ora_count_row_count = int(df_ora_count.sum())
    
    pos_row_count = pd.read_sql('''SELECT COUNT(*) FROM "{}"'''.format(table_name_of_orcle), con =engine)
    df_pos_count_row_count = int(pos_row_count.sum())
    
    
    log_table_dict = {'oracle_DB':[table_name_of_orcle] ,'postgresql_BD':[table_name_of_orcle], 'rows_oracle':[df_ora_count_row_count],
       'rows_postgresql':[df_pos_count_row_count]}
    log_table =pd.DataFrame.from_dict(log_table_dict)
    
    return log_table
