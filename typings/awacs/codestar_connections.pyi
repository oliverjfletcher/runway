"""
This type stub file was generated by pyright.
"""

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS CodeStar Connections"
prefix = "codestar-connections"

class Action(BaseAction):
    def __init__(self, action=...) -> None: ...

class ARN(BaseARN):
    def __init__(self, resource=..., region=..., account=...) -> None: ...

CreateConnection = Action("CreateConnection")
CreateHost = Action("CreateHost")
DeleteConnection = Action("DeleteConnection")
DeleteHost = Action("DeleteHost")
GetConnection = Action("GetConnection")
GetHost = Action("GetHost")
GetIndividualAccessToken = Action("GetIndividualAccessToken")
GetInstallationUrl = Action("GetInstallationUrl")
ListConnections = Action("ListConnections")
ListHosts = Action("ListHosts")
ListInstallationTargets = Action("ListInstallationTargets")
ListTagsForResource = Action("ListTagsForResource")
PassConnection = Action("PassConnection")
RegisterAppCode = Action("RegisterAppCode")
StartAppRegistrationHandshake = Action("StartAppRegistrationHandshake")
StartOAuthHandshake = Action("StartOAuthHandshake")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateConnectionInstallation = Action("UpdateConnectionInstallation")
UseConnection = Action("UseConnection")