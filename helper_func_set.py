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

######################## END OF dictionary_helper() definition #########################

def display_words_count(filename, first_n_word):
    from collections import defaultdict, Counter
    from pprint import pprint
    word_counts = defaultdict(int)
    # for Linux system, need to remove an extra'\r' character
    lines = [ line.strip('\r\n') for line in open(filename, 'r') ]
    for line in lines:
        for word in line.split(' '):
            word_counts[word.lower()] += 1
    words_freq = Counter(word_counts)
    if '' in words_freq.most_common(first_n_word)[0]:
        pprint(words_freq.most_common(first_n_word)[1:])
        
######################## END OF display_words_count() definition ######################### 


def close_kitchen_if_past_cutoff_time(point_in_time):
 if point_in_time >= closing_time():
 close_kitchen()
 log_time_closed(point_in_time)

