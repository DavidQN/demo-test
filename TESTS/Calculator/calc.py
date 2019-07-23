
class Calculator():

    @staticmethod
    def add(arg1, arg2):
        if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
            raise ValueError("Arguments passed into this method must be an Int") 
        return arg1 + arg2

    @staticmethod
    def divide(arg1, arg2):
        if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
            raise ValueError("Arguments passed into this method must be an Int") 
        return arg1 / arg2

    @staticmethod
    def multiply(arg1, arg2):
        if not isinstance(arg1, (int, float)) or not isinstance(arg1, (int, float)):
            raise ValueError("Arguments passed into this method must be an Int or Float") 
        return arg1 * arg2