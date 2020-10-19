# Associative Rule learning using Eclat algorithm

## What is Associative leaning
Associative learning is a learning principle in which a human or animal remembers a new information by associating with an existing information. For example, if someone gets a stomach ache after eating food, they associate that particular food to stomach ache. This means that our brain stores information in a chain and any new information is directly appended to this chain based on the connection it creates with the nodes of that chain. As we gain experience over time, we process mutliple infomation about each node and based on the information from experience, its characteristics or position changes in the chain.

## Associate Rule learning
Associate Rule learning is a rule based learning method for machines, where intresting relations are generated between each item in the dataset. These relationships are found based on the associate learning constraints. Based on the concept of strong rules, Rakesh Agrawal, Tomasz Imieliński and Arun Swami[1] introduced association rules for finding relationships between products in large-scale transaction dataset. For example, the rule found in the sales data of a supermarket was that if people bought onions and potatoes together, they are tend to buy hamburger meat. Such information amongst products can be used as the basis for decisions about store sale, product placements in a store, promotions, etc.

## Constraints:
1. Support: Support is a measure to determine the frequency of item bought by customers.
![Support](https://github.com/akitkumar24/AssociativeLearning/blob/master/Support.PNG)

Count(A) = Number of times the items A in all the transactions.

2. Confidence: Confidence measures the percentage of times that item B is purchased, given that item A was purchased.

Confidence of a rule A --> B:

![Confidence](https://github.com/akitkumar24/AssociativeLearning/blob/master/Confidence.PNG)

# Eclat Algorithm
Eclat algorithm is a depth first search algorithm for finding frequent item sets in a transaction or database. It represents the data in vertical pattern making the algorithm faster than Aprori which is a breadth first search algorithm.

## Associate Rule learning on Instacart Dataset

In 2017 instacart released dataset containing 3 millions instacart orders in an open source challange on Kaggle. They challenged Kaggle community to use this anonymized data on customer orders over time to predict which previously purchased products will be in a user’s next order. I have used this dataset to suggest the item/s that the consumer might purchase based on its association with the previous item in the cart. The link to the dataset can be found [here](https://www.kaggle.com/c/instacart-market-basket-analysis)

The order for training or creating rules can be found in "order_products__prior.csv". 
~~~
order_id
product_id 
add_to_cart_order: order in which each product was added to cart
reordered: 1 if this product has been ordered by this user in the past, 0 otherwise
~~~

To get the rules, we need the product and its transaction ID. To do so, I grouped all the columns of the csv based on the product_id and combined all the order_id into a list respective to their product_id

~~~
df = pd.read_csv("order_products__prior.csv")
df = df.groupby('product_id')['order_id'].apply(list).reset_index(name='transSet')
~~~
In my code, I am working with the set intersection between items to get common transactions. In order to do so, I have created the dictionary of products with its transaction.

~~~
setdict = {str(df.iloc[i].product_id):set(df.iloc[i].transSet) for i in range(len(df))
~~~

Using Eclat Algorithm, We will generate a dictionary which will contain all the items that were bought after the purchase of certain items.

Minimum confidence used is 0.7

# Result:

| People who bought                                                             |    Also bought this                 |
| ----------------------------------------------------------------------------- |:-----------------------------------:|
|Cut Russet Potatoes Steam N' Mash, Dry Nose Oil, Green Chile Anytime Sauce     | Diet Cola                           |
| Chocolate Sandwich Cookies, Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce, Light Strawberry Blueberry Yogurt, Green Chile Anytime Sauce      | Chocolate Chip Cookie Dough   |
| Grade A Extra Large Eggs, Banana | Chocolate Sandwich Cookies, Robust Golden Unsweetened Oolong Tea      |
| Strawberries, Banana, Carb Balance Flour Tortillas | Cut Russet Potatoes Steam N' Mash      |

There are many patterns like above and can be used as basis for decisions about store sale, product placements in a store, promotions, etc.
 



# References

1. Agrawal, R.; Imieliński, T.; Swami, A. (1993). "Mining association rules between sets of items in large databases". Proceedings of the 1993 ACM SIGMOD international conference on Management of data - SIGMOD '93. p. 207. CiteSeerX 10.1.1.40.6984. doi:10.1145/170035.170072. ISBN 978-0897915922.
2. Zaki, M. J. (2000). "Scalable algorithms for association mining". IEEE Transactions on Knowledge and Data Engineering. 12 (3): 372–390. CiteSeerX 10.1.1.79.9448. doi:10.1109/69.846291.

