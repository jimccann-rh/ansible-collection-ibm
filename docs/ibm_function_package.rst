
ibm_function_package -- Configure IBM Cloud 'ibm_function_package' resource
===========================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_function_package' resource

This module supports idempotency


ForMoreInfoRefer
----------------
refer - https://registry.terraform.io/providers/IBM-Cloud/ibm/latest/docs/resources/function_package

Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.39.1
- Terraform v0.12.20



Parameters
----------

  namespace (True, str, None)
    (Required for new resource) IBM Cloud function namespace.


  user_defined_parameters (False, str, [])
    Parameters values in KEY VALUE format. Parameter bindings included in the context passed to the package.


  name (True, str, None)
    (Required for new resource) Name of package.


  publish (False, bool, False)
    Package visibilty.


  user_defined_annotations (False, str, [])
    Annotation values in KEY VALUE format.


  bind_package_name (False, str, None)
    Name of package to be binded.


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  function_namespace (True, any, None)
    The namespace in IBM Cloud™ Functions where you want to create your resources. This can also be provided via the environment variable 'FUNCTION_NAMESPACE'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

