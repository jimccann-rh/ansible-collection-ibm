#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_healthcheck
short_description: Configure IBM Cloud 'ibm_cis_healthcheck' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_healthcheck' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.4
    - Terraform v0.12.20

options:
    expected_codes:
        description:
            - (Required for new resource) expected_codes
        required: False
        type: str
    method:
        description:
            - method
        required: False
        type: str
        default: GET
    timeout:
        description:
            - timeout
        required: False
        type: int
        default: 5
    retries:
        description:
            - retries
        required: False
        type: int
        default: 2
    allow_insecure:
        description:
            - allow_insecure
        required: False
        type: bool
        default: True
    type:
        description:
            - type
        required: False
        type: str
        default: http
    cis_id:
        description:
            - (Required for new resource) CIS instance crn
        required: False
        type: str
    expected_body:
        description:
            - (Required for new resource) expected_body
        required: False
        type: str
    interval:
        description:
            - interval
        required: False
        type: int
        default: 60
    modified_on:
        description:
            - None
        required: False
        type: str
    path:
        description:
            - path
        required: False
        type: str
        default: /
    description:
        description:
            - description
        required: False
        type: str
    follow_redirects:
        description:
            - follow_redirects
        required: False
        type: bool
        default: True
    created_on:
        description:
            - None
        required: False
        type: str
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
    ibmcloud_api_key:
        description:
            - The API Key used for authentification. This can also be 
              provided via the environment variable 'IC_API_KEY'.
        required: True
    ibmcloud_region:
        description:
            - Denotes which IBM Cloud region to connect to
        default: us-south
        required: False
    ibmcloud_zone:
        description:
            - Denotes which IBM Cloud zone to connect to in multizone 
              environment. This can also be provided via the environmental
              variable 'IC_ZONE'.
        required: False

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('expected_codes', 'str'),
    ('cis_id', 'str'),
    ('expected_body', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'expected_codes',
    'method',
    'timeout',
    'retries',
    'allow_insecure',
    'type',
    'cis_id',
    'expected_body',
    'interval',
    'modified_on',
    'path',
    'description',
    'follow_redirects',
    'created_on',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    expected_codes=dict(
        required=False,
        type='str'),
    method=dict(
        default='GET',
        type='str'),
    timeout=dict(
        default=5,
        type='int'),
    retries=dict(
        default=2,
        type='int'),
    allow_insecure=dict(
        default=True,
        type='bool'),
    type=dict(
        default='http',
        type='str'),
    cis_id=dict(
        required=False,
        type='str'),
    expected_body=dict(
        required=False,
        type='str'),
    interval=dict(
        default=60,
        type='int'),
    modified_on=dict(
        required=False,
        type='str'),
    path=dict(
        default='/',
        type='str'),
    description=dict(
        required=False,
        type='str'),
    follow_redirects=dict(
        default=True,
        type='bool'),
    created_on=dict(
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
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True),
    ibmcloud_region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_zone=dict(
        type='str',
        fallback=(env_fallback, ['IC_ZONE']))
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ibmcloud as ibmcloud

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

    result = ibmcloud.ibmcloud_terraform(
        resource_type='ibm_cis_healthcheck',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.2.4',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=ibmcloud.Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
