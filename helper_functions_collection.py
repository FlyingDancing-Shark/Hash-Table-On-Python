'''
*********description*********

'''

color_dict = {'red': ['5'], 'green': [''], 'blue': ['0']}


def dictionary_helper(dict_obj, dict_key, default=0):
    found_value = dict_obj.get(dict_key)
    if found_value[0]:
            result = int(found_value[0])
    else:
            result = default
    return result

value = dictionary_helper(color_dict, 'red')



