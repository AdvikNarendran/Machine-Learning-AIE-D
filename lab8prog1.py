import numpy as np
from collections import Counter
import pandas as pd

class DecisionTreeRootFinder:
    def __init__(self):
        self.root_feature = None
    
    def calculate_information_gain(self, data, labels, feature_index):
        # Calculate total entropy before split
        total_entropy = self.calculate_entropy(labels)
        
        # Calculate entropy after split
        unique_values = set(data[:, feature_index])
        split_entropy = 0
        for value in unique_values:
            subset_indices = np.where(data[:, feature_index] == value)[0]
            subset_labels = labels[subset_indices]
            split_entropy += (len(subset_labels) / len(labels)) * self.calculate_entropy(subset_labels)
        
        # Calculate information gain
        information_gain = total_entropy - split_entropy
        
        return information_gain
    
    def calculate_entropy(self, labels):
        label_counts = Counter(labels)
        entropy = 0
        total_instances = len(labels)
        for label in label_counts:
            probability = label_counts[label] / total_instances
            entropy -= probability * np.log2(probability)
        
        return entropy
    
    def find_root_feature(self, data, labels):
        num_features = data.shape[1]
        max_information_gain = float('-inf')
        best_feature_index = None
        
        for feature_index in range(num_features):
            information_gain = self.calculate_information_gain(data, labels, feature_index)
            if information_gain > max_information_gain:
                max_information_gain = information_gain
                best_feature_index = feature_index
        
        self.root_feature = best_feature_index
        return best_feature_index

# Example usage:
# Assuming data is a numpy array where each row represents an instance and each column represents a feature
# Assuming labels is a numpy array containing corresponding labels for each instance

data = np.array([
    [1, 2, 3],  # Sample instance 1 with features [1, 2, 3]
    [4, 5, 6],  # Sample instance 2 with features [4, 5, 6]
    [7, 8, 9]   # Sample instance 3 with features [7, 8, 9]
])

# Corresponding labels for each instance
labels = np.array([0, 1, 0])  # Sample labels for each instance

# Initialize the DecisionTreeRootFinder
root_finder = DecisionTreeRootFinder()

# Find the root feature
root_feature_index = root_finder.find_root_feature(data, labels)

print("Root feature index:", root_feature_index)