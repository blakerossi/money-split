numbers = input("What dollar amounts are you starting with? please enter each amount seperated by a space: ")
ending_am = input("What is your final dollar amount? ")
starting_amounts = numbers.split(" ") 
number_of_splits = len(starting_amounts)
ending_amount = int(ending_am)

# converting all the strings in the starting_amounts array into integers
def strings_to_floats(*starting_amounts):
    int_starting_amounts = []
    for i in starting_amounts:
        try:
            int_starting_amounts.append(float(i))
        except ValueError:
            pass    
    return int_starting_amounts

int_starting_amounts = strings_to_floats(*starting_amounts)

# calculating the starting_ammounts into a total
def starting_amount_total(*int_starting_amounts):
    total = 0
    for i in int_starting_amounts:
        total += i
    return total

starting_total = starting_amount_total(*int_starting_amounts)

#calculating the ratio of a given integer in the int_starting_ammounts array to the starting_total
def ratio_to_total(int):
    ratio = int/starting_total
    return ratio

#creating an array of ratios from each starting_ammount to the starting_total
def ratios_of_starting_amounts(*int_starting_amounts):
    ratios_arr = []
    for i in int_starting_amounts:
        ratio = ratio_to_total(i)
        ratios_arr.append(ratio)
    return ratios_arr

ratios_array = ratios_of_starting_amounts(*int_starting_amounts)

#this function creates an array of the ratios applied to the ending total
def money_split(ending_amount, *ratios_array):
    ending_tot = []
    for i in ratios_array:
        ending_tot.append(ending_amount * i)
    return ending_tot

ending_totals = money_split(ending_amount, *ratios_array)
print(ending_totals)
