def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."    
    result = ""
    for num in range(1, n + 1):
        if num > 1:
            result += " "
        result += str(num)
    return result
print(number_pattern(4))
print(number_pattern(12))