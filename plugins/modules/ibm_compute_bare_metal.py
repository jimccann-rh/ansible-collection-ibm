#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_compute_bare_metal
for_more_info:  refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/compute_bare_metal

short_description: Configure IBM Cloud 'ibm_compute_bare_metal' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_compute_bare_metal' resource
    - This module supports idempotency
requirements:
    - IBM-Cloud terraform-provider-ibm v1.43.0
    - Terraform v0.12.20

options:
    public_subnet:
        description:
            - None
        required: False
        type: str
    domain:
        description:
            - (Required for new resource) Domain name
        required: True
        type: str
    hourly_billing:
        description:
            - Enables hourly billing
        required: False
        type: bool
        default: True
    software_guard_extensions:
        description:
            - None
        required: False
        type: bool
        default: False
    restricted_network:
        description:
            - None
        required: False
        type: bool
        default: False
    quote_id:
        description:
            - Quote ID for Quote based provisioning
        required: False
        type: int
    ssh_key_ids:
        description:
            - SSH KEY IDS list
        required: False
        type: list
        elements: int
    fixed_config_preset:
        description:
            - Fixed config preset value
        required: False
        type: str
    os_reference_code:
        description:
            - OS refernece code value
        required: False
        type: str
    package_key_name:
        description:
            - None
        required: False
        type: str
    private_vlan_id:
        description:
            - None
        required: False
        type: int
    post_install_script_uri:
        description:
            - None
        required: False
        type: str
    tcp_monitoring:
        description:
            - TCP monitoring enabled if set as true
        required: False
        type: bool
        default: False
    storage_groups:
        description:
            - None
        required: False
        type: list
        elements: dict
    ipv6_enabled:
        description:
            - Boolean value true if IPV6 ia enabled or false
        required: False
        type: bool
        default: False
    datacenter:
        description:
            - None
        required: False
        type: str
    block_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    network_speed:
        description:
            - Network speed in MBPS
        required: False
        type: int
        default: 100
    process_key_name:
        description:
            - None
        required: False
        type: str
    public_bandwidth:
        description:
            - None
        required: False
        type: int
    ipv6_static_enabled:
        description:
            - boolean value true if ipv6 static is enabled else false
        required: False
        type: bool
        default: False
    file_storage_ids:
        description:
            - None
        required: False
        type: list
        elements: int
    unbonded_network:
        description:
            - None
        required: False
        type: bool
        default: False
    notes:
        description:
            - Optional notes info
        required: False
        type: str
    gpu_secondary_key_name:
        description:
            - None
        required: False
        type: str
    disk_key_names:
        description:
            - None
        required: False
        type: list
        elements: str
    extended_hardware_testing:
        description:
            - None
        required: False
        type: bool
        default: False
    public_vlan_id:
        description:
            - None
        required: False
        type: int
    private_subnet:
        description:
            - None
        required: False
        type: str
    secondary_ip_count:
        description:
            - Secondary IP addresses count
        required: False
        type: int
    user_metadata:
        description:
            - User metadata info
        required: False
        type: str
    tags:
        description:
            - None
        required: False
        type: list
        elements: str
    image_template_id:
        description:
            - OS image template ID
        required: False
        type: int
    private_network_only:
        description:
            - only private network configured if is true
        required: False
        type: bool
        default: False
    redundant_power_supply:
        description:
            - None
        required: False
        type: bool
    os_key_name:
        description:
            - None
        required: False
        type: str
    gpu_key_name:
        description:
            - None
        required: False
        type: str
    redundant_network:
        description:
            - None
        required: False
        type: bool
        default: False
    hostname:
        description:
            - Host name
        required: False
        type: str
    memory:
        description:
            - None
        required: False
        type: int
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
    ('domain', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'public_subnet',
    'domain',
    'hourly_billing',
    'software_guard_extensions',
    'restricted_network',
    'quote_id',
    'ssh_key_ids',
    'fixed_config_preset',
    'os_reference_code',
    'package_key_name',
    'private_vlan_id',
    'post_install_script_uri',
    'tcp_monitoring',
    'storage_groups',
    'ipv6_enabled',
    'datacenter',
    'block_storage_ids',
    'network_speed',
    'process_key_name',
    'public_bandwidth',
    'ipv6_static_enabled',
    'file_storage_ids',
    'unbonded_network',
    'notes',
    'gpu_secondary_key_name',
    'disk_key_names',
    'extended_hardware_testing',
    'public_vlan_id',
    'private_subnet',
    'secondary_ip_count',
    'user_metadata',
    'tags',
    'image_template_id',
    'private_network_only',
    'redundant_power_supply',
    'os_key_name',
    'gpu_key_name',
    'redundant_network',
    'hostname',
    'memory',
]

