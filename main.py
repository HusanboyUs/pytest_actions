

class Calculator:

    @staticmethod
    def add_numbers(num1,num2):
        return num1 + num2
    
    @staticmethod
    def minus_numbers(num1,num2):
        return num1-num2
    
    @staticmethod
    def multiply_numbers(num1,num2):
        return num1*num2
    
    @staticmethod
    def subtract_numbers(num1,num2):
        return num1 // num2
    
    @staticmethod
    def is_bigger(num1,num2):
        if num1 > num2:
            return True
        else:
            return False
    

    @staticmethod
    def is_small(num1,num2):
        return num1 + num2
    
    @staticmethod
    def number_square(num1):
        raise TypeError()
    
    
    @staticmethod
    def number_root(num1):
        pass

print(Calculator.subtract_numbers(4,2))