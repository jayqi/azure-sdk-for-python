# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._component_linked_storage_accounts_operations import build_create_and_update_request, build_delete_request, build_get_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ComponentLinkedStorageAccountsOperations:
    """ComponentLinkedStorageAccountsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.applicationinsights.v2020_03_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        resource_name: str,
        storage_type: Union[str, "_models.StorageType"],
        **kwargs: Any
    ) -> "_models.ComponentLinkedStorageAccounts":
        """Returns the current linked storage settings for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ComponentLinkedStorageAccounts, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ComponentLinkedStorageAccounts"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            storage_type=storage_type,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseLinkedStorage, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ComponentLinkedStorageAccounts', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/linkedStorageAccounts/{storageType}'}  # type: ignore


    @distributed_trace_async
    async def create_and_update(
        self,
        resource_group_name: str,
        resource_name: str,
        storage_type: Union[str, "_models.StorageType"],
        linked_storage_accounts_properties: "_models.ComponentLinkedStorageAccounts",
        **kwargs: Any
    ) -> "_models.ComponentLinkedStorageAccounts":
        """Replace current linked storage account for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :param linked_storage_accounts_properties: Properties that need to be specified to update
         linked storage accounts for an Application Insights component.
        :type linked_storage_accounts_properties:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ComponentLinkedStorageAccounts, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ComponentLinkedStorageAccounts"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(linked_storage_accounts_properties, 'ComponentLinkedStorageAccounts')

        request = build_create_and_update_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            storage_type=storage_type,
            content_type=content_type,
            json=_json,
            template_url=self.create_and_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseLinkedStorage, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ComponentLinkedStorageAccounts', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_and_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/linkedStorageAccounts/{storageType}'}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        resource_name: str,
        storage_type: Union[str, "_models.StorageType"],
        linked_storage_accounts_properties: "_models.ComponentLinkedStorageAccountsPatch",
        **kwargs: Any
    ) -> "_models.ComponentLinkedStorageAccounts":
        """Update linked storage accounts for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :param linked_storage_accounts_properties: Properties that need to be specified to update a
         linked storage accounts for an Application Insights component.
        :type linked_storage_accounts_properties:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccountsPatch
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ComponentLinkedStorageAccounts, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ComponentLinkedStorageAccounts"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(linked_storage_accounts_properties, 'ComponentLinkedStorageAccountsPatch')

        request = build_update_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            storage_type=storage_type,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseLinkedStorage, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ComponentLinkedStorageAccounts', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/linkedStorageAccounts/{storageType}'}  # type: ignore


    @distributed_trace_async
    async def delete(
        self,
        resource_group_name: str,
        resource_name: str,
        storage_type: Union[str, "_models.StorageType"],
        **kwargs: Any
    ) -> None:
        """Delete linked storage accounts for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            storage_type=storage_type,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseLinkedStorage, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/linkedStorageAccounts/{storageType}'}  # type: ignore

