
ibm_space -- Configure IBM Cloud 'ibm_space' resource
=====================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_space' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/space

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.39.1
- Terraform v0.12.20



Parameters
----------

  managers (False, list, None)
    The IBMID of the users who will have manager role in this space, ex - user@example.com


  developers (False, list, None)
    The IBMID of the users who will have developer role in this space, ex - user@example.com


  space_quota (False, str, None)
    The name of the Space Quota Definition


  tags (False, list, None)
    None


  name (True, str, None)
    (Required for new resource) The name for the space


  org (True, str, None)
    (Required for new resource) The org this space belongs to


  auditors (False, list, None)
    The IBMID of the users who will have auditor role in this space, ex - user@example.com


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

