"""
This type stub file was generated by pyright.
"""

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Elastic File System"
prefix = "elasticfilesystem"

class Action(BaseAction):
    def __init__(self, action=...) -> None: ...

class ARN(BaseARN):
    def __init__(self, resource=..., region=..., account=...) -> None: ...

Backup = Action("Backup")
ClientMount = Action("ClientMount")
ClientRootAccess = Action("ClientRootAccess")
ClientWrite = Action("ClientWrite")
CreateAccessPoint = Action("CreateAccessPoint")
CreateFileSystem = Action("CreateFileSystem")
CreateMountTarget = Action("CreateMountTarget")
CreateTags = Action("CreateTags")
DeleteAccessPoint = Action("DeleteAccessPoint")
DeleteFileSystem = Action("DeleteFileSystem")
DeleteFileSystemPolicy = Action("DeleteFileSystemPolicy")
DeleteMountTarget = Action("DeleteMountTarget")
DeleteTags = Action("DeleteTags")
DescribeAccessPoints = Action("DescribeAccessPoints")
DescribeBackupPolicy = Action("DescribeBackupPolicy")
DescribeFileSystemPolicy = Action("DescribeFileSystemPolicy")
DescribeFileSystems = Action("DescribeFileSystems")
DescribeLifecycleConfiguration = Action("DescribeLifecycleConfiguration")
DescribeMountTargetSecurityGroups = Action("DescribeMountTargetSecurityGroups")
DescribeMountTargets = Action("DescribeMountTargets")
DescribeTags = Action("DescribeTags")
ListTagsForResource = Action("ListTagsForResource")
ModifyMountTargetSecurityGroups = Action("ModifyMountTargetSecurityGroups")
PutBackupPolicy = Action("PutBackupPolicy")
PutFileSystemPolicy = Action("PutFileSystemPolicy")
PutLifecycleConfiguration = Action("PutLifecycleConfiguration")
Restore = Action("Restore")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateFileSystem = Action("UpdateFileSystem")