# Write a program that creates a dictionary of common keys from the two dictionaries below and aggregates the values of each key into a set.

dict_1 = {"first": 2, "second": 4, "third": 8}
dict_2 = {"second": 16, "fifth": 1, "third": 6}

# We use the "&" operator to get the intersection of sets, so that the common elements of both sets are stored in a variable.

mutual_keys = set(dict_1.keys()) & set(dict_2.keys())

# Using a for loop, we read the keys of mutual_keys into the variable key and create a dictionary with None as the value for each key.

mixture_dict = {key: None for key in mutual_keys}

# In this case, instead of None, we write {dict_1[key], dict_2[key]}.

mixture_dict = {key: {dict_1[key], dict_2[key]} for key in mutual_keys}

# Print the result.

print(mixture_dict)