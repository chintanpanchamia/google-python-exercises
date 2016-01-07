__author__ = 'chintanpanchamia'

def num_ones_in_binary(inp):
    output = 0
    while(inp > 0):
        if(inp % 2 == 1):
            output += 1
        inp = inp/2
    return output

def most_ones_in_binary(inp):
    output = map(num_ones_in_binary, inp)
    final_output = {}
    for i in range(0,len(output)):
        final_output[output[i]] = inp[i]
    output = sorted(output, reverse=True)
    return final_output[output[0]]


def num_digits(x):
    return len(str(x))


def most_digits(L):
    L = sorted(L, key=num_digits)
    return L[-1]


def largest_two_digit_even(L):
    two_digit_numbers = [i for i in L if num_digits(i) == 2]
    evens = [i for i in two_digit_numbers if i % 2 == 0]
    evens.sort()
    return evens[-1]


def best(L, criteria):
    return criteria(L)


L = [1, 76, 84, 95, 214, 1023, 511, 32]
print(best(L, min))
print(best(L, largest_two_digit_even))
print(best(L, most_digits))
print(best(L, most_ones_in_binary))