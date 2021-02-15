import json
import pymysql
from sqlalchemy import create_engine
import pandas as pd


class SQL_manager(object):

    def __init__(self, path):
        self.path = path

    def gimmie_a_db(self):
        """
                            ---What it does---
        This function creates a MySQL database for use in a Python enviroment.
        Using a json file to connect to a MySQL server stored in AWS. 
                            
                            ---What it needs---
            - MySQL library for Python
            - A path to the settings (path) in string format
                            
                            ---What it returns---
        This function returns a MySQL database ready for connection
        """

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
                    self.settings = json.load(outfile)
                    
                    return self.settings
                
            except Exception as error:
                raise ValueError(error)


        def creator (self):
            """
                                ---What it does---
            Creates a MySLQ database and returns it.
                                
                                ---What it needs---
                -The connection settings (settings) in dictionary format
                                
                                ---What it returns---
            A MySQL database ready to connect.
            """

            self.IP_DNS = self.json_readed["IP_DNS"]
            self.USER = self.json_readed["USER"]
            self.PASSWORD = self.json_readed["PASSWORD"]
            self.DATABASE = self.json_readed["BD_NAME"]
            self.PORT = self.json_readed["PORT"]

            self.sql_db = pymysql.connect(host=self.IP_DNS, user=self.USER, 
                                    password=self.PASSWORD, database=self.DATABASE, 
                                    port=self.PORT)
            
            self.cursor = self.sql_db.cursor()
            
            print(f"Connected to MySQL server {self.DATABASE}")
                                            
            return self.sql_db

        self.settings = json_to_dict(self)
        self.sql_db = creator(self)

        return self.sql_db

    # Quick oders for your database
    def ORDER_show_tables (self):
        """
                            ---What it does---
        Shows the tables in your database
        """
        self.sql_db.execute_interactive_sql(sql="SHOW TABLES")


    def ORDER_describe_table (self, table):
        """
                            ---What it does---
        Describes a table in your database
        """
        self.sql_db.execute_interactive_sql(sql=f"DESCRIBE {table}")


    def ORDER_drop_if_already_exists (self, table):
        """
                            ---What it does---
        Drops the table in your database if it already exists
                            ---What it needs---
            - Name of your table (table). 
        """
        self.sql_db.execute_interactive_sql(sql=f"DROP TABLE IF EXISTS {table}")


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

        self.sql_db.execute_interactive_sql(sql=f"{self.command}")


    def ORDER_create_a_df_from_sql(self, query):
        self.df = pd.read_sql(query, con=self.sql_db)

        return self.df


    def ORDER_close(self):
        """
                                ---What it does---
        Closes conection with your database
        """

        print(f"Closing connection connection with MySQL server...")
        self.sql_db.close()