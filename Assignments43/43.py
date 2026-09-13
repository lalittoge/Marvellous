import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier



def main():

    Datapath=("MarvellousInfosystems_PlayPredictor.csv")

    df=pd.read_csv(Datapath)
    print(df)

    model=model.fit(df)
    model=KNeighborsClassifier(n_neighbors=3)
    new_point=()
if __name__ == "__main__":
    main()