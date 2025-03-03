#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cdn
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/cdn

short_description: Configure IBM Cloud 'ibm_cdn' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cdn' resource
    - This module does not support idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.43.0
    - Terraform v0.12.20

options:
    vendor_name:
        description:
            - Vendor name
        required: False
        type: str
        default: akamai
    bucket_name:
        description:
            - Bucket name
        required: False
        type: str
    http_port:
        description:
            - HTTP port number
        required: False
        type: int
        default: 80
    performance_configuration:
        description:
            - performance configuration info
        required: False
        type: str
        default: General web delivery
    host_name:
        description:
            - (Required for new resource) Host name
        required: True
        type: str
    cname:
        description:
            - cname info
        required: False
        type: str
    header:
        description:
            - Header info
        required: False
        type: str
    respect_headers:
        description:
            - respect headers info
        required: False
        type: bool
        default: True
    path:
        description:
            - Path details
        required: False
        type: str
        default: /*
    origin_type:
        description:
            - Origin type info
        required: False
        type: str
        default: HOST_SERVER
    origin_address:
        description:
            - (Required for new resource) origin address info
        required: True
        type: str
    file_extension:
        description:
            - File extension info
        required: False
        type: str
    certificate_type:
        description:
            - Certificate type
        required: False
        type: str
    protocol:
        description:
            - Protocol name
        required: False
        type: str
        default: HTTP
    https_port:
        description:
            - HTTPS port number
        required: False
        type: int
        default: 443
    cache_key_query_rule:
        description:
            - query rule info
        required: False
        type: str
        default: include-all
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('host_name', 'str'),
    ('origin_address', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'vendor_name',
    'bucket_name',
    'http_port',
    'performance_configuration',
    'host_name',
    'cname',
    'header',
    'respect_headers',
    'path',
    'origin_type',
    'origin_address',
    'file_extension',
    'certificate_type',
    'protocol',
    'https_port',
    'cache_key_query_rule',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
]

TL_CONFLICTS_MAP = {
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    vendor_name=dict(
        required=False,
        type='str'),
    bucket_name=dict(
        required=False,
        type='str'),
    http_port=dict(
        required=False,
        type='int'),
    performance_configuration=dict(
        required=False,
        type='str'),
    host_name=dict(
        required=False,
        type='str'),
    cname=dict(
        required=False,
        type='str'),
    header=dict(
        required=False,
        type='str'),
    respect_headers=dict(
        required=False,
        type='bool'),
    path=dict(
        required=False,
        type='str'),
    origin_type=dict(
        required=False,
        type='str'),
    origin_address=dict(
        required=False,
        type='str'),
    file_extension=dict(
        required=False,
        type='str'),
    certificate_type=dict(
        required=False,
        type='str'),
    protocol=dict(
        required=False,
        type='str'),
    https_port=dict(
        required=False,
        type='int'),
    cache_key_query_rule=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    conflicts = {}
    if len(TL_CONFLICTS_MAP) != 0:
        for arg in TL_CONFLICTS_MAP:
            if module.params[arg]:
                for conflict in TL_CONFLICTS_MAP[arg]:
                    try:
                        if module.params[conflict]:
                            conflicts[arg] = conflict
                    except KeyError:
                        pass
    if len(conflicts):
        module.fail_json(msg=("conflicts exist: {}".format(conflicts)))

    result = ibmcloud_terraform(
        resource_type='ibm_cdn',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.43.0',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
