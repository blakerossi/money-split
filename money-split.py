def strings_to_floats(*starting_amounts):
    """converting all the strings in the starting_amounts list into floats"""
    float_starting_amounts = []
    for i in starting_amounts:
        try:
            float_starting_amounts.append(float(i))
        except ValueError:
            pass    
    return float_starting_amounts


def starting_amount_total(*float_starting_amounts):
    return sum(float_starting_amounts)


def ratio_to_total(int):
    """calculating the ratio of a given integer in the int_starting_ammounts list to the starting_total"""
    ratio = int/starting_total
    return ratio


def ratios_of_starting_amounts(*float_starting_amounts):
    """creating a list of ratios from each starting_ammount to the starting_total"""
    ratios_list = []
    for i in float_starting_amounts:
        ratio = ratio_to_total(i)
        ratios_list.append(ratio)
    return ratios_list

def money_split(ending_amount, *ratios_list):
    """this function creates a list of the ratios applied to the ending total"""
    ending_tot = []
    for i in ratios_list:
        ending_tot.append(ending_amount * i)
    return ending_tot


if __name__ == "__main__":

    numbers = input("What dollar amounts are you starting with? please enter each amount seperated by a space: ")
    ending_am = input("What is your final dollar amount? ")
    starting_amounts = numbers.split(" ") 
    ending_amount = int(ending_am)
    float_starting_amounts = strings_to_floats(*starting_amounts)
    starting_total = starting_amount_total(*float_starting_amounts)
    ratios_list = ratios_of_starting_amounts(*float_starting_amounts)
    ending_totals = money_split(ending_amount, *ratios_list)

print(ending_totals)
