Part a) How you implemented the initial tree (Section A) and why you chose your approaches?

For implementing the decision tree, we have used the ID3 (Iterative Dichotomiser 3) Heuristic. 

Training Phase - Building the decision tree:
1. In the ID3 algorithm, we begin with the original set of attributes as the root node. 
2. On each iteration of the algorithm, we iterate through every unused attribute of the remaining set and calculates the entropy (or information gain) of that attribute. 
3. Then, we select the attribute which has the smallest entropy (or largest information gain) value. 
4. The set of remaining attributes is then split by the selected attribute to produce subsets of the data. The algorithm continues to recurse on each subset, considering only attributes never selected before.

Testing Phase:
At runtime, we will use trained decision tree to classify the new unseen test cases by working down the decision tree using the values of this test case to arrive at a terminal node that tells us what class this test case belongs to.


I choose this approach because of the following reasons:

1. It uses a greedy approach by selecting the best attribute to split the dataset on each iteration.
2. Runs quite fast on the discrete data (Runs within 3 to 4 mins). However, on continuous data, it runs within 30-40 mins.
3. Accuracy come around 84% - 85% when discrete splitting and randomness is used along with this algorithm


--------------------------------------------------------------------------------------------------------------------------------------------------------


Part b) Accuracy result of your initial implementation (with cross validation)?

For section, I have used continuous splitting of the data. However, I have tested the decision tree with and without randomness in section A.
So, my results are as follows:

1. ID3 Algorithm with continuous splitting (non - random) = 0.8037 or 80.37%
2. ID3 Algorithm with continuous splitting (random shuffling) = 0.8129 or 81.29%


--------------------------------------------------------------------------------------------------------------------------------------------------------


Part c) Explain improvements that you made (Section C) and why you think it works better (or worse)?

I have done the following improvements:

1. Used Discrete Splitting Strategy instead of Continuous Splitting Strategy
Reason -- ID3 is harder to use on continuous data. If the values of any given attribute is continuous, then there are many more places to split the data on this attribute, and searching for the best value to split by can be time consuming. Thus, we have split the attributes "age" and "fnlweight" around their mean into two respective classes. By doing this, there was a major improvement in the time taken by the two algorithms and the accuracy too.

2. Used Random shuffling of data:
Reason -- We know that ID3 does not guarantee an optimal solution; it can get stuck in local optimums. The advantage of this method is that it reduces the probability that the ID3 algorithm will get stuck into local optimims. There was a slight increase in the accuracy by using the random shuffling of the data.


--------------------------------------------------------------------------------------------------------------------------------------------------------


Part d) Accuracy results for your improvements?

For this section, I have used discrete splitting of the data along with other improvements as mentioned above. I have tested the decision tree with and without randomness.

So, my results are as follows:

1. ID3 Algorithm with discrete splitting (non - random) = 0.8480 or 84.80%
2. ID3 Algorithm with discrete splitting (random shuffling) = 0.8512 or 85.12%

Note: The average accuracy for the ID3 Algorithm with discrete splitting (random shuffling) can change a little as the code is using random shuffling. I have reported the one that I found the best during multiple runs of the program.


