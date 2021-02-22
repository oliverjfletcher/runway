"""
This type stub file was generated by pyright.
"""

import logging
import re

from botocore.docs.utils import AutoPopulatedParam, HideParamFromOperations
from botocore.signers import (
    add_generate_db_auth_token,
    add_generate_presigned_post,
    add_generate_presigned_url,
)
from botocore.utils import conditionally_calculate_md5

"""Builtin event handlers.

This module contains builtin handlers for events emitted by botocore.
"""
logger = logging.getLogger(__name__)
REGISTER_FIRST = object()
REGISTER_LAST = object()
VALID_BUCKET = re.compile(r"^[a-zA-Z0-9.\-_]{1,255}$")
_ACCESSPOINT_ARN = (
    r"^arn:(aws).*:s3:[a-z\-0-9]+:[0-9]{12}:accesspoint[/:]" r"[a-zA-Z0-9\-]{1,63}$"
)
_OUTPOST_ARN = (
    r"^arn:(aws).*:s3-outposts:[a-z\-0-9]+:[0-9]{12}:outpost[/:]"
    r"[a-zA-Z0-9\-]{1,63}[/:]accesspoint[/:][a-zA-Z0-9\-]{1,63}$"
)
VALID_S3_ARN = re.compile("|".join([_ACCESSPOINT_ARN, _OUTPOST_ARN]))
VERSION_ID_SUFFIX = re.compile(r"\?versionId=[^\s]+$")
SERVICE_NAME_ALIASES = {"runtime.sagemaker": "sagemaker-runtime"}

def handle_service_name_alias(service_name, **kwargs): ...
def check_for_200_error(response, **kwargs): ...
def set_operation_specific_signer(context, signing_name, **kwargs):
    """ Choose the operation-specific signer.

    Individual operations may have a different auth type than the service as a
    whole. This will most often manifest as operations that should not be
    authenticated at all, but can include other auth modes such as sigv4
    without body signing.
    """
    ...

def decode_console_output(parsed, **kwargs): ...
def generate_idempotent_uuid(params, model, **kwargs): ...
def decode_quoted_jsondoc(value): ...
def json_decode_template_body(parsed, **kwargs): ...
def validate_bucket_name(params, **kwargs): ...
def sse_md5(params, **kwargs):
    """
    S3 server-side encryption requires the encryption key to be sent to the
    server base64 encoded, as well as a base64-encoded MD5 hash of the
    encryption key. This handler does both if the MD5 has not been set by
    the caller.
    """
    ...

def copy_source_sse_md5(params, **kwargs):
    """
    S3 server-side encryption requires the encryption key to be sent to the
    server base64 encoded, as well as a base64-encoded MD5 hash of the
    encryption key. This handler does both if the MD5 has not been set by
    the caller specifically if the parameter is for the copy-source sse-c key.
    """
    ...

def disable_signing(**kwargs):
    """
    This handler disables request signing by setting the signer
    name to a special sentinel value.
    """
    ...

def add_expect_header(model, params, **kwargs): ...

class DeprecatedServiceDocumenter(object):
    def __init__(self, replacement_service_name) -> None: ...
    def inject_deprecation_notice(self, section, event_name, **kwargs): ...

def document_copy_source_form(section, event_name, **kwargs): ...
def handle_copy_source_param(params, **kwargs):
    """Convert CopySource param for CopyObject/UploadPartCopy.

    This handler will deal with two cases:

        * CopySource provided as a string.  We'll make a best effort
          to URL encode the key name as required.  This will require
          parsing the bucket and version id from the CopySource value
          and only encoding the key.
        * CopySource provided as a dict.  In this case we're
          explicitly given the Bucket, Key, and VersionId so we're
          able to encode the key and ensure this value is serialized
          and correctly sent to S3.

    """
    ...

def inject_presigned_url_ec2(params, request_signer, model, **kwargs): ...
def inject_presigned_url_rds(params, request_signer, model, **kwargs): ...
def json_decode_policies(parsed, model, **kwargs): ...
def parse_get_bucket_location(parsed, http_response, **kwargs): ...
def base64_encode_user_data(params, **kwargs): ...
def document_base64_encoding(param): ...
def validate_ascii_metadata(params, **kwargs):
    """Verify S3 Metadata only contains ascii characters.

    From: http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html

    "Amazon S3 stores user-defined metadata in lowercase. Each name, value pair
    must conform to US-ASCII when using REST and UTF-8 when using SOAP or
    browser-based uploads via POST."

    """
    ...

