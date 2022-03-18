from pexpect import ExceptionPexpect


class DuplicatedError(Exception):
    pass

class ExistenceError(Exception):
    # Both Thread and Post
    pass

class AccessError(Exception):
    pass

