def function_with_uncommon_error_solution(a, b):
    if b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error_solution(10, 0)
print(result)  # Output: 10

result = function_with_uncommon_error_solution(0, 10)
print(result)  # Output: 0.0

result = function_with_uncommon_error_solution(10, 2)
print(result)  # Output: 5.0

#The following line will raise ZeroDivisionError
#result = function_with_uncommon_error_solution(0,0) 