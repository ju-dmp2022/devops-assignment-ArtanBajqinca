import logger

class CalculatorHelper():
    log_properties = {
        'custom_dimensions': {
            'userId': 'artan_bajqinca'
        }
    }

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
            admin = self.User('admin','test1234')
            self._user_list.append(admin)
            self._is_initialized = True
            self.logger = logger.get_logger(__name__)

    class User():
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def __repr__(self):
            return f"User(username={self.username}, password={self.password})"

    def add(self, a, b):
        a = int(a)
        b = int(b)
        result = a + b
        self.logger.debug(f"Adding {a} and {b} resuluts in {result}", extra=self.log_properties)
        return a + b

    def subtract(self, a, b):
        a = int(a)
        b = int(b)
        result = a - b
        self.logger.debug(f"Subtracting {a} and {b} resuluts in {result}", extra=self.log_properties)
        return a - b

    def multiply(self, a, b):
        a = int(a)
        b = int(b)
        result = a * b
        self.logger.debug(f"Multiplying {a} and {b} resuluts in {result}", extra=self.log_properties)
        return a * b

    def divide(self, a, b):
        a = int(a)
        b = int(b)
        result = a / b
        self.logger.debug(f"Dividing {a} and {b} resuluts in {result}", extra=self.log_properties)
        return a / b

    def register_user(self, username, password):
        # Log the attempt to register a new user
        self.logger.debug(f"Attempting to register user: {username}", extra=self.log_properties)
        for user in self._user_list:
            if user.username == username:
                # Log if the user already exists
                self.logger.warning(f"User {username} already exists", extra=self.log_properties)
                return None
        # Register the new user and log the success
        user = self.User(username, password)
        self._user_list.append(user)
        self.logger.info(f"User {username} registered successfully", extra=self.log_properties)
        return username

    def login(self, username, password):
        # Log the attempt to log in
        self.logger.debug(f"User {username} attempting to log in", extra=self.log_properties)
        for user in self._user_list:
            if user.username == username and user.password == password:
                self._current_user = user
                # Log a successful login
                self.logger.info(f"User {username} logged in successfully", extra=self.log_properties)
                return username
        # Log a failed login attempt
        self.logger.warning(f"Login failed for user {username}", extra=self.log_properties)
        return None

    def logout(self):
        # Log the logout action
        if self._current_user:
            user = self._current_user
            self._current_user = None
            self.logger.info(f"User {user.username} logged out", extra=self.log_properties)
            return user
        else:
            # Log if no user is logged in
            self.logger.warning("No user is currently logged in", extra=self.log_properties)
            return None

    def get_current_user(self):
        return self._current_user