
import pandas as pd
import numpy as np

def main():
    border="-"*30
    data={
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    df = pd.DataFrame(data)

    print(data)
    print(border)
    print(df)
    print(border)
    print(df.shape)
    print(border)
    print(df.columns)
    print(border)
    print(df.describe)
    print(border)
    print(df.dtypes)
    print(border)
    df['Total']=df['Math']+df['Science']+df['English']
    print(df)
    print(border)
    print(df[df['Science']>85])
    print(border)
    df['Name']=df['Name'].replace('Pooja','Puja')
    print(df)
    print(border)
    print(df.sort_values(by='Total'))
    print(border)
    df.drop(columns=['English'],inplace=True)
    print(df)
    print(border)



    data2={
        'Name':['Amit','Sagar','Pooja'],
        'Math':[np.nan,76,88],
        'Science':[91,np.nan,85]

    }
    df=pd.DataFrame(data2)
    print(df)
    print(border)
    df=df.fillna(df.mean(numeric_only=True))
    print(df)


if __name__== "__main__":
    main()