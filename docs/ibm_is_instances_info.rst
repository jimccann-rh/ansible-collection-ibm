
ibm_is_instances_info -- Retrieve IBM Cloud 'ibm_is_instances' resource
=======================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Retrieve an IBM Cloud 'ibm_is_instances' resource


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/data-sources/is_instances

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.39.1
- Terraform v0.12.20



Parameters
----------

  instance_group_name (False, str, None)
    Instance group name to filter the instances attached to it


  vpc_name (False, str, None)
    Name of the vpc to filter the instances attached to it


  resource_group (False, str, None)
    Instance resource group


  dedicated_host_name (False, str, None)
    Name of the dedicated host to filter the instances attached to it


  placement_group_name (False, str, None)
    Name of the placement group to filter the instances attached to it


  placement_group (False, str, None)
    ID of the placement group to filter the instances attached to it


  instance_group (False, str, None)
    Instance group ID to filter the instances attached to it


  vpc_crn (False, str, None)
    VPC CRN to filter the instances attached to it


  dedicated_host (False, str, None)
    ID of the dedicated host to filter the instances attached to it


  vpc (False, str, None)
    VPC ID to filter the instances attached to it


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

