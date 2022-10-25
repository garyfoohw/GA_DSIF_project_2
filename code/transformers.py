import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from utils import ordinal_to_rank

class MSSubClassConvert(BaseEstimator, TransformerMixin):
    '''
    Custom Transformer that assert only 'MSSubClass' column to string type
    '''
    #Class Constructor 
    def __init__(self, drop=[]):
        self.drop=drop
        return None
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform(self, X, y = None):
        X['MS SubClass']=X['MS SubClass'].astype(str)
        return X
        
class DropCorrelated(BaseEstimator, TransformerMixin):
    '''
    Custom Transformer that  drop correlated columns as passed
    '''
    #Class Constructor 
    def __init__(self, drop=[]):
        self.drop=drop
        return None
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform(self, X, y = None):
        return X.drop(columns=self.drop)
    
class FeatureSelector(BaseEstimator, TransformerMixin):
    #Class Constructor 
    def __init__(self, feature_names=None,by=None):
        '''
        Custom Transformer that extracts columns as passed by names in a list, or numerical/catergorical
        feature_names: list of features to pick for. If feautres_names is not None, 'by' will be ignored.
        by: 'categorical' or 'numerical'. The type of features to pick out for. Only used if feature_names is None.
        '''
        self.feature_names = feature_names
        self.by=by
        return None
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform(self, X, y = None):
        if self.feature_names is not None:
            return X[self.feature_names] 
        else:
            if self.by=="categorical":
                return X.select_dtypes(exclude='number')
            elif self.by=="numerical":
                return X.select_dtypes(include='number')
            else:
                print(f"Error: Expected 'categorical' or 'numerical', but got ''{self.by}'.")
                return None
            
class StandardImpute(BaseEstimator, TransformerMixin):
    '''
    Custom Transformer that imputes with None, 0 or mode.
    '''
    #Class Constructor 
    def __init__(self, none=[], zero=[], mode=[]):
        '''
        zero:list of cols to impute to 0
        none: list of cols to impute to None
        mode: list of cols to impute with mode
        '''
        self.zero = zero
        self.none = none
        self.mode = mode
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform(self, X, y = None):
        X_cols=list(X.columns)
        
        for i in [z for z in self.none if z in X_cols]:
            X[i]=X[i].fillna("None")
            
        for j in [z for z in self.zero if z in X_cols]:
            X[j]=X[j].fillna(0)
        
        for k in [z for z in self.mode if z in X_cols]:
            X[k]=X[k].fillna(X[k].mode()[0])
        
        return X 
    
class ImputeZero(BaseEstimator, TransformerMixin):
    '''
    Custom Transformer that fills Na with 0
    '''
    #Class Constructor 
    def __init__(self):
        return None
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform(self, X, y = None):
        return X.fillna(0)
    
class LotFrontageImpute(BaseEstimator, TransformerMixin):
    '''
    Custom Transformer that imputes Lot Frontage with data from Neighborhood's Lot Frontage
    '''
    #Class Constructor 
    def __init__(self):
        return None
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform(self, X, y = None):
        X['Lot Frontage']=X.groupby(by="Neighborhood")['Lot Frontage'].transform(
            lambda z: z.fillna(z.median() if not np.isnan(z.median()) else X['Lot Frontage'].median()))
        
        return X
    
class OrdinalToNumeric(BaseEstimator, TransformerMixin):
    '''
    Custom Transformer that transforms ordinal features to numerical
    '''
    #Class Constructor 
    def __init__(self):
        return None
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform(self, X, y = None):
        X=ordinal_to_rank(X)
        
        return X
    
class AlignTrainPredict(BaseEstimator, TransformerMixin):
    '''
    Custom Transformer that forces 'predict' and 'fit' dataframes to match a pre-determined sequence
    of features.
    Required as cross validation + one hot encoding will cause colums to mismatch.
    '''
    #Class Constructor 
    def __init__(self,feature_names):
        self.feature_names=feature_names
        return None
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform(self, X, y = None):
        list_to_retain=[z for z in self.feature_names if z in X.columns]
        X=X[list_to_retain]
        
        list_of_missing_feat=[z for z in self.feature_names if z not in X.columns]
        for i in list_of_missing_feat:
            X.loc[:,i]=0
            
        #reset sequence of columns
        X=X[self.feature_names]
        
        return X
    
class OneHotEncode(BaseEstimator, TransformerMixin):
    '''
    Custom Transformer that one hot encode categorical features only and return the whole DF
    '''
    #Class Constructor 
    def __init__(self):
        return None
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform(self, X, y = None):
        
        #look at categorical columns
        df_c=X.select_dtypes(exclude='number')

        #look at numerical columns
        df_n=X.select_dtypes(include='number')

        df_c=pd.get_dummies(df_c,drop_first=True)

        df_new=pd.concat([df_n,df_c],axis=1)
        
        return df_new
    
class Passthrough(BaseEstimator, TransformerMixin):
    '''
    Custom Transformer that does nothing but provides methods to pass information out of the pipeline.
    '''
    #Class Constructor 
    def __init__(self):
        
        return None
    
    #Return self nothing else to do here    
    def fit(self, X, y = None):
        return self 
    
    #Method that describes what we need this transformer to do
    def transform(self, X, y = None):
        self.X=X
        return X
    
    #method to pass feature_names outside of pipeline
    def get_feature_names(self):
        return self.X.columns