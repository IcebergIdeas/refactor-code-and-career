def unexecuted_example(self):
  if fruit == "Apples":
        my_snack = "Apples"
        return my_snack

    if fruit != "Oranges":
        if fruit == "Apples":
            # this piece of code will never be hit since we already returned for Apples above
            my_snack = "Apples"
            return my_snack
        else:
            my_snack = fruit
            return my_snack
    else:
        my_snack = "Oranges"
        return my_snack
