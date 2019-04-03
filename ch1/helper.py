from urllib.parse import parse_qs

def get_first_int(values, key, default=0):

    found = values.get(key, [''])

    if found[0]:
        found = int(found[0])
    else:
        found = default
    
    return found

if __name__ == "__main__":

    my_value = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
    print(get_first_int(my_value, 'green'))

    list_comprehension = [x for x in range(100)]