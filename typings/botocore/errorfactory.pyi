"""
This type stub file was generated by pyright.
"""

from botocore.exceptions import ClientError

class BaseClientExceptions(object):
    ClientError = ...
    def __init__(self, code_to_exception) -> None:
        """Base class for exceptions object on a client

        :type code_to_exception: dict
        :param code_to_exception: Mapping of error codes (strings) to exception
            class that should be raised when encountering a particular
            error code.
        """
        ...
    def from_code(self, error_code):
        """Retrieves the error class based on the error code

        This is helpful for identifying the exception class needing to be
        caught based on the ClientError.parsed_reponse['Error']['Code'] value

        :type error_code: string
        :param error_code: The error code associated to a ClientError exception

        :rtype: ClientError or a subclass of ClientError
        :returns: The appropriate modeled exception class for that error
            code. If the error code does not match any of the known
            modeled exceptions then return a generic ClientError.
        """
        ...
    def __getattr__(self, name): ...

class ClientExceptionsFactory(object):
    def __init__(self) -> None: ...
    def create_client_exceptions(self, service_model):
        """Creates a ClientExceptions object for the particular service client

        :type service_model: botocore.model.ServiceModel
        :param service_model: The service model for the client

        :rtype: object that subclasses from BaseClientExceptions
        :returns: The exceptions object of a client that can be used
            to grab the various different modeled exceptions.
        """
        ...