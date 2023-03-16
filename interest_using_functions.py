deposit = 45
int_rate = 1.021


def first(init_amount):
    year1_amount = init_amount * int_rate
    return year1_amount


print(f"after first year amount with interest : {first(deposit):.2f}")


def second():
    year1_amount = first(deposit)
    second_year = year1_amount * int_rate
    return second_year


print(f"after second year amount with interest is: {second():.2f}")


def third():
    year2_amount = second()
    third_year = year2_amount * int_rate
    print(f"amount after three years is : {third_year:.2f}")


third()
