import pandas as pd
import numpy as np

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
        # self.storage_options = storage_options

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
                                low_memory= self.low_memory, memory_map= self.memory_map, float_precision= self.float_precision) 

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


    def value_changer(self, column= None, position= None, choice= None, copy= True, errors= 'raise'):
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

        self.choice = choice
        self.copy = copy
        self.errors = errors

        if column != None:
            print("\nChanging type using the column's name...")

            before = self.df[column].dtype
            self.df[column] = self.df[column].astype(dtype= self.choice, copy= self.copy, errors= self.errors)
            after = self.df[column].dtype

            print(f'Changed from {before} to {after}')

        elif position != None:
            print("\nChanging type using the column's position...")

            before = self.df.iloc[:, position].dtype
            self.df.iloc[:, position] = self.df.iloc[:, position].astype(dtype= self.choice, copy= self.copy, errors= self.errors)
            after = self.df.iloc[:, position].dtype

            print(f'Changed from {before} to {after}')

    def nan_manager(self):
        pass