import csv
import math

# data set taken from
# https://data.world/us-doe-gov/e8fc308b-97df-460e-bdc6-cce8eb82e943/workspace/file?filename=Earthquakes%2Fearthquakes.csv

'''
1 - Latitude
2 - Longitude
3 - DepthMeters
4 - MagType
5 - Magnitude
6 - potential_blast 
7 - bix_potential_blasts
'''
tuples = []
attribute_values = {
    "Latitude": set(),
    "Longitude": set(),
    "DepthMeters": set(),
    "MagType": set(),
    "Magnitude": set(),
    "potential_blast": set(),
    "bix_potential_blasts":set()
}
attributes = ["Latitude", "Longitude", "DepthMeters","MagType", "Magnitude", "potential_blast", "bix_potential_blasts"]
visited_attributes = []


#Class for storing decision tree values
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
    #Read data from csv
    with open('Earthquakes_earthquakes.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        global tuples
        tuples = list(reader) 
    
    #Get only the attributes we need
    for row in tuples:
        attribute_values["Latitude"].add(row[1])
        attribute_values["Longitude"].add(row[2])
        attribute_values["DepthMeters"].add(row[3])
        attribute_values["MagType"].add(row[5])
        attribute_values["Magnitude"].add(row[6])
        attribute_values["potential_blast"].add(row[10])
        attribute_values["bix_potential_blasts"].add(row[11])

    
def generate_decision_tree():
    attr_gain = []
    #Calculate gain for given attribute
    for attribute in attributes:
        attr_gain.append((attribute, gain(tuples, attribute)))

    max_attribute_gain = attr_gain[0]
    #Get attribute with highest gain
    for attr in attr_gain:                      
        if attr[1] > max_attribute_gain[1]:
            max_attribute_gain = attr

    print(attr_gain) #Change this value to max_attribute_gain to see which attribute is selected

    root = node(max_attribute_gain[0], max_attribute_gain[1])

    #Attempt to create tree and assign values
    root.add_children(list(attribute_values[max_attribute_gain[0]]))
    for child in list(attribute_values[max_attribute_gain[0]]):
        new_node = node(child, 0)
        root.add_child(new_node)

    
    # generate_decision_tree("""" couldn't get recursive call to work """)
    
    #make max_attribute_gain a node and create its values as children



def entropy(dataset):
    #Entropy of a dataset is a calculated based on shannon entropy.
    #In this case, the dataset[i][10] is our target variable that we wil be predction for.
    ent = 0
    positive = len([yes for yes in dataset if yes[10] == "1"]) #calculates the probablity for a desired result (although 1 refers to an impactful eartquake)
    negative = len([no for no in dataset if no[10] == "0"]) #calculates the probablity for an undesired result 

    #calculates the probablity
    positive_prob = positive/len(dataset) 
    negative_prob = negative/len(dataset)

    #cacluates the entropy
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
