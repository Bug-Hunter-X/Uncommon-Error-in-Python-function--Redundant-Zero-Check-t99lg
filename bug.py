def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(10, 0)
print(result)  # Output: 10

result = function_with_uncommon_error(0, 10)
print(result)  # Output: 10

result = function_with_uncommon_error(10, 2)
print(result)  # Output: 5.0

result = function_with_uncommon_error(0,0)