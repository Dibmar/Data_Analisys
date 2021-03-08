# Needed for stablishing connection with database and queries
import json
import pymysql
import psycopg2
from sqlalchemy import create_engine
import sys

# For data export as csv and/or dataframe
import pandas as pd


class MySQL_manager(object):
    """
    This class has been created to establish a connection with a MySQL server database. For this it uses:
        
        - The json library
        - The pymysql library
        - The slalchemy/create_engine library
        - The pandas library

    This class can make queries in MySQL and return the results as a dataframe for further exploration.
    """
    def __init__(self, path):
        self.path = path


    def json_to_dict(self):
        """
                            ---What it does---
        Loads a json file and turns it into a dictionary.
                            
                            ---What it needs---
            - The path to the file (path) in string format
        
                            ---What it returns---
        A dictionary (settings) with the contents of the json loaded
        """
        try:
            with open(self.path, 'r+') as outfile:
                settings = json.load(outfile)
                
                return settings
            
        except Exception as error:
            raise ValueError(error)


    # For connecting your Database
    def CREATE_a_MySQL_db(self):
        """
                            ---What it does---
        This function creates a MySQL database for use in a Python enviroment.
        Using a json file to connect to a MySQL server stored in AWS. 
                            
                            ---What it needs---
            - MySQL library for Python
            - A path to the settings (path) in string format
                + The settings file should be a json file
                            
                            ---What it returns---
        This function returns a MySQL database ready for connection
        """

        try:
            with open(self.path, 'r+') as outfile:
                settings = json.load(outfile)
                

            self.IP_DNS = settings["IP_DNS"]
            self.USER = settings["USER"]
            self.PASSWORD = settings["PASSWORD"]
            self.DATABASE = settings["BD_NAME"]
            self.PORT = settings["PORT"]

            self.connection = pymysql.connect(host=self.IP_DNS, user=self.USER, 
                                    password=self.PASSWORD, database=self.DATABASE, 
                                    port=self.PORT)
            
            self.cursor = self.connection.cursor()
            
            # self.engine = create_engine(f'mysql+pymysql://user:{self.USER}/DB?local_infile=1') 
            
            print(f"Connected to MySQL server {self.DATABASE}")
                                            
            return self.connection, self.cursor
       
        except Exception as error:
            raise ValueError(error)        


    # Quick oders for your database
    def ORDER_show_tables (self):
        """
                            ---What it does---
        Shows the tables in your database
        """
        result = self.cursor.execute("SHOW TABLES")
        tables = self.cursor.fetchall()
        table_list = [table for table in tables]

        self.table_dict = {}

        for item in range(result):
            self.table_dict[item] = table_list[item][0]
            print(f'{item}: {self.table_dict[item]}')

        return self.table_dict


    def ORDER_describe_table (self, table):
        """
                            ---What it does---
        Describes a table in your database
        """
        
        self.cursor.execute(f"DESCRIBE {table}")
        data = [detail for detail in self.cursor.fetchall()]

        name = []
        d_type = []
        default_v = []
        nullable = []
        prim_k = []
        collation =[]

        for d in data:
            name.append(d[0])
            d_type.append(d[1])
            nullable.append(d[2])
            prim_k.append(d[3])
            default_v.append(d[4])
            collation.append(d[5])

        self.table_data = pd.DataFrame({'name': name, 'data_type': d_type, 'nullable': nullable,
                                        'primary_key': prim_k, 'default_value': default_v, 'collation': collation})
        print(self.table_data)
    

    def ORDER_drop_if_already_exists (self, table):
        """
                            ---What it does---
        Drops the table in your database if it already exists
                            ---What it needs---
            - Name of your table (table). 
        """
        self.cursor.execute(f"DROP TABLE IF EXISTS {table}")


    def ORDER_join_tables (self, table, table_2, on, selection= '*', how= 'inner'):
        """
                            ---What it does---
        Joins the selected tables in your database on the column of your choice, selection and method.

                            ---What it needs---
            - Names of your tables (table, table_2) in  string format.
            - The column to join on (on) in string format.
            - Your selection (selection), by default set to '*'.
            - The method of join (how), by default set to 'inner'.
        """
        if how == 'left' or how == 'LEFT':
            self.command = f"""SELECT {selection} 
                FROM {table} 
                LEFT JOIN {table_2} ON {on};"""
        
        elif how == 'right' or how == 'RIGHT':
            self.command = f"""SELECT {selection} 
                FROM {table} 
                RIGHT JOIN {table_2} ON {on};"""

        elif how == 'inner' or how == 'INNER':
            self.command = f"""SELECT {selection} 
                FROM {table} 
                INNER JOIN {table_2} ON {on};"""

        elif how == 'full' or how == 'FULL':
            self.command = f"""SELECT {selection} FROM {table}
                    LEFT JOIN {table_2} ON {on}
                    UNION
                    SELECT {selection} FROM {table_2}
                    LEFT JOIN {table} ON {on}"""

        self.cursor.execute(f"{self.command}")


    def ORDER_insert_into_table(self, table, columns, values):
        """
                            ---What it does---
        This function adds data to a given table using MySQL INSERT INTO statement, printing the query.
        
        ---What it needs---
            - The name of the (table)
            - The columns of the table (columns). It should be in string format.
                * In this format -> "(col_1, col_2)"
            - The values to insert. It should be in string format.
                * In this way -> "(val_1, val_2), (val_3, val_4);"
            BOTH table and values MUST coincide in order!

        ---What it returns---
        This function does not return anything
        """
        
        query = f"INSERT INTO {table} {columns} VALUES {values};"
        print(query)

        self.cursor.execute(query)


    def ORDER_create_a_df_from_sql(self, query= None, return_file= True, store= False, name= 'my_file', destination='Output/'):
        """
                            ---What it does---
        Creates a dataframe from a given sql table and returns it and/or saves it locally.
        This table must be generated through a MySQL query.

                            ---What it needs---
            - A valid MySQL query (query). It should be in string format.
            - A boolean value
            - A boolean value (store) if you wish to save the dataframe in csv format locally. Set to False by default.
            - The name of the file to save (name) it should be in string format. Set to 'my_file' by default.
            - The directory to be saved in (destination). It should be in string format end with '/'. Set as 'Output/' by default.
        
                            ---What it returns---
        This function returns a dataframe object
        """
        self.df = pd.read_sql(query, con= self.connection)

        if return_file == True and store == False:
    
            return self.df
        
        elif return_file == True and store == True:
            self.name = f'{name}.csv'

            if destination.endswith('/'):
                self.stored_in = f'{destination}{self.name}'
            
            else:
                self.stored_in = f'{destination}/{self.name}'

            print(f'The file will be stored as "{name}"  in {destination}...')
            self.df.to_csv(self.stored_in)

            return self.df


    def ORDER_select_all_from (self, table):
        """
                            ---What it does---
        This function prints all available data in dataframe format.
        
                            ---What it needs---
            - The name of the (table)
            
                            ---What it returns---
        This function does not return anything
        """

        query = f'SELECT * FROM {table}'
        
        table =  pd.read_sql(query, con= self.connection)

        print(table)


    def ORDER_custom_query(self, query):
        """
                            ---What it does---
        This function executes a custom query. Then prints it.

                            ---What it needs---
            - A query in string format and in the proper sintax

                            ---What it returns---
        This function does not return anything
        """
        print(query)
        self.cursor.execute(query)


    def ORDER_load_data_infile(self, dataframe, table, delimiter= ',', new_line= '\\r\\n'):
        """
                            ---What it does---
        This function executes the LOAD DATA INFILE query. Allowing the user to review it as a safeguard before execution.
        
                            ---What it needs---
            - A dataframe to load into (dataframe)
            - A table to load the data in
            Needless to say, both need to coincide in both number and name of columns

                            ---What it returns---
        This function does not return anything
        """
        
        query = (f"""
            LOAD DATA LOCAL INFILE 
            INTO TABLE {table} 
            COLUMNS TERMINATED BY {delimiter} 
            LINES TERMINATED BY {new_line}
            IGNORE 1 LINES
            {tuple(dataframe.columns)}
            ;""")
        
        print(query)

        choice = input('Do you wish to execute? y/n> ')

        if choice == 'y' or choice == 'Y':
            print('Executing query')
            self.cursor.execute(query)
        
        else:
            print('Quitting')


    def ORDER_close(self):
        """
                                ---What it does---
        Closes conection with your database
        """

        print(f"Closing connection connection with MySQL server...")
        self.cursor.close()
        self.connection.close()


