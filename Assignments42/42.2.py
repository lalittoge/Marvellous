import math
import numpy as np
def EuclideanDistance(P1,P2):
    Ans = math.sqrt((float(P1['X']) - float(P2['X']))**2 + (float(P1['Y']) - float(P2['Y']))**2
        )
    

    return Ans


def UserDefinedKNN():
    border = "-"*40
    Data=[
        {'point':'A','X':'1','Y':'2','label':'Red'},
        {'point':'B','X':'2','Y':'3','label':'Red'},
        {'point':'C','X':'3','Y':'1','label':'Blue'},
        {'point':'D','X':'6','Y':'5','label':'Blue'}
    ]

    print(border)
    print("User Defined KNN")
    print(border)

    for i in Data:
        print(i)
    print(border)


    x = float(input("Enter X coordinate of new point: "))
    y = float(input("Enter Y coordinate of new point: "))
    new_point={'X':x,'Y':y}

    print("Distance between two point are :")
    for d in Data:
        d['distance']=EuclideanDistance(d,new_point)
        print(d['distance'],d['label'])


    sorted_data=sorted(Data,key=lambda item:item['distance'])

    print("Sorted data is :")
    print(border)

    for d in sorted_data:
        print(d)

    k=3
    nearest=sorted_data[:k]

    print("Neaest 3 point are :")

    print(border)

    for d in nearest:
        print(d)

    votes={}

    for neibours in nearest:
        label=neibours['label']
        votes[label]=votes.get(label,0) +1


    print(border)
    print("Voting result is :",)
    print(border)

    for d in votes:
        print("Names:", d, "no of votes :", votes[d])
    
    print(border)

    iMAx=0
    Name=""

    for d in votes:
        if(votes[d]>iMAx):
            iMAx=votes[d]
            Names=d

    print("Final prediction is :",Names)



        
        

    




def main():
    UserDefinedKNN()

if __name__ == "__main__":
    main()