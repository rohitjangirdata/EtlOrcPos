Readme
=======
This library help you to copy your data(Table wise) from Oracle Database to Postgresql Database. 

>Following libraries are used :
```sh
import pandas as pd
import numpy as np
import cx_Oracle
from sqlalchemy import create_engine
```
Connection Details
---------------------------
> **Note:** All credentials of Database connection should be correct.

You have to provide all credentials for the Database connection (i.e. User name, password, Host, IP) .Also needed table name which you want to copy from Oracle DB to Postgresql DB, after that you will get pandas dataframe including table name and number of rows in the log table.

How to use 
---------------
```sh
pip install etlorcpos
```
```sh
from EtlOrcPos import copytable_orcpsg_getlog
``` 
```sh
copytable_orcpsg_getlog()
```
Then function ask for input for all credentials needed for connection to Databases

> **Note:** Libraries like **cx_Oracle** and **sqlalchemy** are very powerful so can be use  alone for ETL job.
