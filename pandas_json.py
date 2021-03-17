
import pandas.io.json as pd_JSON
import pandas as pd

f=open('data.JSON','r')
data=pd_JSON.loads(f.read())

df=pd.json_normalize(data,record_path='records')

print(df.head())