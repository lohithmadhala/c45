import csv
import math
import pdb


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
visited_attributes = []


class node:

    def __init__(self, attribute_name, gain):
        self.attribute_name = attribute_name
        self.gain = gain
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def add_children(self, list_of_nodes):
        self.children.extend(list_of_nodes)


def log(num):
    if num == 0: return 0
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

    
def generate_decision_tree():
    attr_gain = []
    for attribute in attributes:
        attr_gain.append((attribute, gain(tuples, attribute)))

    max_attribute_gain = attr_gain[0]
    for attr in attr_gain:
        if attr[1] > max_attribute_gain[1]:
            max_attribute_gain = attr
    
    print(max_attribute_gain) 
    root = node(max_attribute_gain[0], max_attribute_gain[1])

    root.add_children(list(attribute_values[max_attribute_gain[0]]))
    for child in list(attribute_values[max_attribute_gain[0]]):
        new_node = node(child, 0)
        root.add_child(new_node)
    
    #make max_attribute_gain a node and create its values as children



def entropy(dataset):
    ent = 0
    # pdb.set_trace()
    positive = len([yes for yes in dataset if yes[7] == " Effect"])
    negative = len([no for no in dataset if no[7] == " No effect"]) #len(dataset) - positive
    
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
    for ent_pair in values_entropy:
        value_prob = values_entropy[ent_pair][0]/len(dataset)
        gain_dataset_attribute -= value_prob * values_entropy[ent_pair][1]
    
    return gain_dataset_attribute
    
    



if __name__ == "__main__":
    read_from_csv()
    generate_decision_tree()
