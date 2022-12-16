def from_string_to_list(string, container):
    f = string.split()
    for i in f:
        container.append(int(i))
