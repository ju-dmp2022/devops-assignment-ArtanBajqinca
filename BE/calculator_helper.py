class CalculatorHelper():
    log_properties = {
        'custom_dimensions': {
            'userId': 'artan_bajqinca'
        }
    }

# CD/CI test 1

    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculatorHelper, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._user_list = []
            self._current_user = None
            admin = self.User('admin', 'test1234')
            self._user_list.append(admin)
            self._is_initialized = True

    class User():
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def __repr__(self):
            return f"User(username={self.username}, password={self.password})"

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def calculate(self, operation, operand1, operand2):
        if operation == 'add':
            return self.add(operand1, operand2)
        elif operation == 'subtract':
            return self.subtract(operand1, operand2)
        elif operation == 'multiply':
            return self.multiply(operand1, operand2)
        elif operation == 'divide':
            if operand2 == 0:
                raise ValueError("Division by zero is not allowed")
            return self.divide(operand1, operand2)
        else:
            raise ValueError(f"Unsupported operation: {operation}")

    def register_user(self, username, password):
        for user in self._user_list:
            if user.username == username:
                return None
        user = self.User(username, password)
        self._user_list.append(user)
        return username

    def login(self, username, password):
        for user in self._user_list:
            if user.username == username and user.password == password:
                self._current_user = user
                return username
        return None

    def logout(self):
        if self._current_user:
            user = self._current_user
            self._current_user = None
            return user
        else:
            return None

    def get_current_user(self):
        return self._current_user
