# EDA libs

import pandas as pd
import numpy as np

# Visualization libs

import matplotlib.pyplot as plt
from datetime import date

# Helpful libs

import sys, os

class Titan ():
    
    def __init__(self, path):
        
        # For dataframe construction.
        self.df = ''
        self.path = path     


    def create_df(self, wish= False, sep=',', delimiter= None, header= 'infer', 
                names= None, index_col= None, usecols= None, squeeze= False, 
                prefix= None, mangle_dupe_cols= True, dtype= None,
                engine= None, converters= None,
                true_values= None, false_values= None, skipinitialspace= False, 
                skiprows= None, skipfooter= 0, nrows= None, 
                na_values= None, keep_default_na= True, na_filter= True,
                verbose= False, skip_blank_lines= True, parse_dates= False,
                infer_datetime_format= False, keep_date_col= False, date_parser= None,
                dayfirst= False, cache_dates= True, iterator= False,
                chunksize= None, compression= 'infer', thousands= None,
                decimal= '.', lineterminator= None, quotechar='"',
                quoting= 0, doublequote= True, escapechar= None, 
                comment= None, encoding= None, dialect= None, 
                error_bad_lines= True, warn_bad_lines= True, 
                delim_whitespace= False, low_memory= True, 
                memory_map= False, float_precision= None, storage_options= None):
        """
                            ---What it does---
        This function creates a dataframe object using the pandas library and the read_csv function.

                            ---What it needs--
            - The command to return/not return the dataframe (wish). Should be a boolean.
            - A path to follow (provided earlier in class creation). Should be a double barred ('\\') formatted  string.
            - The rest of necessary values are set to default (as they appear in the pandas documentation)

                            ---What it returns---
        The dataframe generated (self.df).
        """
        # For df creation
        self.sep = sep                                  # By default set as ','
        self.delimiter = delimiter
        self.header = header
        self.names = names
        self.index_col = index_col
        self.usecols = usecols
        self.squeeze = squeeze
        self.prefix = prefix
        self.mangle_dupe_cols = mangle_dupe_cols
        self.dtype = dtype
        self.engine = engine
        self.converters= converters
        self.true_values = true_values
        self.false_values = false_values
        self.skipinitialspace = skipinitialspace
        self.skiprows = skiprows
        self.skipfooter = skipfooter
        self.nrows = nrows
        self.na_values = na_values
        self.keep_default_na = keep_default_na
        self.na_filter = na_filter
        self.verbose = verbose
        self.skip_blank_lines = skip_blank_lines
        self.parse_dates = parse_dates
        self.infer_datetime_format = infer_datetime_format
        self.keep_date_col = keep_date_col
        self.date_parser = date_parser
        self.dayfirst = dayfirst
        self.cache_dates = cache_dates
        self.iterator = iterator
        self.chunksize = chunksize
        self.compression = compression
        self.thousands = thousands
        self.decimal = decimal
        self.lineterminator = lineterminator
        self.quotechar = quotechar
        self.quoting = quoting
        self.doublequote = doublequote
        self.escapechar = escapechar
        self.comment = comment
        self.encoding = encoding
        self.dialect = dialect
        self.error_bad_lines = error_bad_lines
        self.warn_bad_lines = warn_bad_lines
        self.delim_whitespace = delim_whitespace
        self.low_memory = low_memory
        self.memory_map = memory_map
        self.float_precision = float_precision
        self.storage_options = storage_options

        # Creation of dataframe
        self.df = pd.read_csv(filepath_or_buffer= self.path, sep= self.sep,
                                delimiter= self.delimiter, header= self.header, names= self.names,
                                index_col= self.index_col, usecols= self.usecols, squeeze= self.squeeze,
                                prefix= self.prefix, mangle_dupe_cols= self.mangle_dupe_cols,
                                dtype= self.dtype, engine= self.engine, converters= self.converters,
                                true_values= self.true_values, false_values= self.false_values, 
                                skipinitialspace= self.skipinitialspace, skiprows= self.skiprows, 
                                skipfooter= self.skipfooter, nrows= self.nrows, na_values= self.na_values, 
                                keep_default_na= self.keep_default_na, na_filter= self.na_filter, verbose= self.verbose,
                                skip_blank_lines= self.skip_blank_lines, parse_dates= self.parse_dates,
                                infer_datetime_format= self.infer_datetime_format,
                                keep_date_col= self.keep_date_col, date_parser= self.date_parser, dayfirst= self.dayfirst,
                                cache_dates= self.cache_dates, iterator= self.iterator, chunksize= self.chunksize,
                                compression= self.compression, thousands= self.thousands, decimal= self.decimal,
                                lineterminator= self.lineterminator, quotechar = self.quotechar,quoting= self.quoting,
                                doublequote= self.doublequote, escapechar= self.escapechar, comment= self.comment,
                                encoding= self.encoding, dialect= self.dialect, error_bad_lines= self.error_bad_lines, 
                                warn_bad_lines= self.warn_bad_lines, delim_whitespace= self.delim_whitespace, 
                                low_memory= self.low_memory, memory_map= self.memory_map, float_precision= self.float_precision,
                                storage_options= self.storage_options) 

        if wish == True:
            return self.df


    def general_info(self):
        """
                            ---What it does--
        This function creates two dataframe objects to inform the user of all the relevant preliminary information about a dataframe.
        Such as:    1- Shape of the dataframe
                    2- Name and position of columns
                    3- Type of data contained
                    4- Number of NaN values


                            ---What it needs---
        A df object

                            ---What it returns---
        The data report (2 to 4) in dataframe format (report)
        """

        # df columns info
        columns_name = self.df.columns
        rows = self.df.shape[0]
        columns = self.df.shape[1]
        

        shape_df = pd.DataFrame({'Shape': ['Rows', 'Columns'], ' ': [rows, columns]})


        col_data = []
        null_numb = []
        for n in range(columns):
            col_data.append(self.df.iloc[:, n].dtype)
            null_numb.append(self.df.iloc[:, n].isnull().sum())
        

        report = pd.DataFrame({'Columns': columns_name, 'Data type': col_data, 'NaNs in column': null_numb})

        title = '\t\tGeneral info on the df:'
        sub_title = 'Shape'
        sub_title_2 = 'Data type and NaNs'

        print(title)
        print(sub_title)
        print(shape_df)
        print('-' * len(sub_title_2), '\n')
        print(sub_title_2)
        print(report)
        

        return report


    def value_changer(self, column= None, position= None, change_num= True, copy= True, errors= 'raise', downcast= None):
        """
                                ---What it does---
        This function changes the data type of a given column in a dataframe. Locating it either by name or position.
                                
                                ---What it needs---
            - Either the name or the colum's position.
                * column for name
                * position for the colum's position
            - The choice to change the data to
            - The rest of necessary values are set to default (as they appear in the pandas documentation)
                                
                                ---What it returns---
        This function does not return anything.
        """

        self.column = column
        self.position = position

        self.change_num = change_num
        self.copy = copy
        self.errors = errors
        self.downcast = downcast



        def change_to_num_or_str(self):
            if change_num == False:
                if column != None:
                    print("\nChanging type using the column's name...")

                    before = self.df[column].dtype
                    self.df[column] = self.df[column].astype(dtype= str, copy= self.copy, errors= self.errors)
                    after = self.df[column].dtype

                    print(f'Changed from {before} to {after}')

                elif position != None:
                    print("\nChanging type using the column's position...")

                    before = self.df.iloc[:, position].dtype
                    self.df.iloc[:, position] = self.df.iloc[:, position].astype(dtype= str, copy= self.copy, errors= self.errors)
                    after = self.df.iloc[:, position].dtype

                    print(f'Changed from {before} to {after}')
            
            else:
                if column != None:
                    print("\nChanging type using the column's name...")

                    before = self.df[column].dtype
                    self.df[column] = pd.to_numeric(self.df[column], errors= self.errors)
                    after = self.df[column].dtype

                    print(f'Changed from {before} to {after}')

                elif position != None:
                    print("\nChanging type using the column's position...")

                    before = self.df.iloc[:, position].dtype
                    self.df.iloc[:, position] = pd.to_numeric(self.df.iloc[:, position], errors= self.errors)
                    after = self.df.iloc[:, position].dtype

                    print(f'Changed from {before} to {after}')


        def auxiliary_function (self):
            """
            TODO
                                ---What it does---
            This function acts only if the regular function is unable to change data types.
            In such a case, it finds and drops any data that refuses to co-operate.
            
                                ---What it needs---
                - Column to be checked (self.column)
            
                                ---What it returns---
            This function does not return anything.
            """
            to_nuke = dict(pd.to_numeric(self.df[self.column], errors='coerce'))
            
            print('Unable to change types. Auxiliary function launched!')
            for e in to_nuke:
                print (f'- {e}: {to_nuke}\n')

            # for e in to_nuke.keys():
            #     print(f'Deleting {e}')
            #     self.column = self.column.drop(e)
                
            print('\n... Odd data dropped')
        try:
            change_to_num_or_str(self)
        
        except ValueError as ve:
            print('An error occured!...')
            
            auxiliary_function(self)
            print('Rebooting...')

            change_to_num_or_str(self)
        


    def nan_manager(self, column= None, position= None, drop_na= False, fill_na= False, axis=0, 
                    subset=None, value=None, method=None, limit=None, downcast=None, inplace=True, 
                    how='any'):
        """
                            ---What it does---
        This functions allows the user to either fill or drop NaN values in a dataframe, using the fillna() and dropna() functions of
        the pandas library.

                            ---What it needs---
            - Location of the data:
                * Name of the column (column)
                * Position of the column (position)
                * Almost all the attributes of the fill_na and dropna functions
                    -> TODO implement the thresh= in the function
                    
                            ---What it returns---
        This function does not return anything
        """
        
        self.column = column
        self.position = position
        self.axis = axis
        self.inplace = inplace


        if drop_na == True:
            self.how = how

            print('Dropping data...')

            if column != None:
                print(f"Dropping NaN values by column name\n")
            
                self.df[column].dropna(axis= self.axis, how= self.how, inplace= self.inplace)

            if position != None:
                print(f"Dropping NaN values by position\n")
                
                self.df.iloc[:, position].dropna(axis= self.axis, how= self.how, inplace= self.inplace)

            else:
                self.df.dropna(axis= self.axis, how= self.how, inplace= self.inplace)


        elif fill_na == True:
            self.value = value
            self.method = method
            self.limit = limit
            self.downcast = downcast

            print('Filling data...')

            if column != None:
                if type(self.value) == int or type(self.value) == float:

                    self.df[column].fillna(value= self.value, method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)
                
                elif type(self.value) == str:
                    methods = ['mean', 'std', 'mode']

                    if self.value in methods:
                       
                        if self.value == methods[0]:
                            self.df[column].fillna(value= self.df[column].mean(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)

                        if self.value == methods[1]:
                            self.df[column].fillna(value= self.df[column].std(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)

                        if self.value == methods[2]:
                            self.df[column].fillna(value= self.df[column].mode(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)
                    
                    else:
                        self.df[column].fillna(value= self.value, method= self.method, 
                                            axis= self.axis, inplace= self.inplace, limit= self.limit,
                                            downcast= self.downcast)
            
            elif position != None:
                if type(self.value) == int or type(self.value) == float:
                    self.df.iloc[:, position].fillna(value= self.value, method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)
                
                elif type(self.value) == str:
                    methods = ['mean', 'std', 'mode']

                    if self.value in methods:
                        if self.value == methods[0]:
                            self.df.iloc[:, position].fillna(value= self.df.iloc[:, position].mean(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)

                        if self.value == methods[1]:
                            self.df.iloc[:, position].fillna(value= self.df.iloc[:, position].std(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)

                        if self.value == methods[2]:
                            self.df.iloc[:, position].fillna(value= self.df.iloc[:, position].mode(), method= self.method, 
                                        axis= self.axis, inplace= self.inplace, limit= self.limit,
                                        downcast= self.downcast)
                    
                    else:
                        self.df.iloc[:, position].fillna(value= self.value, method= self.method, 
                                            axis= self.axis, inplace= self.inplace, limit= self.limit,
                                            downcast= self.downcast)
            

    def return_df(self, wish= False, name= None):
        """
                            ---What it does---
        This function rerturs a processed dataframe.

                            ---What it needs---
            - A dataframe (self.dataframe)
            - wish = True saves de dataframe in .csv format in the CURRENT directory
            - sep is equal to self.sep (',' by default)

                            ---What it returns---
        A dataframe (self.df)
        """
        name = name + '_' + str(date.today()) + '.csv'
        
        print(self.df)

        if wish == True:
            self.df.to_csv(name, sep= self.sep)
        return self.df


    def quick_plotter(self):

        def num_generator(self):    
            to_plot = self.df.select_dtypes(include=['float64', 'int64'])

            return to_plot


        def plot_bar(self, save_image = 0):
            """
                                ---What it does---
            Plots a barplot with the variable given. And if desired, saves the plot in the same directory as parent file with "<current date>_barplot.jpg" as name.
                                ---What it needs---
            A df_column, panda series or dictionary with numerical values
                                ---What it returns---
            If desired (save_image != 0), a jpg image file in the same directory using "<current date>_barplot.jpg" as name.
            """

            if self.column.sum() > 0:
                self.column.plot(kind = 'bar')

                if save_image != 0:
                    name = str(date.today()) + '_barplot.jpg'
                    plt.savefig(name)
            else:
                print(f'No numeric data to plot')


        def plot_line(self, save_image = 0):
            """
                                ---What it does---
            Plots a lineplot with the variable given. And if desired, saves the plot in the same directory as parent file with "<current date>_lineplot.jpg" as name.
                                ---What it needs---
            A df_column, panda series or dictionary with numerical values
                                ---What it returns---
            If desired (save_image != 0), a jpg image file in the same directory using "<current date>_lineplot.jpg" as name.
            """

            if self.column.sum() > 0:
                self.column.plot()

                if save_image != 0:
                    name = str(date.today()) + '_lineplot.jpg'
                    plt.savefig(name)
            else:
                print(f'No numeric data to plot')


        def plot_pie(self, save_image = 0):
            """
                                ---What it does---
            Plots a pieplot with the variable given. And if desired, saves the plot in the same directory as parent file with "<current date>_pieplot.jpg" as name.
                                ---What it needs---
            A df_column, panda series or dictionary with numerical values
                                ---What it returns---
            If desired (save_image != 0), a jpg image file in the same directory using "<current date>_pieplot.jpg" as name.
            """

            if self.column.sum() > 0:
                data = self.column

                # Create lables
                labels = dict(self.column).keys()

                # Plot pie chart
                plt.pie(data, autopct='%1.1f%%', startangle=0, shadow= True, pctdistance = 0.5, labeldistance = 1.2)

                # Legend and titles
                plt.legend(labels, loc= 'best')
                plt.title(self.to_plot.name, loc='center')

                plt.tight_layout()
                plt.show()
                
                if save_image != 0:
                    name = str(date.today()) + '_pieplot.jpg'
                    plt.savefig(name)
            else:
                print ("No numeric data to plot")


        self.to_plot = num_generator(self)
        func_dict = {1: plot_bar(self), 2: plot_line(self), 3: plot_pie(self)}

        print("Your columns will be plotted according to your input.")

        for column in self.to_plot.columns:
            print(self.to_plot[column])
            func_dict[1](self.to_plot[column])


    def add_to_my_path_dir (self):
        """
                            ---What it does---
        This function adds the libraries current path to your pc path directory.

                            ---What it needs---
            - The sys and os libraries
        
                            ---What it returns---
        This function does not return anything
        """
        CURR_DIR = os.path.dirname(os.path.abspath(__file__))
        print(CURR_DIR)
        sys.path.append(CURR_DIR)
        for path in sys.path:
            print(path)    


# Sample = Titan(path= '')
# Sample.add_to_my_path_dir()