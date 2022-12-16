def recursive_reverse(some_list):
    if not some_list:
        return []
    return [some_list.pop()] + recursive_reverse(some_list)


print(recursive_reverse([1, 2, 3]))