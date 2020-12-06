TARGET_SUM = 2020

# Parse file
with open('01/records.txt','r') as records_file:
    records = [ int(r) for r in records_file.read().split('\n') ]
    records.sort()

# Find starting location
j = 1
while records[j] < TARGET_SUM / 2:
    j += 1
i = j - 1

# Find the correct numbers
while records[i] + records[j] != TARGET_SUM:
    if records[i] + records[j] < TARGET_SUM:
        j += 1
    else:
        i -= 1
    if i < 0 or j >= len(records):
        print('That sum does not exist!')
        exit(1)

# Print results
print("{} + {} = {}, {} * {} = {}".format(records[i], 
                                            records[j], 
                                            TARGET_SUM, 
                                            records[i], 
                                            records[j],
                                            records[i]*records[j]))
