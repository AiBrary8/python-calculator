class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        neg = -1
        if(a < 0):
            neg = -neg
            a = -a
        if(b < 0):
            neg = -neg
            b = -b
        for i in range(b):
            result = self.add(result, a)
        if(neg == 1):
            result = -result
        return result

    def divide(self, a, b):
        if(b == 0):
            return "Invalid denominator = 0"
        result = 0
        neg = -1
        if(a < 0):
            neg = -neg
            a = a - a - a
        if(b < 0):
            neg = -neg
            b = b - b - b
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if (neg == 1):
            result = -result
        return result
    
    def modulo(self, a, b):
        if(b == 0):
            return "Invalid b = 0"
        if(a == 0):
            return 0
        swap = 0
        neg = -1
        if(a < 0):
            swap+=1
            a = -a
        if(b < 0):
            neg = 1
            swap-=1
            b = -b
        while a >= b:
            a = a - b
        if(swap != 0):
            a = a - b
        if(swap == 0 and neg == 1):
            a = -a
        if(neg != 1 and a < 0):
            a = -a
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 5))
    print("Example: division: ", calc.divide(10, -2))
    print("Example: modulo: ", calc.modulo(0, 8))