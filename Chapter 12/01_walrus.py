# using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"if list is too long ({n} element, expect <= 3)")