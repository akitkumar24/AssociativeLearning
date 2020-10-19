import string
import random

ITEMS = 6
NTRANS = 9
MINSUPPORT = 3
nTrans = 3421083
someconf = 0.7
stores = 0
import pandas as pd
from collections import defaultdict

mainItems = defaultdict(lambda:[])
def makeset(item,trans):
    s = set()
    for i in range(NTRANS):
        if item in trans[i]:
            s.add(i)
            
    return s
def eclat(itemset,tsd):
    global stores
    '''input("? ")
    print(itemset)
    for i in tsd:
        print(i,"---",tsd[i])'''
    klist = list(tsd.keys())
    klen = len(klist)
    for i in range(klen-1):
        item = klist[i]     
        newitemset = itemset.union(item)                            # Adding each item to previous set to generate new rules
        #newitemset = (B)
        newtsd = {}
        for j in range(i+1,klen):
            jitem = klist[j]
            tmp = tsd[jitem].intersection(tsd[item])                # Checking the number of transactions common between A and B
            confAB = len(tmp)/len(tsd[item])
            # checking if the confidence is greater than required confidence
            if len(tmp)>= MINSUPPORT and confAB>=someconf:          # MINSUPPORT is the minimun number of transactions should be common between A and B
                print(confAB,newitemset,jitem)
                mainItems[tuple(newitemset)].append(jitem)          # adding the rule to mainItems
                newtsd[jitem]= tmp                                  # creating new 

                
        if len(newtsd) > 0:
            eclat(newitemset,newtsd)
            
def getName(x,df):
     for i in x:
             e = int(i)
             try:
                     print(df[df.product_id==e].product_name.iloc[0])
             except:
                     print()
            
            
if __name__ == "__main__":
    # code to generate random transactions
    '''items = list(string.ascii_uppercase)[:ITEMS]
    print("items ",items)
    input("? ")
    
    trans = []
    for i in range(NTRANS):
        n = random.randrange(2,6)
        random.shuffle(items)
        trans.append(set(items[:n]))
        
    tsetdict= {}
    for item in items:
        tsetdict[item] = makeset(item,trans)
    for i in tsetdict.keys():
        print(i,"---",tsetdict[i])'''
    
    # reading the training data
    df = pd.read_csv("Data/order_products__prior.csv")
    df1 = df.groupby('product_id')['order_id'].apply(set).reset_index(name='transSet')
    setdict = {str(df1.iloc[i].product_id):df1.iloc[i].transSet for i in range(len(df1))}
    del df
    del df1
    eclat(set(),setdict)
    
    
    df = pd.read_csv("Data/products.csv")
    numberOfRules = len(mainItems.keys())
    allRules = list(mainItems.keys())

    for i in range(10):
        index = random.randint(0,numberOfRules)
        print("Items in bag")
        getName(allRules[index],df)
        print()
        print("Suggested items")
        getName(mainItems[allRules[index]],df)
        print()
        print("---------------------------------------")

    
    
    
