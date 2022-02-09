def search_fast(haystact, needle):
    for item in haystact:
        if item == needle:
            return True
    return False

def search_show(haystact, needle):
    return_value = False
    for item in haystact:
        if item == needle:
            return_value = True
    return return_value