def fix_route53_ids(params, model, **kwargs):
    """
    Check for and split apart Route53 resource IDs, setting
    only the last piece. This allows the output of one operation
    (e.g. ``'foo/1234'``) to be used as input in another
    operation (e.g. it expects just ``'1234'``).
    """
    ...

def inject_account_id(params, **kwargs): ...
def add_glacier_version(model, params, **kwargs): ...
def add_accept_header(model, params, **kwargs): ...
def add_glacier_checksums(params, **kwargs):
    """Add glacier checksums to the http request.

    This will add two headers to the http request:

        * x-amz-content-sha256
        * x-amz-sha256-tree-hash

    These values will only be added if they are not present
    in the HTTP request.

    """
    ...

def document_glacier_tree_hash_checksum(): ...
def document_cloudformation_get_template_return_type(section, event_name, **kwargs): ...
def switch_host_machinelearning(request, **kwargs): ...
def check_openssl_supports_tls_version_1_2(**kwargs): ...
def change_get_to_post(request, **kwargs): ...
def set_list_objects_encoding_type_url(params, context, **kwargs): ...
def decode_list_object(parsed, context, **kwargs): ...
def decode_list_object_v2(parsed, context, **kwargs): ...
def decode_list_object_versions(parsed, context, **kwargs): ...
def convert_body_to_file_like_object(params, **kwargs): ...

class ParameterAlias(object):
    def __init__(self, original_name, alias_name) -> None: ...
    def alias_parameter_in_call(self, params, model, **kwargs): ...
    def alias_parameter_in_documentation(self, event_name, section, **kwargs): ...

class ClientMethodAlias(object):
    def __init__(self, actual_name) -> None:
        """ Aliases a non-extant method to an existing method.

        :param actual_name: The name of the method that actually exists on
            the client.
        """
        ...
    def __call__(self, client, **kwargs): ...

class HeaderToHostHoister(object):
    """Takes a header and moves it to the front of the hoststring.
    """

    _VALID_HOSTNAME = ...
    def __init__(self, header_name) -> None: ...
    def hoist(self, params, **kwargs):
        """Hoist a header to the hostname.

        Hoist a header to the beginning of the hostname with a suffix "." after
        it. The original header should be removed from the header map. This
        method is intended to be used as a target for the before-call event.
        """
        ...

def inject_api_version_header_if_needed(model, params, **kwargs): ...

