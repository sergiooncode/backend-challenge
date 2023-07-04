class LandbotChallengeBaseException(Exception):
    """Base Landbot Exception"""

    def __init__(self, message=None):
        self.message = message
        super(Exception, self).__init__(message)


class LandbotUnexpectedError(LandbotChallengeBaseException):
    """Landbot Unexpected Error"""
