def slope_of_cubic( coff , x ):
    a, b, c, d = coff
    #slope of polynomial is defined by taking its derivative
    slope = 3 * a * x**2 + 2 * b * x +c
    return slope

def get_coefficients():

        input_str = input("Enter the coefficients of the cubic polynomial as space-separated values: ")

        coff = tuple(map(float, input_str.split()))

        if len(coff) != 4:
            print("Error: Please enter exactly 4 coefficients.")
            return None

        return coff

coff = get_coefficients()

x = float(input("the value of x to which slope to be calculate :"))
result = slope_of_cubic(coff , x )
print(f'the slope of given cubic polynomial at x = {x} is {result}')