#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_database
short_description: Configure IBM Cloud 'ibm_database' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_database' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.4.0
    - Terraform v0.12.20

options:
    users:
        description:
            - NA
        required: False
        type: list
        elements: dict
    connectionstrings:
        description:
            - NA
        required: False
        type: list
        elements: dict
    service_endpoints:
        description:
            - Types of the service endpoints. Possible values are 'public', 'private', 'public-and-private'.
        required: False
        type: str
        default: public
    members_disk_allocation_mb:
        description:
            - Disk allocation required for cluster
        required: False
        type: int
    backup_id:
        description:
            - The CRN of backup source database
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    adminuser:
        description:
            - The admin user id for the instance
        required: False
        type: str
    status:
        description:
            - The resource instance status
        required: False
        type: str
    groups:
        description:
            - NA
        required: False
        type: list
        elements: dict
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    resource_group_id:
        description:
            - The id of the resource group in which the Database instance is present
        required: False
        type: str
    version:
        description:
            - The database version to provision if specified
        required: False
        type: str
    members_memory_allocation_mb:
        description:
            - Memory allocation required for cluster
        required: False
        type: int
    tags:
        description:
            - NA
        required: False
        type: list
        elements: str
    whitelist:
        description:
            - NA
        required: False
        type: list
        elements: dict
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    adminpassword:
        description:
            - The admin user password for the instance
        required: False
        type: str
    location:
        description:
            - (Required for new resource) The location or the region in which Database instance exists
        required: False
        type: str
    key_protect_key:
        description:
            - The CRN of Key protect key
        required: False
        type: str
    name:
        description:
            - (Required for new resource) Resource instance name for example, my Database instance
        required: False
        type: str
    key_protect_instance:
        description:
            - The CRN of Key protect instance
        required: False
        type: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about the resource
        required: False
        type: str
    remote_leader_id:
        description:
            - The CRN of leader database
        required: False
        type: str
    plan:
        description:
            - (Required for new resource) The plan type of the Database instance
        required: False
        type: str
    guid:
        description:
            - Unique identifier of resource instance
        required: False
        type: str
    members_cpu_allocation_count:
        description:
            - CPU allocation required for cluster
        required: False
        type: int
    service:
        description:
            - (Required for new resource) The name of the Cloud Internet database service
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
    ('location', 'str'),
    ('name', 'str'),
    ('plan', 'str'),
    ('service', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'users',
    'connectionstrings',
    'service_endpoints',
    'members_disk_allocation_mb',
    'backup_id',
    'resource_status',
    'adminuser',
    'status',
    'groups',
    'resource_group_name',
    'resource_group_id',
    'version',
    'members_memory_allocation_mb',
    'tags',
    'whitelist',
    'resource_crn',
    'adminpassword',
    'location',
    'key_protect_key',
    'name',
    'key_protect_instance',
    'resource_name',
    'resource_controller_url',
    'remote_leader_id',
    'plan',
    'guid',
    'members_cpu_allocation_count',
    'service',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    users=dict(
        required=False,
        elements='',
        type='list'),
    connectionstrings=dict(
        required=False,
        elements='',
        type='list'),
    service_endpoints=dict(
        default='public',
        type='str'),
    members_disk_allocation_mb=dict(
        required=False,
        type='int'),
    backup_id=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    adminuser=dict(
        required=False,
        type='str'),
    status=dict(
        required=False,
        type='str'),
    groups=dict(
        required=False,
        elements='',
        type='list'),
    resource_group_name=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    version=dict(
        required=False,
        type='str'),
    members_memory_allocation_mb=dict(
        required=False,
        type='int'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    whitelist=dict(
        required=False,
        elements='',
        type='list'),
    resource_crn=dict(
        required=False,
        type='str'),
    adminpassword=dict(
        required=False,
        type='str'),
    location=dict(
        required=False,
        type='str'),
    key_protect_key=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    key_protect_instance=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    remote_leader_id=dict(
        required=False,
        type='str'),
    plan=dict(
        required=False,
        type='str'),
    guid=dict(
        required=False,
        type='str'),
    members_cpu_allocation_count=dict(
        required=False,
        type='int'),
    service=dict(
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
        resource_type='ibm_database',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.4.0',
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
