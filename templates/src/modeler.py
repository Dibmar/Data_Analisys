# Data libraries
import pandas as pd
import numpy as np

# Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning libraries
from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import make_classification

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from xgboost import XGBClassifier


class Model_Maker():
    def __init__(self, dataframe= None):
        self.df = dataframe


    def column_encoder(self, column= None, position= None):
        """
                            ---What it does---
        This function encodes one column of your dataframe using Label Encoder and returns it.

                            ---What it needs---
            - You to choose between
                * The name of your column (column). It should be in string format
                * The position of your column (position). It should be int
            For the encoding to take place.

                            ---What it return---
        This function returns your encoded column
        """
        label_enc = LabelEncoder()
        
        if column != None:
            self.column_encoded = label_enc.fit_transform(self.df[column])
        
        elif position != None:
            self.column_encoded = label_enc.fit_transform(self.df.iloc[:, position])
        
        return self.column_encoded
    

    def data_splitter(self, train_list= None, name_test= None, range_of_columns= None, 
                    index_test= None, test_size= 0.33, random_state= 42, 
                    shuffle= True, stratify= None):
        """
                            ---What it does---
        This function splits your data into a Train and Test baches, then returns them.

                            ---What it needs---
            - You to choose between
                * The list of columns for train (train_list) and name of the colum for test (name_test).
                    It should be a list containing strings
                * The position of your columns for testing (range_of_columns) and index of the colum for test (index_test). 
                    It should be a valid entry for pandas' function iloc
            For the encoding to take place.

                            ---What it returns---
        This function returns X_train, X_test, y_train, y_test. In that order 
        """
        if (train_list != None) and (name_test != None):
            self.X = self.df[train_list]
            self.y = self.df[test]

        elif (range_of_columns != None) and (index_test != None):
            self.X = self.df.iloc[:, range_of_columns]
            self.y = self.df[index_test]
        
        else:
            print('Your input does not compute. Make up your mind!')
            

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y,
                                                                                test_size= test_size,
                                                                                random_state= random_state
                                                                                shuffle= shuffle,
                                                                                stratify= stratify)

        return self.X_train, self.X_test, self.y_train, self.y_test


   def scale_data(self, how=None, name_list= None, 
                index_range= None, copy=True, with_mean=True, 
                with_std=True, feature_range=(0, 1), clip=False):
        """
        TODO
                            ---What it does---
        This function creates a random forest classifier model. Prints it and returns it.

                            ---What it needs---
            - The sklearn standard arguments necessary

                            ---What it return---
        This function returns the created model
        """    
        standard = ['standard', 'Standard', 'STANDARD']
        minmax = ['minmax','MinMax', 'MINMAX']

        print(f'You chose a {how} scaler for your data')

        if name_list != None:
            data = self.df[data]
        
        elif index_range != None:
            data = self.df.iloc[: , index_range]

        if how in standard:
            scaler = StandardScaler()

        elif how in minmax:
            scaler = MinMaxScaler()

        else:
            print(f'{how} is not supported or does not exist.')

        scaled_data = scaler.fit_transform(data)

        return scaled_data


    def create_linear_or_logistic_model(self, kind= 'linear', fit_intercept=True, 
                            normalize=False, copy_X=True, 
                            n_jobs=None, positive=False, 
                            penalty='l2', dual=False, 
                            tol=0.0001, C=1.0, intercept_scaling=1, 
                            class_weight=None, random_state=None, 
                            solver='lbfgs', max_iter=100, 
                            multi_class='auto', verbose=0, 
                            warm_start=False, 
                            l1_ratio=None):
        """
                            ---What it does---
        This function creates a simple linear/logistic regression model. Prints it and returns it.

                            ---What it needs---
            - The kind of model you wish to create (linear or logistic). Must be string. set to 'linear' by default.
            - The sklearn standard arguments necessary

                            ---What it return---
        This function returns the created model
        """

        linear_list = ['linear', 'Linear', 'LINEAR']
        logistic_list = ['logistic', 'Logistic', 'LOGISTIC']

        if kind in linear_list:
            created_model = LinearRegression(fit_intercept= fit_intercept, 
                                                normalize=normalize, copy_X=copy_X, 
                                                n_jobs=n_jobs, positive=positive)
            print(self.created_model)

            self.linear_model = self.created_model.fit(self.X_train, self.y_train)
            print(self.linear_model.coef_)

            return self.linear_model
        
        elif kind in logistic_list:
            created_model = LogisticRegression(penalty= penalty, dual= dual, 
                                                    tol= tol, C= C, 
                                                    fit_intercept= fit_intercept, 
                                                    intercept_scaling= intercept_scaling, 
                                                    class_weight= class_weight, random_state= random_state, 
                                                    solver= solver, max_iter= max_iter, 
                                                    multi_class= multi_class, verbose= verbose, 
                                                    warm_start= warm_start, n_jobs= n_jobs, 
                                                    l1_ratio= l1_ratio)
            print(self.created_model) 

            self.logistic_model = self.created_model.fit(self.X_train, self.y_train)
            print(self.linear_model.coef_)

            return self.logistic_mode


    def create_random_forest (self, n_estimators=10, 
                            criterion='gini', max_depth=None, 
                            min_samples_split=2, min_samples_leaf=1, 
                            min_weight_fraction_leaf=0.0, 
                            max_features='auto', max_leaf_nodes=None, 
                            min_impurity_decrease=0.0, 
                            min_impurity_split=None, bootstrap=True, 
                            oob_score=False, n_jobs=1, 
                            random_state=None, verbose=0, 
                            warm_start=False, class_weight=None):
        """
        TODO
                            ---What it does---
        This function creates a random forest classifier model. Prints it and returns it.

                            ---What it needs---
            - The sklearn standard arguments necessary

                            ---What it return---
        This function returns the created model
        """

        created_model = RandomForestClassifier(n_estimators= n_estimators, 
                            criterion= criterion, max_depth= max_depth, 
                            min_samples_split= min_samples_split, 
                            min_samples_leaf= min_samples_leaf, 
                            min_weight_fraction_leaf= min_weight_fraction_leaf, 
                            max_features= max_features, 
                            max_leaf_nodes= max_leaf_nodes, 
                            min_impurity_decrease= min_impurity_decrease, 
                            min_impurity_split= min_impurity_split, 
                            bootstrap= bootstrap, oob_score= oob_score, 
                            n_jobs= n_jobs, random_state= n_jobs, 
                            verbose= verbose, warm_start= warm_start, 
                            class_weight= class_weight)

        self.forest_model = traffic_forest.fit(self.X_train, self.y_train)
        y_pred = forest_model.predict(self.X_test)

        return self.forest_model