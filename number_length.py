# Length of Number
# Create a function that takes a number num and returns its length.

# Examples
# number_length(10) ➞ 2

# number_length(5000) ➞ 4

# number_length(0) ➞ 1
# Notes
# The use of the len() function is prohibited.



def number_length(num):
    result = str(num)
    return len(result)
print(number_length(10))
print(number_length(5000))


def number_length(num):
    # Handle the special case when the number is 0
    if num == 0:
        return 1
    
    count = 0
    while num > 0:
        num //= 10  # Integer division by 10 removes the last digit
        count += 1
    
    return count

# Test cases
print(number_length(10))   # Output: 2
print(number_length(5000)) # Output: 4
print(number_length(0))    # Output: 1
