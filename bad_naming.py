def bad_name_examples(my_string, increment, value1, term):
    for i in range(0, value1):
        while value1 >= increment:
            my_string += term
            value1 -= increment
    return my_string
