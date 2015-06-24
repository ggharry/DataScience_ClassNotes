#!/usr/bin/python
# Import required libraries
import sys
from collections import defaultdict

def get_stats(records):
    # Start a counter and store the textfile in memory
    impressionSum = 0.0
    maxImpressionSum = 0.0
    clickSum = 0.0
    maxClickSum = 0.0
    numRecords = len(records)

    # For each line, find the sum of index 2 in the list.
    for record in records:
        impressionSum = impressionSum + record[0]
        clickSum = clickSum + record[1]
        maxImpressionSum = max(maxImpressionSum, impressionSum)
        maxClickSum = max(maxClickSum, clickSum)

        return [impressionSum / numRecords, clickSum / numRecords, maxImpressionSum, maxClickSum]

def get_data_dictionary(lines):
    tree = lambda: defaultdict(tree)
    data = tree()

    for line in lines:
        age = int(line.strip().split(',')[0])
        gender = int(line.strip().split(',')[1])
        impressions = int(line.strip().split(',')[2])
        clicks = int(line.strip().split(',')[3])
        signed_in = int(line.strip().split(',')[4])

        if data[age][gender][signed_in] == {}:
            data[age][gender][signed_in] = []

        data[age][gender][signed_in].append([impressions, clicks])

    return data

lines = sys.stdin.readlines()
lines.pop(0)
categories = get_data_dictionary(lines)

for age in categories:
    for gender in categories[age]:
        for signed_in in categories[age][gender]:
            records = categories[age][gender][signed_in]
            if len(records) != 0:
                print get_stats(records)
### EOF ###