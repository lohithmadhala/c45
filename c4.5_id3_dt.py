import csv
import math

'''
1 - region
2 - epicenter
3 - distance from coast
4 - depth
5 - scale
6 - duration 
7 - effect (target variable)
'''
tuples = []
attribute_values = {
    "Region": set(),
    "Epicenter": set(),
    "Distance_from_shore": set(),
    "Depth": set(),
    "Scale": set(),
    "Duration": set(),
    "Effect":set()
}
attributes = [
    "Region","Epicenter", "Distance_from_shore", "Depth", "Scale", "Duration", "Effect"
    ]

def log(num):
    return math.log(num,2)

def read_from_csv():
    with open('earthquake.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        global tuples
        tuples = list(reader) 
    
    for row in tuples:
        attribute_values["Region"].add(row[1])
        attribute_values["Epicenter"].add(row[2])
        attribute_values["Distance_from_shore"].add(row[3])
        attribute_values["Depth"].add(row[4])
        attribute_values["Scale"].add(row[5])
        attribute_values["Duration"].add(row[6])
        attribute_values["Effect"].add(row[7])

def entropy(dataset):
    ent = 0
    postive = len([yes for yes in dataset if yes[6] == "Effect"])
    negative = len([no for no in dataset if no[6] == "No effect"]) #len(dataset) - positive
    
    positive_prob = positive/len(dataset)
    negative_prob = negative/len(dataset)

    ent = - positive_prob * log(positive_prob) - negative_prob * log(negative_prob)
    return ent

def gain(dataset, attribute_name): #dataset is filtered to just attribute_name
    ds_entropy = entropy(dataset)
    values_entropy = {}
    for value in attribute_values[attribute_name]: # loop through attribute values and prepare dataset for each value
        value_subset = [row for row in dataset if value in row]
        values_entropy[value] = [len(value_subset), entropy(value_subset)]
    
    gain_dataset_attribute = ds_entropy
    for entropy in values_entropy:
        value_prob = entropy[0]/len(dataset)
        gain_dataset_attribute -= value_prob * entropy[1]
    
    return gain_dataset_attribute
    
    



if __name__ == "__main__":
    read_from_csv()
