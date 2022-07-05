# Program 8a: Pandas
# Create a dataframe, a dictionary of objects. 
# Create a dataFrame for drug efficacy.
# Program_8a.py: Create a DataFrame. Drug Efficacy.
import numpy as np
import pandas as pd
# pd.set_option('display.colheader_justify', 'center')
df1=pd.DataFrame({
    "Date": pd.Timestamp("20220125"),
    "Dosage (mg)": np.array(list(range(2,22,2))),
    "Sex " : pd.Categorical(["F","F","M","F","M",
                            "M","F","F","F","M"]),
    "Weight (Kg)" : pd.Series([52.2,65.8,80.7,53.5,40.9,
                     52.2,64.4,61.7,53.5,61.2],
                    dtype="float32"),
    "Efficacy (%)" : pd.Series([0,0,0,0,5,
                           20,90,100,100,100],dtype="int32")
    })
df2=pd.DataFrame({
    "Date": pd.Timestamp("20220126"),
    "Dosage (mg)": np.array(list(range(22,42,2))),
    "Sex " : pd.Categorical(["M","M","F","M","M",
                            "F","M","F","F","M"]),
    "Weight (Kg)" : pd.Series([
                     86.2,72.6,59.0,67.1,56.2,
                     61.2,78.0,45.3,54.4,88.9],
                    dtype="float32"),
    "Efficacy (%)" : pd.Series([
                           70,65,55,50,50,
                           45,10,0,0,0],dtype="int32")
    })
df=pd.concat([df1,df2],ignore_index=True)
df
df1.to_csv("Drug_Trial.csv")