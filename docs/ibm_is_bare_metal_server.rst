
ibm_is_bare_metal_server -- Configure IBM Cloud 'ibm_is_bare_metal_server' resource
===================================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_is_bare_metal_server' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/is_bare_metal_server

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.39.1
- Terraform v0.12.20



Parameters
----------

  network_interfaces (False, list, None)
    None


  action (False, str, None)
    This restart/start/stops a bare metal server.


  keys (True, list, None)
    (Required for new resource) SSH key Ids for the bare metal server


  profile (True, str, None)
    (Required for new resource) profile name


  zone (True, str, None)
    (Required for new resource) Zone name


  vpc (False, str, None)
    The VPC the bare metal server is to be a part of


  primary_network_interface (True, list, None)
    (Required for new resource) Primary Network interface info


  image (True, str, None)
    (Required for new resource) image id


  delete_type (False, str, hard)
    Enables stopping type of the bare metal server before deleting


  user_data (False, str, None)
    User data given for the bare metal server


  resource_group (False, str, None)
    Resource group name


  tags (False, list, None)
    Tags for the Bare metal server


  name (False, str, None)
    Bare metal server name


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  generation (False, int, 2)
    The generation of Virtual Private Cloud infrastructure that you want to use. Supported values are 1 for VPC generation 1, and 2 for VPC generation 2 infrastructure. If this value is not specified, 2 is used by default. This can also be provided via the environment variable 'IC_GENERATION'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