class Postgre_SQL_manager(MySQL_manager):
    """
    This class has been created to establish a connection with a Postgre SQL database. For this it uses:
        
        - The json library
        - The psycopg2 library
        - The slalchemy/create_engine library
        - The pandas library
        - The MySQL_manager (parent class)

    This class can make queries in Postgre SQL and return the results as a dataframe for further exploration.
    """

    def __init__(self, path):
        self.path = path


    def CREATE_a_postgre_db (self):
        """
                            ---What it does---
        This function creates a postgre SQL database connection with Python.

                            ---What it needs---
            - This function needs access to a json with the connection settings (self.path)

                            ---What it returns---
        This function returns the cursor object.
        """
                
        try:
            with open(self.path, 'r+') as outfile:
                settings = json.load(outfile) 
                    
            localhost = settings['localhost']
            user = settings['user']
            password = settings['password']
            dbname = settings['dbname']

            try:
                self.conection = psycopg2.connect(f"host={localhost} dbname= {dbname} user= {user} password= {password}")   
                self.cursor =  self.conection.cursor()

                return self.cursor

            except psycopg2.DatabaseError:
                if self.conection:
                    self.conection.rollback()
                
                print ('Error %s' % psycopg2.DatabaseError)  
                sys.exit(1)
                        
        except Exception as error:
            raise ValueError(error)


