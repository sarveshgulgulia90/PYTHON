class Polynomial:
    def __init__(self, coefficients):
        # coefficients is a list representing the coefficients of the polynomial
        # The index i of the list corresponds to the coefficient of x^i
        self.coefficients = coefficients

    def __add__(self, other):
        # Adding two polynomials
        # Pad the shorter polynomial with zeros
        len_self, len_other = len(self.coefficients), len(other.coefficients)
        max_len = max(len_self, len_other)
        
        padded_self = self.coefficients + [0] * (max_len - len_self)
        padded_other = other.coefficients + [0] * (max_len - len_other)
        
        # Sum the coefficients element-wise
        result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        
        return Polynomial(result_coefficients)

    def __mul__(self, other):
        # Multiplying two polynomials
        result_degree = len(self.coefficients) + len(other.coefficients) - 2
        result_coefficients = [0] * (result_degree + 1)

        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]

        return Polynomial(result_coefficients)

    def __str__(self):
        # Display the polynomial using __str__ method
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                if i == 0:
                    terms.append(str(coef))
                elif i == 1:
                    terms.append(f"{coef}x")
                else:
                    terms.append(f"{coef}x^{i}")

        # Join the terms in reverse order to display the polynomial correctly
        return " + ".join(terms[::-1])

# Example usage:
poly1 = Polynomial([1, 0, 1, 1])   
poly2 = Polynomial([1, 2, 1])     

# Addition
sum_poly = poly1 + poly2
print("Sum:", sum_poly)

# Multiplication
product_poly = poly1 * poly2
print("Product:", product_poly)
