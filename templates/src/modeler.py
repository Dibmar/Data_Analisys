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
from sklearn.model_selection import GridSearchCVf
from sklearn.model_selection import cross_val_score

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.pipeline import Pipeline
from sklearn.pipeline import FeatureUnion

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import make_classification

from sklearn.linear_model import LogisticRegression


from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from xgboost import XGBClassifier


class Model_Maker():
    def __init__(self, dataframe= None):
        self.df = dataframe
        self.label_enc = LabelEncoder()


    def column_encoder(self, column= None, position= None):
        """
                            ---What it does---
        This function

                            ---What it needs---
            - 

                            ---What it return---
        This function
        """
        
        if column != None:
            self.column_encoded = encoder.fit_transform(self.df[column])
        
        elif position != None:
            self.column_encoded = encoder.fit_transform(self.df.iloc[:, position])
        
        return self.column_encoded
    

    def data_splitter(self, train_list= None, test= None, test_size= 0.33, random_state= 42, scale_data= True):
        """
                            ---What it does---
        This function

                            ---What it needs---
            - 

                            ---What it return---
        This function
        """
        
        self.X = self.df[train_list]
        self.y = self.df[test]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y,
                                                                                test_size= test_size,
                                                                                random_state= random_state)


        if scale_data == True:
                self.scaler = MinMaxScaler()

                self.X_train = self.scaler.fit_transform(self.X_train)
                self.X_test = self.scaler.transform(self.X_test)


        return self.X_train, self.X_test, self.y_train, self.y_test
    

    def create_linear_model(self):
        """
                            ---What it does---
        This function

                            ---What it needs---
            - 

                            ---What it return---
        This function
        """

        self.created_model = LinearRegression(fit_intercept=False).fit(self.X, self.y)
        print(self.created_model)

        self.linear_model = self.created_model.fit(self.X_train, self.y_train)
        print(linear_model.coef_)
