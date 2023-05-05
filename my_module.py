# my_module.py
import numpy as np
import pandas as pd

def main():
    pass


########## Read CSV file ##########################
def read_csv_file(file_name:str):
    pd.read_csv(file_name)


######### Data Processing #########################

#Get variable dtypes 
def info(dataframe=str):           
    dataframe.info()      


#Drop columns from DF 
def drop_from_df(dataframe,*columns):       ## *col represents a variable number of columns
    dataframe = dataframe.drop(columns= list(columns)) # *columns argumentreturn tuples therefore list(col) converts the items into a list.
    return dataframe






if __name__ == '__main__':
    main()



    

