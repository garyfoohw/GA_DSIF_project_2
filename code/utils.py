import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from scipy import stats

def show_hist_qq(df,x,hist_title=""):
    '''
    Plots a univariate histogram and Q-Q plot
        
    string: DataFrame which contains the variable to be plot as a column
    x: Name of column to plot
    title: Title of Histogram
    return: None.
    '''
    fig,axes=plt.subplots(1,2)
    fig.set_size_inches(18, 5)
    _=sns.histplot(data=df, x=x, kde=True, ax=axes[0]).set(title=hist_title)
    _=stats.probplot(df[x],plot=axes[1])
    print(f"Skew: {df[x].skew():.2f}")
    
def log_and_return(df,col,drop=False):
    '''
    Apply natural numpy.log1p to a column in a DataFrame and returns the whole Dataframe
    df: Dataframe
    col: Name of column to log
    drop: Boolean, to drop original column
    return: Dataframe with logged column
    '''
    eps=0.001
    df[f'log_{col}']=np.log1p(df[col]+eps)
    if drop:
        df=df.drop(columns=col)
    return df

def correlation_map(df,title="",size=(18,18)):
    '''
    Show a correlation heatmap
    df: Dataframe to perform correlation
    title: Title of heatmap
    size: Size of chart, default (18,18)
    '''
    plt.rcParams['figure.figsize']=(18,18)
    _=sns.heatmap(df.corr(),square=True).set(title=title)
    
def single_correlation_map(df,col,size=(1,10),corr_threshold=0.5):
    '''
    Show a correlation map for a single variable
    df: Dataframe to correlate
    col: name of column to show
    size: Size of chart, default (1,10)
    corr_threshold: min level of +/- correlation to include in plot
    return:list of features plotted
    '''
    plt.rcParams['figure.figsize']=size
    corrmap=df.corr()[[col]].sort_values(ascending=False,by=col).iloc[1:,:]
    
    corrmap=corrmap[corrmap[col].abs()>=corr_threshold]

    _=sns.heatmap(corrmap,annot=True,vmin=-1,vmax=1).set(title=f"Correlation for {col}")
    
    return list(corrmap.index)

def RMSE_vs_feat_count(df,drawline=None):
    '''
    create a chart of RMSE for a dataframe with x = 'Feature Count' and y='RMSE'
    df:Dataframe
    '''
    fig=px.line(df,x="Feature Count",y="RMSE",title="RMSE against number of features",
           width=800, height=400)
    
    if drawline is not None:
        fig.add_vline(x=drawline, line_width=3, line_dash="dash", line_color="green")
        
    fig.show()
    
def ordinal_to_rank(df):
    '''
    df:Dataframe to map the ordinal values to numerical
    return: Mapped DataFrame
    '''
    var='Lot Shape'
    df[var]=df[var].map({"IR3":1,"IR2":2,"IR1":3,"Reg":4})

    var='Utilities'
    df[var]=df[var].map({"ELO":1,"NoSeWa":2,"NoSewr":3,"AllPub":4})

    var='Land Slope'
    df[var]=df[var].map({"Sev":1,"Mod":2,"Gtl":3})

    var='Exter Qual'
    df[var]=df[var].map({"Po":1,"Fa":2,"TA":3,"Gd":4,"Ex":5})

    var='Exter Cond'
    df[var]=df[var].map({"Po":1,"Fa":2,"TA":3,"Gd":4,"Ex":5})

    var='Bsmt Qual'
    df[var]=df[var].map({"None":0,"Po":1,"Fa":2,"TA":3,"Gd":4,"Ex":5})

    var='Bsmt Cond'
    df[var]=df[var].map({"None":0,"Po":1,"Fa":2,"TA":3,"Gd":4,"Ex":5})

    var='Bsmt Exposure'
    df[var]=df[var].map({"None":0,"No":1,"Mn":2,"Av":3,"Gd":4})

    var='BsmtFin Type 1'
    df[var]=df[var].map({"None":0,"Unf":1,"LwQ":2,"Rec":3,"BLQ":4,"ALQ":5,"GLQ":6})

    var='BsmtFin Type 2'
    df[var]=df[var].map({"None":0,"Unf":1,"LwQ":2,"Rec":3,"BLQ":4,"ALQ":5,"GLQ":6})

    var='Heating QC'
    df[var]=df[var].map({"Po":1,"Fa":2,"TA":3,"Gd":4,"Ex":5})

    var='Electrical'
    df[var]=df[var].map({"Mix":1,"FuseP":2,"FuseF":3,"FuseA":4,"SBrkr":5})

    var='Kitchen Qual'
    df[var]=df[var].map({"Po":1,"Fa":2,"TA":3,"Gd":4,"Ex":5})

    var='Functional'
    df[var]=df[var].map({"Sal":1,"Sev":2,"Maj2":3,"Maj1":4,"Mod":5,"Min2":6,
                        "Min1":7,"Typ":8})

    var='Fireplace Qu'
    df[var]=df[var].map({"None":0,"Po":1,"Fa":2,"TA":3,"Gd":4,"Ex":5})

    var='Garage Finish'
    df[var]=df[var].map({"None":0,"Unf":1,"RFn":2,"Fin":3})

    var='Garage Qual'
    df[var]=df[var].map({"None":0,"Po":1,"Fa":2,"TA":3,"Gd":4,"Ex":5})

    var='Garage Cond'
    df[var]=df[var].map({"None":0,"Po":1,"Fa":2,"TA":3,"Gd":4,"Ex":5})

    var='Paved Drive'
    df[var]=df[var].map({"N":1,"P":2,"Y":3})

    var='Pool QC'
    df[var]=df[var].map({"None":0,"Fa":1,"TA":2,"Gd":3,"Ex":4})

    var='Fence'
    df[var]=df[var].map({"None":0,"MnWw":1,"GdWo":2,"MnPrv":3,"GdPrv":4})

    var='Central Air'
    df[var]=df[var].map({"N":0,"Y":1})
    
    return df

def onehot_encode_categorical_features(df,return_number=True,label=""):
    '''
    Onehot encode categorical features only and return the whole dataframe, or only the catergorial portion
    df: Dataframe to one-hot encode
    return_numer: True if the numerical features are to be returned, False if otherwise.
    label: target feature to retain (i.e. the y variable). Must be filled in if return_number = False
    return: Treated Dataframe    
    '''
    #look at categorical columns
    df_c=df.select_dtypes(exclude='number')

    #look at numerical columns
    df_n=df.select_dtypes(include='number')

    df_c=pd.get_dummies(df_c,drop_first=True)
    
    if return_number:
        return pd.concat([df_n,df_c],axis=1)
    else:
        if label=="":
            display("label attribute cannot be blank")
            return None
        return pd.concat([df_c,df[label]],axis=1)