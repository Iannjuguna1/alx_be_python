# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: does not need access to class or instance
    @staticmethod
    def add(a, b):
        return a + b

    # Class method: uses 'cls' to access class-level attributes
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

