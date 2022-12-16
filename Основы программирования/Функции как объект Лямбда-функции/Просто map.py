def simple_map(transformation, values):
    new_values = []
    for i in values:
        new_values.append(transformation(i))
    return new_values
