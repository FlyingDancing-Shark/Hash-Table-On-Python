'''
*********description*********

'''

from collections import defaultdict, Counter
from pprint import pprint

color_dict = {'red': ['5'], 'green': [''], 'blue': ['0']}


def dictionary_helper(dict_obj, dict_key, default=0):
    found_value = dict_obj.get(dict_key)
    if found_value[0]:
            result = int(found_value[0])
    else:
            result = default
    return result

value = dictionary_helper(color_dict, 'red')

##############################################################################

def display_words_count(filename, first_n_word):
    word_counts = defaultdict(int)
    lines = [ line.strip('\n') for line in open(filename, 'r') ]
    for line in lines:
        for word in line.split(' '):
            word_counts[word.lower()] += 1
    words_freq = Counter(word_counts)
    if '' in words_freq.most_common(first_n_word)[0]:
        pprint(words_freq.most_common(first_n_word)[1:])
        
####################################################################################### 

