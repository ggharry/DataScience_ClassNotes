#!/usr/bin/python
# Import required libraries
import sys
from collections import defaultdict

# Start a counter and store the textfile in memory
impressionSum = 0.0
ageSum = 0.0
clickThruSum = 0.0
oldestAge = 0
ageDist = {}
ageDist = defaultdict(lambda: 0, ageDist)
lines = sys.stdin.readlines()
lines.pop(0)

# For each line, find the sum of index 2 in the list.
for line in lines:
  currentAgeRecord = int(line.strip().split(',')[0])

  impressionSum = impressionSum + int(line.strip().split(',')[2])
  ageSum = ageSum + currentAgeRecord
  clickThruSum = clickThruSum + int(line.strip().split(',')[3])

  ageDist[currentAgeRecord] += 1

  if currentAgeRecord > oldestAge:
    oldestAge = currentAgeRecord

# Printing results
print 'Impression Sum: ', impressionSum
print 'Average Age: ', ageSum / len(lines)
print 'Average Click Per Impression: ', clickThruSum / impressionSum
print 'Oldest Age: ', oldestAge
print 'Age Distributions: ', ageDist

# Writing age distributions to a text file called ageDist.txt
f = open('ageDist.txt', 'w')
for key, value in ageDist.iteritems():
  f.write("Age " + str(key) + ": " + str(value) + "\n")
f.close()

### EOF ###