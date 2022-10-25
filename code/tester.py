import pandas as pd

class Tester():
    '''
    This class is to help with reading and submission of Kaggle test file
    '''
    def __init__(self,path):
        '''
        Instantiates the Tester object, read from test file, and save ID sequence
        '''
        self.df=pd.read_csv(path)
        self.df_id=self.df[['Id']]
    
    def get_test_df(self):
        '''
        return: Test DataFrame
        '''
        return self.df
    
    def get_length(self):
        '''
        return: Lenth of test file
        '''
        return self.df_id.shape[0]
    
    def write_submission(self,pred,output):
        '''
        Takes a prediction and output path, and writes a Kaggle format csv to file
        pred: list, whose length must be equal to length of test file
        output: output path of .csv (must end with ".csv")
        '''
        
        #check if length of pred is correct
        if len(pred) != self.get_length():
            print("Length mismatch")
            return 1
        
        #merge the ID and predicted SalePrice
        self.df_result=pd.concat([self.df_id,pd.DataFrame(pred)],axis=1)

        #rename the columns
        self.df_result.rename(columns={self.df_result.columns[1]: "SalePrice"}, inplace = True)
        
        #save to csv
        self.df_result.to_csv(output,index=False)
        
        print(f"Output saved to {output}")