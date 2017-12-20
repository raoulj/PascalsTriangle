class PascalTriangle:

    def __init__(self, n):
        self.triangle = [self._pascal_level(i) for i in range(0,n)]
        
        import math
        max_number_of_digits_in_line = sum([int(math.log10(x)) + 1 for x in self.triangle[-1]])
        max_spaces_in_line = len(self.triangle[-1])
        self.max_line_length = max_number_of_digits_in_line + max_spaces_in_line

    def _pascal_level(self, n):
        return [self._combination(n,i) for i in range(0,n + 1)]

    def _combination(self,n,r):
        assert(n >= r)
        return self._factorial(n)/(self._factorial(n - r) * self._factorial(r))

    def _factorial(self,n):
        # Guard against negative input
        if n < 0:
            raise Exception("Factorial can't take negative inputs!")
        # Base Case
        if (n <= 1):
            return 1
        # Recur
        return n * self._factorial(n - 1)

    def _string_for_line(self, line):
        numbers_in_line = ' '.join([str(x) for x in line])
        return ' ' * ((self.max_line_length - len(numbers_in_line))/2) + numbers_in_line

    def __str__(self):
        return '\n'.join([self._string_for_line(x) for x in self.triangle])
    

triangle = PascalTriangle(30)
print triangle