BUILTIN_HANDLERS = [
    ("choose-service-name", handle_service_name_alias),
    (
        "getattr.mturk.list_hi_ts_for_qualification_type",
        ClientMethodAlias("list_hits_for_qualification_type"),
    ),
    (
        "before-parameter-build.s3.UploadPart",
        convert_body_to_file_like_object,
        REGISTER_LAST,
    ),
    (
        "before-parameter-build.s3.PutObject",
        convert_body_to_file_like_object,
        REGISTER_LAST,
    ),
    ("creating-client-class", add_generate_presigned_url),
    ("creating-client-class.s3", add_generate_presigned_post),
    ("creating-client-class.iot-data", check_openssl_supports_tls_version_1_2),
    ("after-call.iam", json_decode_policies),
    ("after-call.ec2.GetConsoleOutput", decode_console_output),
    ("after-call.cloudformation.GetTemplate", json_decode_template_body),
    ("after-call.s3.GetBucketLocation", parse_get_bucket_location),
    ("before-parameter-build", generate_idempotent_uuid),
    ("before-parameter-build.s3", validate_bucket_name),
    ("before-parameter-build.s3.ListObjects", set_list_objects_encoding_type_url),
    ("before-parameter-build.s3.ListObjectsV2", set_list_objects_encoding_type_url),
    (
        "before-parameter-build.s3.ListObjectVersions",
        set_list_objects_encoding_type_url,
    ),
    ("before-parameter-build.s3.CopyObject", handle_copy_source_param),
    ("before-parameter-build.s3.UploadPartCopy", handle_copy_source_param),
    ("before-parameter-build.s3.CopyObject", validate_ascii_metadata),
    ("before-parameter-build.s3.PutObject", validate_ascii_metadata),
    ("before-parameter-build.s3.CreateMultipartUpload", validate_ascii_metadata),
    ("docs.*.s3.CopyObject.complete-section", document_copy_source_form),
    ("docs.*.s3.UploadPartCopy.complete-section", document_copy_source_form),
    ("before-call.s3", add_expect_header),
    ("before-call.glacier", add_glacier_version),
    ("before-call.apigateway", add_accept_header),
    ("before-call.s3.PutObject", conditionally_calculate_md5),
    ("before-call.s3.UploadPart", conditionally_calculate_md5),
    ("before-call.glacier.UploadArchive", add_glacier_checksums),
    ("before-call.glacier.UploadMultipartPart", add_glacier_checksums),
    ("before-call.ec2.CopySnapshot", inject_presigned_url_ec2),
    ("request-created.machinelearning.Predict", switch_host_machinelearning),
    ("needs-retry.s3.UploadPartCopy", check_for_200_error, REGISTER_FIRST),
    ("needs-retry.s3.CopyObject", check_for_200_error, REGISTER_FIRST),
    ("needs-retry.s3.CompleteMultipartUpload", check_for_200_error, REGISTER_FIRST),
    ("choose-signer.cognito-identity.GetId", disable_signing),
    ("choose-signer.cognito-identity.GetOpenIdToken", disable_signing),
    ("choose-signer.cognito-identity.UnlinkIdentity", disable_signing),
    ("choose-signer.cognito-identity.GetCredentialsForIdentity", disable_signing),
    ("choose-signer.sts.AssumeRoleWithSAML", disable_signing),
    ("choose-signer.sts.AssumeRoleWithWebIdentity", disable_signing),
    ("choose-signer", set_operation_specific_signer),
    ("before-parameter-build.s3.HeadObject", sse_md5),
    ("before-parameter-build.s3.GetObject", sse_md5),
    ("before-parameter-build.s3.PutObject", sse_md5),
    ("before-parameter-build.s3.CopyObject", sse_md5),
    ("before-parameter-build.s3.CopyObject", copy_source_sse_md5),
    ("before-parameter-build.s3.CreateMultipartUpload", sse_md5),
    ("before-parameter-build.s3.UploadPart", sse_md5),
    ("before-parameter-build.s3.UploadPartCopy", sse_md5),
    ("before-parameter-build.s3.UploadPartCopy", copy_source_sse_md5),
    ("before-parameter-build.ec2.RunInstances", base64_encode_user_data),
    (
        "before-parameter-build.autoscaling.CreateLaunchConfiguration",
        base64_encode_user_data,
    ),
    ("before-parameter-build.route53", fix_route53_ids),
    ("before-parameter-build.glacier", inject_account_id),
    ("after-call.s3.ListObjects", decode_list_object),
    ("after-call.s3.ListObjectsV2", decode_list_object_v2),
    ("after-call.s3.ListObjectVersions", decode_list_object_versions),
    ("request-created.cloudsearchdomain.Search", change_get_to_post),
    (
        "docs.*.glacier.*.complete-section",
        AutoPopulatedParam(
            "accountId",
            'Note: this parameter is set to "-" by'
            "default if no value is not specified.",
        ).document_auto_populated_param,
    ),
    (
        "docs.*.glacier.UploadArchive.complete-section",
        AutoPopulatedParam("checksum").document_auto_populated_param,
    ),
    (
        "docs.*.glacier.UploadMultipartPart.complete-section",
        AutoPopulatedParam("checksum").document_auto_populated_param,
    ),
    (
        "docs.request-params.glacier.CompleteMultipartUpload.complete-section",
        document_glacier_tree_hash_checksum(),
    ),
    (
        "docs.*.cloudformation.GetTemplate.complete-section",
        document_cloudformation_get_template_return_type,
    ),
    ("docs.*.ec2.RunInstances.complete-section", document_base64_encoding("UserData")),
    (
        "docs.*.autoscaling.CreateLaunchConfiguration.complete-section",
        document_base64_encoding("UserData"),
    ),
    (
        "docs.*.ec2.CopySnapshot.complete-section",
        AutoPopulatedParam("PresignedUrl").document_auto_populated_param,
    ),
    (
        "docs.*.ec2.CopySnapshot.complete-section",
        AutoPopulatedParam("DestinationRegion").document_auto_populated_param,
    ),
    (
        "docs.*.s3.*.complete-section",
        AutoPopulatedParam("SSECustomerKeyMD5").document_auto_populated_param,
    ),
    (
        "docs.*.s3.*.complete-section",
        AutoPopulatedParam("CopySourceSSECustomerKeyMD5").document_auto_populated_param,
    ),
    (
        "docs.*.lambda.UpdateFunctionCode.complete-section",
        document_base64_encoding("ZipFile"),
    ),
    (
        "docs.*.s3.*.complete-section",
        HideParamFromOperations(
            "s3",
            "ContentMD5",
            [
                "DeleteObjects",
                "PutBucketAcl",
                "PutBucketCors",
                "PutBucketLifecycle",
                "PutBucketLogging",
                "PutBucketNotification",
                "PutBucketPolicy",
                "PutBucketReplication",
                "PutBucketRequestPayment",
                "PutBucketTagging",
                "PutBucketVersioning",
                "PutBucketWebsite",
                "PutObjectAcl",
            ],
        ).hide_param,
    ),
    ("creating-client-class.rds", add_generate_db_auth_token),
    ("before-call.rds.CopyDBClusterSnapshot", inject_presigned_url_rds),
    ("before-call.rds.CreateDBCluster", inject_presigned_url_rds),
    ("before-call.rds.CopyDBSnapshot", inject_presigned_url_rds),
    ("before-call.rds.CreateDBInstanceReadReplica", inject_presigned_url_rds),
    (
        "before-call.rds.StartDBInstanceAutomatedBackupsReplication",
        inject_presigned_url_rds,
    ),
    (
        "docs.*.rds.CopyDBClusterSnapshot.complete-section",
        AutoPopulatedParam("PreSignedUrl").document_auto_populated_param,
    ),
    (
        "docs.*.rds.CreateDBCluster.complete-section",
        AutoPopulatedParam("PreSignedUrl").document_auto_populated_param,
    ),
    (
        "docs.*.rds.CopyDBSnapshot.complete-section",
        AutoPopulatedParam("PreSignedUrl").document_auto_populated_param,
    ),
    (
        "docs.*.rds.CreateDBInstanceReadReplica.complete-section",
        AutoPopulatedParam("PreSignedUrl").document_auto_populated_param,
    ),
    (
        "docs.*.rds.StartDBInstanceAutomatedBackupsReplication.complete-section",
        AutoPopulatedParam("PreSignedUrl").document_auto_populated_param,
    ),
    ("before-call.neptune.CopyDBClusterSnapshot", inject_presigned_url_rds),
    ("before-call.neptune.CreateDBCluster", inject_presigned_url_rds),
    (
        "docs.*.neptune.CopyDBClusterSnapshot.complete-section",
        AutoPopulatedParam("PreSignedUrl").document_auto_populated_param,
    ),
    (
        "docs.*.neptune.CreateDBCluster.complete-section",
        AutoPopulatedParam("PreSignedUrl").document_auto_populated_param,
    ),
    ("before-call.docdb.CopyDBClusterSnapshot", inject_presigned_url_rds),
    ("before-call.docdb.CreateDBCluster", inject_presigned_url_rds),
    (
        "docs.*.docdb.CopyDBClusterSnapshot.complete-section",
        AutoPopulatedParam("PreSignedUrl").document_auto_populated_param,
    ),
    (
        "docs.*.docdb.CreateDBCluster.complete-section",
        AutoPopulatedParam("PreSignedUrl").document_auto_populated_param,
    ),
    (
        "docs.title.sms-voice",
        DeprecatedServiceDocumenter("pinpoint-sms-voice").inject_deprecation_notice,
    ),
    ("before-call", inject_api_version_header_if_needed),
]