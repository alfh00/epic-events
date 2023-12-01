class UserContext:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserContext, cls).__new__(cls)
            cls._instance.current_user = None
        return cls._instance

    def set_current_user(self, user):
        self.current_user = user

    def get_current_user(self):
        return self.current_user
