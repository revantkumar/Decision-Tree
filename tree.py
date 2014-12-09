import csv
import math
import random

# Implement your decision tree below
# Used the ID3 algorithm to implement the Decision Tree

# Class used for learning and building the Decision Tree using the given Training Set
class DecisionTree():
    tree = {}

    def learn(self, training_set, attributes, target):
        self.tree = build_tree(training_set, attributes, target)


# Class Node which will be used while classify a test-instance using the tree which was built earlier
class Node():
    value = ""
    children = []

    def __init__(self, val, dictionary):
        self.value = val
        if (isinstance(dictionary, dict)):
            self.children = dictionary.keys()


# Majority Function which tells which class has more entries in given data-set
def majorClass(attributes, data, target):

    freq = {}
    index = attributes.index(target)

    for tuple in data:
        if (freq.has_key(tuple[index])):
            freq[tuple[index]] += 1 
        else:
            freq[tuple[index]] = 1

    max = 0
    major = ""

    for key in freq.keys():
        if freq[key]>max:
            max = freq[key]
            major = key

    return major


# Calculates the entropy of the data given the target attribute
def entropy(attributes, data, targetAttr):

    freq = {}
    dataEntropy = 0.0

    i = 0
    for entry in attributes:
        if (targetAttr == entry):
            break
        i = i + 1

    i = i - 1

    for entry in data:
        if (freq.has_key(entry[i])):
            freq[entry[i]] += 1.0
        else:
            freq[entry[i]]  = 1.0

    for freq in freq.values():
        dataEntropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
        
    return dataEntropy


# Calculates the information gain (reduction in entropy) in the data when a particular attribute is chosen for splitting the data.
def info_gain(attributes, data, attr, targetAttr):

    freq = {}
    subsetEntropy = 0.0
    i = attributes.index(attr)

    for entry in data:
        if (freq.has_key(entry[i])):
            freq[entry[i]] += 1.0
        else:
            freq[entry[i]]  = 1.0

    for val in freq.keys():
        valProb        = freq[val] / sum(freq.values())
        dataSubset     = [entry for entry in data if entry[i] == val]
        subsetEntropy += valProb * entropy(attributes, dataSubset, targetAttr)

    return (entropy(attributes, data, targetAttr) - subsetEntropy)


# This function chooses the attribute among the remaining attributes which has the maximum information gain.
def attr_choose(data, attributes, target):

    best = attributes[0]
    maxGain = 0;

    for attr in attributes:
        newGain = info_gain(attributes, data, attr, target) 
        if newGain>maxGain:
            maxGain = newGain
            best = attr

    return best


# This function will get unique values for that particular attribute from the given data
def get_values(data, attributes, attr):

    index = attributes.index(attr)
    values = []

    for entry in data:
        if entry[index] not in values:
            values.append(entry[index])

    return values

# This function will get all the rows of the data where the chosen "best" attribute has a value "val"
def get_data(data, attributes, best, val):

    new_data = [[]]
    index = attributes.index(best)

    for entry in data:
        if (entry[index] == val):
            newEntry = []
            for i in range(0,len(entry)):
                if(i != index):
                    newEntry.append(entry[i])
            new_data.append(newEntry)

    new_data.remove([])    
    return new_data


# This function is used to build the decision tree using the given data, attributes and the target attributes. It returns the decision tree in the end.
def build_tree(data, attributes, target):

    data = data[:]
    vals = [record[attributes.index(target)] for record in data]
    default = majorClass(attributes, data, target)

    if not data or (len(attributes) - 1) <= 0:
        return default
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        best = attr_choose(data, attributes, target)
        tree = {best:{}}
    
        for val in get_values(data, attributes, best):
            new_data = get_data(data, attributes, best, val)
            newAttr = attributes[:]
            newAttr.remove(best)
            subtree = build_tree(new_data, newAttr, target)
            tree[best][val] = subtree
    
    return tree

# This function runs the decision tree algorithm. It parses the file for the data-set, and then it runs the 10-fold cross-validation. It also classifies a test-instance and later compute the average accurracy
# Improvements Used: 
# 1. Discrete Splitting for attributes "age" and "fnlwght"
# 2. Random-ness: Random Shuffle of the data before Cross-Validation
def run_decision_tree():
	
    data = []

    with open("hw4-task1-data.tsv") as tsv:
        for line in csv.reader(tsv, delimiter="\t"):
            
            if line[0] > '37':
                line[0] = '1'
            else:
                line[0] = '0'

            if line[2] > '178302':
                line[2] = '1'
            else:
                line[2] = '0'

            data.append(tuple(line))

	print "Number of records: %d" % len(data)

	attributes = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-info_gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']
	target = attributes[-1]

	K = 10
	acc = []
    for k in range(K):
        random.shuffle(data)
        training_set = [x for i, x in enumerate(data) if i % K != k]
        test_set = [x for i, x in enumerate(data) if i % K == k]
        tree = DecisionTree()
        tree.learn( training_set, attributes, target )
        results = []

        for entry in test_set:
            tempDict = tree.tree.copy()
            result = ""
            while(isinstance(tempDict, dict)):
                root = Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])
                tempDict = tempDict[tempDict.keys()[0]]
                index = attributes.index(root.value)
                value = entry[index]
                if(value in tempDict.keys()):
                    child = Node(value, tempDict[value])
                    result = tempDict[value]
                    tempDict = tempDict[value]
                else:
                    result = "Null"
                    break
            if result != "Null":
                results.append(result == entry[-1])

        accuracy = float(results.count(True))/float(len(results))
        acc.append(accuracy)

    avg_acc = sum(acc)/len(acc)
    print "Average accuracy: %.4f" % avg_acc

    # Writing results to a file (DO NOT CHANGE)
    f = open("result.txt", "w")
    f.write("accuracy: %.4f" % avg_acc)
    f.close()

if __name__ == "__main__":
	run_decision_tree()