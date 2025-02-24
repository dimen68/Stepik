def update_dictionary(d, key, value):
    if key in d.keys():
        v=d[key]
        v.append(value)
        d[key]=v
    elif 2*key in d.keys():
        w=d[2 * key]
        w.append(value)
        d[2*key]=w
    else:
        d[2*key]=[value]