# Params for Data source
TL_REQUIRED_PARAMETERS_DS = [
]

TL_ALL_PARAMETERS_DS = [
    'domain',
    'global_identifier',
    'most_recent',
    'hostname',
]

TL_CONFLICTS_MAP = {
    'os_reference_code': ['image_template_id'],
    'image_template_id': ['os_reference_code'],
}

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibm.cloudcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    public_subnet=dict(
        required=False,
        type='str'),
    domain=dict(
        required=False,
        type='str'),
    hourly_billing=dict(
        required=False,
        type='bool'),
    software_guard_extensions=dict(
        required=False,
        type='bool'),
    restricted_network=dict(
        required=False,
        type='bool'),
    quote_id=dict(
        required=False,
        type='int'),
    ssh_key_ids=dict(
        required=False,
        elements='',
        type='list'),
    fixed_config_preset=dict(
        required=False,
        type='str'),
    os_reference_code=dict(
        required=False,
        type='str'),
    package_key_name=dict(
        required=False,
        type='str'),
    private_vlan_id=dict(
        required=False,
        type='int'),
    post_install_script_uri=dict(
        required=False,
        type='str'),
    tcp_monitoring=dict(
        required=False,
        type='bool'),
    storage_groups=dict(
        required=False,
        elements='',
        type='list'),
    ipv6_enabled=dict(
        required=False,
        type='bool'),
    datacenter=dict(
        required=False,
        type='str'),
    block_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    network_speed=dict(
        required=False,
        type='int'),
    process_key_name=dict(
        required=False,
        type='str'),
    public_bandwidth=dict(
        required=False,
        type='int'),
    ipv6_static_enabled=dict(
        required=False,
        type='bool'),
    file_storage_ids=dict(
        required=False,
        elements='',
        type='list'),
    unbonded_network=dict(
        required=False,
        type='bool'),
    notes=dict(
        required=False,
        type='str'),
    gpu_secondary_key_name=dict(
        required=False,
        type='str'),
    disk_key_names=dict(
        required=False,
        elements='',
        type='list'),
    extended_hardware_testing=dict(
        required=False,
        type='bool'),
    public_vlan_id=dict(
        required=False,
        type='int'),
    private_subnet=dict(
        required=False,
        type='str'),
    secondary_ip_count=dict(
        required=False,
        type='int'),
    user_metadata=dict(
        required=False,
        type='str'),
    tags=dict(
        required=False,
        elements='',
        type='list'),
    image_template_id=dict(
        required=False,
        type='int'),
    private_network_only=dict(
        required=False,
        type='bool'),
    redundant_power_supply=dict(
        required=False,
        type='bool'),
    os_key_name=dict(
        required=False,
        type='str'),
    gpu_key_name=dict(
        required=False,
        type='str'),
    redundant_network=dict(
        required=False,
        type='bool'),
    hostname=dict(
        required=False,
        type='str'),
    memory=dict(
        required=False,
        type='int'),
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

    result_ds = ibmcloud_terraform(
        resource_type='ibm_compute_bare_metal',
        tf_type='data',
        parameters=module.params,
        ibm_provider_version='1.43.0',
        tl_required_params=TL_REQUIRED_PARAMETERS_DS,
        tl_all_params=TL_ALL_PARAMETERS_DS)

    if result_ds['rc'] != 0 or (result_ds['rc'] == 0 and (module.params['id'] is not None or module.params['state'] == 'absent')):
        result = ibmcloud_terraform(
            resource_type='ibm_compute_bare_metal',
            tf_type='resource',
            parameters=module.params,
            ibm_provider_version='1.43.0',
            tl_required_params=TL_REQUIRED_PARAMETERS,
            tl_all_params=TL_ALL_PARAMETERS)
        if result['rc'] > 0:
            module.fail_json(
                msg=Terraform.parse_stderr(result['stderr']), **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result_ds)


def main():
    run_module()


if __name__ == '__main__':
    main()
