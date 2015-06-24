#!/usr/bin/python
# Import required libraries
import sys
import math

AGE_IDX = 0
GENDER_IDX = 1
IMPRESSION_IDX = 2
CLICK_IDX = 3
SIGNED_IN_IDX=4

class ResponseAnalyzer(object):

    def __init__(self, responses, min_age=0):
        self._min_age = min_age   
        self._responses = responses

    def print_informative_message(self):
        ages = self._get_ages()
        impressions = self._get_impressions()
        clicks = self._get_clicks()
        
        print '  Impressions: ', sum(impressions)
        print '  Average age: ', mean(ages) 
        print '  Click through rate: ', 100 * sum(clicks) / float(sum(impressions)), '%'
        print '  Age of oldest person:', max(ages) 
        print '  Age distribution:'
        print '    10th percentile:', percentile(ages, 10)
        print '    25th percentile:', percentile(ages, 25)
        print '    50th percentile:', percentile(ages, 50)
        print '    75th percentile:', percentile(ages, 75)
        print '    90th percentile:', percentile(ages, 90)
        
    def _get_ages(self):
        return self._get_all_vals_for_field('age')
    
    def _get_genders(self):
        return self._get_all_vals_for_field('gender')
        
    def _get_impressions(self):
        return self._get_all_vals_for_field('impression')
    
    def _get_clicks(self):
        return self._get_all_vals_for_field('click')
    
    def _get_signed_in(self):
        return self._get_all_vals_for_field('signed_in')
    
    def _get_all_vals_for_field(self, field):
        return [int(response[field]) for response in self._responses if int(response['age']) >= self._min_age]

def mean(data):
    return sum(data) / float(len(data))

def percentile(data, percentile):
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]
    
def load_std_in():
    return sys.stdin.readlines()

def get_responses_from_records(records):
    records.pop(0)
    responses = []
    for record in records:
        split_record = record.strip().split(',')
        responses.append({'age': int(split_record[AGE_IDX]),
                          'gender': int(split_record[GENDER_IDX]),
                          'impression': int(split_record[IMPRESSION_IDX]),
                          'click': int(split_record[CLICK_IDX]),
                          'signed_in': int(split_record[SIGNED_IN_IDX])})
    return responses
    
def main(name, data_dir='.'):
    responses = get_responses_from_records(load_std_in())
    
    print 'Hello Grader! These are stats on all users.'
    ResponseAnalyzer(responses).print_informative_message()
    
    print '...and these are stats on all users 15 and older.'
    ResponseAnalyzer(responses, 15).print_informative_message()

if __name__ == '__main__':
    main(*sys.argv)