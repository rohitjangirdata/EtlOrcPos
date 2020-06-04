Readme
=======
This library help you to copy your data(Table wise) from Oracle Database to Postgresql Database. Its useful to those how are not friendly to ETL (Extract Transform load) and database connection, So I try to make it user friendly. 

>Following librarys are use :
```sh
import pandas as pd
import numpy as np
import cx_Oracle
from sqlalchemy import create_engine
```
Connection Details
---------------------------
> **Note:** All credentials of Database connection should me correct.

Have to provide all credentials for the connection like User name , password and Host etc. for both the database and also provide table name which you want to copy from Oracle DB to Postgresql DB, after providing all credentials get pandas dataframe having table name and count of rows in table as output .

How to use code
-----------------------

```sh
from EtlOrcPos import copytable_orcpsg_getlog
```
After getting the EtlOrcPos library ,then just call the function 
```sh
copytable_orcpsg_getlog()
```
Then function ask for input for all credentials needed for connection to Databases

> **Note:** Libraries like **cx_Oracle** and **sqlalchemy** are very powerful so can be use  alone for ETL job.