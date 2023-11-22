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


class AuthorizationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def introspect(self, token, **kwargs):  # noqa: E501
        """Retrieve the active state of an OAuth 2.0 token  # noqa: E501

        Retrieves the active state of an OAuth 2.0 token. It follows https://tools.ietf.org/html/rfc7662.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.introspect(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.introspect_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.introspect_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def introspect_with_http_info(self, token, **kwargs):  # noqa: E501
        """Retrieve the active state of an OAuth 2.0 token  # noqa: E501

        Retrieves the active state of an OAuth 2.0 token. It follows https://tools.ietf.org/html/rfc7662.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.introspect_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["token"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method introspect" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'token' is set
        if "token" not in params or params["token"] is None:
            raise ValueError(
                "Missing the required parameter `token` when calling `introspect`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "token" in params:
            form_params.append(("token", params["token"]))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/x-www-form-urlencoded"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/1.1/oauth2/introspect",
            "POST",
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

    def oauth_token(self, client_id, grant_type, **kwargs):  # noqa: E501
        """Get OAuth 2 access token  # noqa: E501

        Retrieves an OAuth 2 access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_token(client_id, grant_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: This is your Fitbit API application id from your settings on dev.fitbit.com. (required)
        :param str grant_type: Authorization grant type. Valid values are 'authorization_code' and 'refresh_token'. (required)
        :param str authorization: The Authorization header must be set to 'Basic' followed by a space, then the Base64 encoded string of your application's client id and secret concatenated with a colon. For example, 'Basic Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ='. The Base64 encoded string, 'Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ=', is decoded as 'client_id:client secret'.
        :param str code: Authorization code received in the redirect as URI parameter. Required if using the Authorization Code flow.
        :param str expires_in: Specify the desired access token lifetime. Defaults to 28800 for 8 hours. The other valid value is 3600 for 1 hour.
        :param str redirect_uri: Uri to which the access token will be sent if the request is successful. Required if specified in the redirect to the authorization page. Must be exact match.
        :param str refresh_token: Refresh token issued by Fitbit. Required if 'grant_type' is 'refresh_token'.
        :param str state: Required if specified in the redirect uri of the authorization page. Must be an exact match.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.oauth_token_with_http_info(
                client_id, grant_type, **kwargs
            )  # noqa: E501
        else:
            (data) = self.oauth_token_with_http_info(
                client_id, grant_type, **kwargs
            )  # noqa: E501
            return data

    def oauth_token_with_http_info(self, client_id, grant_type, **kwargs):  # noqa: E501
        """Get OAuth 2 access token  # noqa: E501

        Retrieves an OAuth 2 access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth_token_with_http_info(client_id, grant_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: This is your Fitbit API application id from your settings on dev.fitbit.com. (required)
        :param str grant_type: Authorization grant type. Valid values are 'authorization_code' and 'refresh_token'. (required)
        :param str authorization: The Authorization header must be set to 'Basic' followed by a space, then the Base64 encoded string of your application's client id and secret concatenated with a colon. For example, 'Basic Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ='. The Base64 encoded string, 'Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ=', is decoded as 'client_id:client secret'.
        :param str code: Authorization code received in the redirect as URI parameter. Required if using the Authorization Code flow.
        :param str expires_in: Specify the desired access token lifetime. Defaults to 28800 for 8 hours. The other valid value is 3600 for 1 hour.
        :param str redirect_uri: Uri to which the access token will be sent if the request is successful. Required if specified in the redirect to the authorization page. Must be exact match.
        :param str refresh_token: Refresh token issued by Fitbit. Required if 'grant_type' is 'refresh_token'.
        :param str state: Required if specified in the redirect uri of the authorization page. Must be an exact match.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "client_id",
            "grant_type",
            "authorization",
            "code",
            "expires_in",
            "redirect_uri",
            "refresh_token",
            "state",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oauth_token" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'client_id' is set
        if "client_id" not in params or params["client_id"] is None:
            raise ValueError(
                "Missing the required parameter `client_id` when calling `oauth_token`"
            )  # noqa: E501
        # verify the required parameter 'grant_type' is set
        if "grant_type" not in params or params["grant_type"] is None:
            raise ValueError(
                "Missing the required parameter `grant_type` when calling `oauth_token`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "code" in params:
            query_params.append(("code", params["code"]))  # noqa: E501
        if "client_id" in params:
            query_params.append(("client_id", params["client_id"]))  # noqa: E501
        if "expires_in" in params:
            query_params.append(("expires_in", params["expires_in"]))  # noqa: E501
        if "grant_type" in params:
            query_params.append(("grant_type", params["grant_type"]))  # noqa: E501
        if "redirect_uri" in params:
            query_params.append(("redirect_uri", params["redirect_uri"]))  # noqa: E501
        if "refresh_token" in params:
            query_params.append(
                ("refresh_token", params["refresh_token"])
            )  # noqa: E501
        if "state" in params:
            query_params.append(("state", params["state"]))  # noqa: E501

        header_params = {}
        if "authorization" in params:
            header_params["Authorization"] = params["authorization"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/oauth2/token",
            "POST",
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

    def revoke(self, token, **kwargs):  # noqa: E501
        """Revokes consent of the access token or refresh token  # noqa: E501

        Revokes consent of the access token or refresh token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.revoke_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.revoke_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def revoke_with_http_info(self, token, **kwargs):  # noqa: E501
        """Revokes consent of the access token or refresh token  # noqa: E501

        Revokes consent of the access token or refresh token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revoke_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["token"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'" " to method revoke" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'token' is set
        if "token" not in params or params["token"] is None:
            raise ValueError(
                "Missing the required parameter `token` when calling `revoke`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "token" in params:
            form_params.append(("token", params["token"]))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/x-www-form-urlencoded"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/oauth2/revoke",
            "POST",
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
