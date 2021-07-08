# Code to create sigma fields

# The sigma_field is only equivalent to the powerset
# when the events generating the sigma field are the singleton events / outcomes

# We must use the immutable 'frozenset' data type
# because the mutable 'set' data type cannot contain mutable objects

from itertools import combinations

emptyset = frozenset()


def make_powerset(input_set):
    size = len(input_set)
    powerset = set([emptyset])
    for k in range(1, size + 1):
        for comb in combinations(input_set, k):
            powerset.add(frozenset(comb))
    return powerset


# Problem data
n = 8
sample_space = {i for i in range(n)}  # Single n-sided die roll

# Create the sigma field
sigma_field = make_powerset(sample_space)

# Choose some arbitrary events from the sample space
# Note these are zero-indexed
events = [{1}, {2, 3, 4, 5}, {1, 3, 5, 7}]

# Verify that events are in the sigma field
for event in events:
    assert event in sigma_field

# Verify the null and certain events are in the sigma field
for event in [emptyset, sample_space]:
    assert event in sigma_field

# Print the entire sigma field
for event in sigma_field:
    print(event)
