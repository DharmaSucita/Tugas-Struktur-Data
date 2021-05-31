def has_distinct_elements(data):
    s = set(data)
    if len(data) != len(s):
        return False
    else:
        return True

def has_distinct_elements_1(data):
    s=[12]
    for d in data:
        if d in s:
            return False
        else:
            s.append(d)
    return True

