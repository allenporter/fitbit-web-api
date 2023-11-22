# coding: utf-8

"""
    Fitbit Web API Explorer

    Fitbit provides a Web API for accessing data from Fitbit activity trackers, Aria scale, and manually entered logs. Anyone can develop an application to access and modify a Fitbit user's data on their behalf, so long as it complies with Fitbit Platform Terms of Service. These Swagger UI docs do not currently support making Fitbit API requests directly. In order to make a request, construct a request for the appropriate endpoint using this documentation, and then add an Authorization header to each request with an access token obtained using the steps outlined here: https://dev.fitbit.com/build/reference/web-api/developer-guide/authorization/.  # noqa: E501

    OpenAPI spec version: 1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fitbit_web_api.api_client import ApiClient


class BodyTimeSeriesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_body_resource_by_date_period(
        self, _resource_path, _date, period, **kwargs
    ):  # noqa: E501
        """Get Body Time Series  # noqa: E501

        Returns time series data in the specified range for a given resource in the format requested using units in the unit system that corresponds to the Accept-Language header provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_body_resource_by_date_period(_resource_path, _date, period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str _resource_path: The resource path, which incudes the bmi, fat, or weight options. (required)
        :param date _date: The range start date in the format yyyy-MM-dd or today. (required)
        :param str period: The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_body_resource_by_date_period_with_http_info(
                _resource_path, _date, period, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_body_resource_by_date_period_with_http_info(
                _resource_path, _date, period, **kwargs
            )  # noqa: E501
            return data

    def get_body_resource_by_date_period_with_http_info(
        self, _resource_path, _date, period, **kwargs
    ):  # noqa: E501
        """Get Body Time Series  # noqa: E501

        Returns time series data in the specified range for a given resource in the format requested using units in the unit system that corresponds to the Accept-Language header provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_body_resource_by_date_period_with_http_info(_resource_path, _date, period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str _resource_path: The resource path, which incudes the bmi, fat, or weight options. (required)
        :param date _date: The range start date in the format yyyy-MM-dd or today. (required)
        :param str period: The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["_resource_path", "_date", "period"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_body_resource_by_date_period" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter '_resource_path' is set
        if "_resource_path" not in params or params["_resource_path"] is None:
            raise ValueError(
                "Missing the required parameter `_resource_path` when calling `get_body_resource_by_date_period`"
            )  # noqa: E501
        # verify the required parameter '_date' is set
        if "_date" not in params or params["_date"] is None:
            raise ValueError(
                "Missing the required parameter `_date` when calling `get_body_resource_by_date_period`"
            )  # noqa: E501
        # verify the required parameter 'period' is set
        if "period" not in params or params["period"] is None:
            raise ValueError(
                "Missing the required parameter `period` when calling `get_body_resource_by_date_period`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "_resource_path" in params:
            path_params["resource-path"] = params["_resource_path"]  # noqa: E501
        if "_date" in params:
            path_params["date"] = params["_date"]  # noqa: E501
        if "period" in params:
            path_params["period"] = params["period"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1/user/-/body/{resource-path}/date/{date}/{period}.json",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_body_resource_by_date_range(
        self, _resource_path, base_date, end_date, **kwargs
    ):  # noqa: E501
        """Get Body Time Series  # noqa: E501

        Returns time series data in the specified range for a given resource in the format requested using units in the unit system that corresponds to the Accept-Language header provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_body_resource_by_date_range(_resource_path, base_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str _resource_path: The resource path, which incudes the bmi, fat, or weight options. (required)
        :param date base_date: The range start date in the format yyyy-MM-dd or today. (required)
        :param date end_date: The end date of the range. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_body_resource_by_date_range_with_http_info(
                _resource_path, base_date, end_date, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_body_resource_by_date_range_with_http_info(
                _resource_path, base_date, end_date, **kwargs
            )  # noqa: E501
            return data

    def get_body_resource_by_date_range_with_http_info(
        self, _resource_path, base_date, end_date, **kwargs
    ):  # noqa: E501
        """Get Body Time Series  # noqa: E501

        Returns time series data in the specified range for a given resource in the format requested using units in the unit system that corresponds to the Accept-Language header provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_body_resource_by_date_range_with_http_info(_resource_path, base_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str _resource_path: The resource path, which incudes the bmi, fat, or weight options. (required)
        :param date base_date: The range start date in the format yyyy-MM-dd or today. (required)
        :param date end_date: The end date of the range. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["_resource_path", "base_date", "end_date"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_body_resource_by_date_range" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter '_resource_path' is set
        if "_resource_path" not in params or params["_resource_path"] is None:
            raise ValueError(
                "Missing the required parameter `_resource_path` when calling `get_body_resource_by_date_range`"
            )  # noqa: E501
        # verify the required parameter 'base_date' is set
        if "base_date" not in params or params["base_date"] is None:
            raise ValueError(
                "Missing the required parameter `base_date` when calling `get_body_resource_by_date_range`"
            )  # noqa: E501
        # verify the required parameter 'end_date' is set
        if "end_date" not in params or params["end_date"] is None:
            raise ValueError(
                "Missing the required parameter `end_date` when calling `get_body_resource_by_date_range`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "_resource_path" in params:
            path_params["resource-path"] = params["_resource_path"]  # noqa: E501
        if "base_date" in params:
            path_params["base-date"] = params["base_date"]  # noqa: E501
        if "end_date" in params:
            path_params["end-date"] = params["end_date"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1/user/-/body/{resource-path}/date/{base-date}/{end-date}.json",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
