#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_container_cluster
short_description: Configure IBM Cloud 'ibm_container_cluster' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_container_cluster' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.2.4
    - Terraform v0.12.20

options:
    hardware:
        description:
            - (Required for new resource) 
        required: False
        type: str
    ingress_hostname:
        description:
            - None
        required: False
        type: str
    region:
        description:
            - The cluster region
        required: False
        type: str
    workers_info:
        description:
            - The IDs of the worker node
        required: False
        type: list
        elements: dict
    machine_type:
        description:
            - None
        required: False
        type: str
    resource_group_id:
        description:
            - ID of the resource group.
        required: False
        type: str
    public_service_endpoint:
        description:
            - None
        required: False
        type: bool
    datacenter:
        description:
            - (Required for new resource) The datacenter where this cluster will be deployed
        required: False
        type: str
    update_all_workers:
        description:
            - None
        required: False
        type: bool
        default: False
    private_vlan_id:
        description:
            - None
        required: False
        type: str
    org_guid:
        description:
            - The bluemix organization guid this cluster belongs to
        required: False
        type: str
    space_guid:
        description:
            - The bluemix space guid this cluster belongs to
        required: False
        type: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    private_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    resource_status:
        description:
            - The status of the resource
        required: False
        type: str
    worker_num:
        description:
            - Number of worker nodes
        required: False
        type: int
        default: 0
    ingress_secret:
        description:
            - None
        required: False
        type: str
    no_subnet:
        description:
            - None
        required: False
        type: bool
        default: False
    worker_pools:
        description:
            - None
        required: False
        type: list
        elements: dict
    albs:
        description:
            - None
        required: False
        type: list
        elements: dict
    kube_version:
        description:
            - None
        required: False
        type: str
    public_vlan_id:
        description:
            - None
        required: False
        type: str
    server_url:
        description:
            - None
        required: False
        type: str
    public_service_endpoint_url:
        description:
            - None
        required: False
        type: str
    resource_name:
        description:
            - The name of the resource
        required: False
        type: str
    resource_crn:
        description:
            - The crn of the resource
        required: False
        type: str
    default_pool_size:
        description:
            - The size of the default worker pool
        required: False
        type: int
        default: 1
    resource_group_name:
        description:
            - The resource group name in which resource is provisioned
        required: False
        type: str
    name:
        description:
            - (Required for new resource) The cluster name
        required: False
        type: str
    webhook:
        description:
            - None
        required: False
        type: list
        elements: dict
    private_service_endpoint:
        description:
            - None
        required: False
        type: bool
    gateway_enabled:
        description:
            - Set true for gateway enabled clusters
        required: False
        type: bool
        default: False
    resource_controller_url:
        description:
            - The URL of the IBM Cloud dashboard that can be used to explore and view details about this cluster
        required: False
        type: str
    disk_encryption:
        description:
            - None
        required: False
        type: bool
        default: True
    is_trusted:
        description:
            - None
        required: False
        type: bool
    account_guid:
        description:
            - The bluemix account guid this cluster belongs to
        required: False
        type: str
    wait_time_minutes:
        description:
            - None
        required: False
        type: int
        default: 90
    crn:
        description:
            - CRN of resource instance
        required: False
        type: str
    billing:
        description:
            - None
        required: False
        type: str
    subnet_id:
        description:
            - None
        required: False
        type: list
        elements: str
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
    ('hardware', 'str'),
    ('datacenter', 'str'),
    ('name', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'hardware',
    'ingress_hostname',
    'region',
    'workers_info',
    'machine_type',
    'resource_group_id',
    'public_service_endpoint',
    'datacenter',
    'update_all_workers',
    'private_vlan_id',
    'org_guid',
    'space_guid',
    'tags',
    'private_service_endpoint_url',
    'resource_status',
    'worker_num',
    'ingress_secret',
    'no_subnet',
    'worker_pools',
    'albs',
    'kube_version',
    'public_vlan_id',
    'server_url',
    'public_service_endpoint_url',
    'resource_name',
    'resource_crn',
    'default_pool_size',
    'resource_group_name',
    'name',
    'webhook',
    'private_service_endpoint',
    'gateway_enabled',
    'resource_controller_url',
    'disk_encryption',
    'is_trusted',
    'account_guid',
    'wait_time_minutes',
    'crn',
    'billing',
    'subnet_id',
]

# define available arguments/parameters a user can pass to the module
from ansible.module_utils.basic import env_fallback
module_args = dict(
    hardware=dict(
        required=False,
        type='str'),
    ingress_hostname=dict(
        required=False,
        type='str'),
    region=dict(
        required=False,
        type='str'),
    workers_info=dict(
        required=False,
        elements='',
        type='list'),
    machine_type=dict(
        required=False,
        type='str'),
    resource_group_id=dict(
        required=False,
        type='str'),
    public_service_endpoint=dict(
        required=False,
        type='bool'),
    datacenter=dict(
        required=False,
        type='str'),
    update_all_workers=dict(
        default=False,
        type='bool'),
    private_vlan_id=dict(
        required=False,
        type='str'),
    org_guid=dict(
        required=False,
        type='str'),
    space_guid=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    private_service_endpoint_url=dict(
        required=False,
        type='str'),
    resource_status=dict(
        required=False,
        type='str'),
    worker_num=dict(
        default=0,
        type='int'),
    ingress_secret=dict(
        required=False,
        type='str'),
    no_subnet=dict(
        default=False,
        type='bool'),
    worker_pools=dict(
        required=False,
        elements='',
        type='list'),
    albs=dict(
        required=False,
        elements='',
        type='list'),
    kube_version=dict(
        required=False,
        type='str'),
    public_vlan_id=dict(
        required=False,
        type='str'),
    server_url=dict(
        required=False,
        type='str'),
    public_service_endpoint_url=dict(
        required=False,
        type='str'),
    resource_name=dict(
        required=False,
        type='str'),
    resource_crn=dict(
        required=False,
        type='str'),
    default_pool_size=dict(
        default=1,
        type='int'),
    resource_group_name=dict(
        required=False,
        type='str'),
    name=dict(
        required=False,
        type='str'),
    webhook=dict(
        required=False,
        elements='',
        type='list'),
    private_service_endpoint=dict(
        required=False,
        type='bool'),
    gateway_enabled=dict(
        default=False,
        type='bool'),
    resource_controller_url=dict(
        required=False,
        type='str'),
    disk_encryption=dict(
        default=True,
        type='bool'),
    is_trusted=dict(
        required=False,
        type='bool'),
    account_guid=dict(
        required=False,
        type='str'),
    wait_time_minutes=dict(
        default=90,
        type='int'),
    crn=dict(
        required=False,
        type='str'),
    billing=dict(
        required=False,
        type='str'),
    subnet_id=dict(
        required=False,
        elements='',
        type='list'),
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
        resource_type='ibm_container_cluster',
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
