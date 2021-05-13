import numpy as np

# Generate an array with 1000 random numbers
x = np.random.randint(0, 1000, size=(1, 1000))[0]

# print the original mean of entire dataset
print("The original Mean value:", x.mean())

# Choose 30 random samples with each sample containing 25 random data points
resamples = [np.random.choice(x, size=25, replace = True) for i in range(30)]

# List for storing means of random samples
avg_lst = []
for i in range(0, 30):
    # compute mean of each sample and store in the list
    avg_lst.append(resamples[i].mean())

# Compute the predicted mean by taking mean of all the means of the random samples
cumm_mean = sum(avg_lst) / len(avg_lst)

print("The inferred Mean value:", cumm_mean)