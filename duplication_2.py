def duplication_example():
    increment = 10
    my_string = ""
    primary_value = 25
    for _ in range(primary_value):
        while primary_value >= increment:
            my_string += "Major"

    second_increment = 1
    for i in range(primary_value):
        while primary_value >= second_increment:
            my_string += "minor"
            primary_value -= second_increment
