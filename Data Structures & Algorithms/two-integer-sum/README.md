brute force
we, take 2 loops of the array i and j and then check if there sum is equal to the target and return the index of the 2

optimized
make a hash map of dict,
then find complement=target-array[i]
if the complement is already present in the hash map then we return array[complement],i
then further go hash[complement]=i so that helps in adding the elements
