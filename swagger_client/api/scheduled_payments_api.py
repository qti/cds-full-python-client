# coding: utf-8

"""
    Consumer Data Standards

    API sets created by the Australian Consumer Data Standards to meet the needs of the Consumer Data Right  # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: cdr-data61@csiro.au
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ScheduledPaymentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_scheduled_payments(self, account_id, x_v, **kwargs):  # noqa: E501
        """Get Scheduled Payments for Account  # noqa: E501

        Obtain scheduled, outgoing payments for a specific account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_scheduled_payments(account_id, x_v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: ID of the account to get scheduled payments for. Must have previously been returned by one of the account list end points. The account specified is the source account for the payment (required)
        :param str x_v: Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (required)
        :param int page: Page of results to request (standard pagination)
        :param int page_size: Page size to request. Default is 25 (standard pagination)
        :param str x_min_v: Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable.
        :param str x_fapi_interaction_id: An [RFC4122](https://tools.ietf.org/html/rfc4122) UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a [RFC4122] UUID value is required to be provided in the response header to track the interaction.
        :param str x_fapi_auth_date: The time when the customer last logged in to the data recipient. Required for all resource calls (customer present and unattended). Not to be included for unauthenticated calls.
        :param str x_fapi_customer_ip_address: The customer's original IP address if the customer is currently logged in to the data recipient. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls.
        :param str x_cds_client_headers: The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the data recipient. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls.
        :return: ResponseBankingScheduledPaymentsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_scheduled_payments_with_http_info(account_id, x_v, **kwargs)  # noqa: E501
        else:
            (data) = self.list_scheduled_payments_with_http_info(account_id, x_v, **kwargs)  # noqa: E501
            return data

    def list_scheduled_payments_with_http_info(self, account_id, x_v, **kwargs):  # noqa: E501
        """Get Scheduled Payments for Account  # noqa: E501

        Obtain scheduled, outgoing payments for a specific account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_scheduled_payments_with_http_info(account_id, x_v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_id: ID of the account to get scheduled payments for. Must have previously been returned by one of the account list end points. The account specified is the source account for the payment (required)
        :param str x_v: Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (required)
        :param int page: Page of results to request (standard pagination)
        :param int page_size: Page size to request. Default is 25 (standard pagination)
        :param str x_min_v: Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable.
        :param str x_fapi_interaction_id: An [RFC4122](https://tools.ietf.org/html/rfc4122) UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a [RFC4122] UUID value is required to be provided in the response header to track the interaction.
        :param str x_fapi_auth_date: The time when the customer last logged in to the data recipient. Required for all resource calls (customer present and unattended). Not to be included for unauthenticated calls.
        :param str x_fapi_customer_ip_address: The customer's original IP address if the customer is currently logged in to the data recipient. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls.
        :param str x_cds_client_headers: The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the data recipient. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls.
        :return: ResponseBankingScheduledPaymentsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'x_v', 'page', 'page_size', 'x_min_v', 'x_fapi_interaction_id', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_cds_client_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_scheduled_payments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_scheduled_payments`")  # noqa: E501
        # verify the required parameter 'x_v' is set
        if ('x_v' not in params or
                params['x_v'] is None):
            raise ValueError("Missing the required parameter `x_v` when calling `list_scheduled_payments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page-size', params['page_size']))  # noqa: E501

        header_params = {}
        if 'x_v' in params:
            header_params['x-v'] = params['x_v']  # noqa: E501
        if 'x_min_v' in params:
            header_params['x-min-v'] = params['x_min_v']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_cds_client_headers' in params:
            header_params['x-cds-client-headers'] = params['x_cds_client_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/banking/accounts/{accountId}/payments/scheduled', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseBankingScheduledPaymentsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_scheduled_payments_bulk(self, x_v, **kwargs):  # noqa: E501
        """Get Scheduled Payments Bulk  # noqa: E501

        Obtain scheduled payments for multiple, filtered accounts that are the source of funds for the payments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_scheduled_payments_bulk(x_v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_v: Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (required)
        :param str product_category: Used to filter results on the productCategory field applicable to accounts. Any one of the valid values for this field can be supplied. If absent then all accounts returned.
        :param str open_status: Used to filter results according to open/closed status. Values can be OPEN, CLOSED or ALL. If absent then ALL is assumed
        :param bool is_owned: Filters accounts based on whether they are owned by the authorised customer.  True for owned accounts, false for unowned accounts and absent for all accounts
        :param int page: Page of results to request (standard pagination)
        :param int page_size: Page size to request. Default is 25 (standard pagination)
        :param str x_min_v: Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable.
        :param str x_fapi_interaction_id: An [RFC4122](https://tools.ietf.org/html/rfc4122) UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a [RFC4122] UUID value is required to be provided in the response header to track the interaction.
        :param str x_fapi_auth_date: The time when the customer last logged in to the data recipient. Required for all resource calls (customer present and unattended). Not to be included for unauthenticated calls.
        :param str x_fapi_customer_ip_address: The customer's original IP address if the customer is currently logged in to the data recipient. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls.
        :param str x_cds_client_headers: The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the data recipient. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls.
        :return: ResponseBankingScheduledPaymentsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_scheduled_payments_bulk_with_http_info(x_v, **kwargs)  # noqa: E501
        else:
            (data) = self.list_scheduled_payments_bulk_with_http_info(x_v, **kwargs)  # noqa: E501
            return data

    def list_scheduled_payments_bulk_with_http_info(self, x_v, **kwargs):  # noqa: E501
        """Get Scheduled Payments Bulk  # noqa: E501

        Obtain scheduled payments for multiple, filtered accounts that are the source of funds for the payments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_scheduled_payments_bulk_with_http_info(x_v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_v: Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (required)
        :param str product_category: Used to filter results on the productCategory field applicable to accounts. Any one of the valid values for this field can be supplied. If absent then all accounts returned.
        :param str open_status: Used to filter results according to open/closed status. Values can be OPEN, CLOSED or ALL. If absent then ALL is assumed
        :param bool is_owned: Filters accounts based on whether they are owned by the authorised customer.  True for owned accounts, false for unowned accounts and absent for all accounts
        :param int page: Page of results to request (standard pagination)
        :param int page_size: Page size to request. Default is 25 (standard pagination)
        :param str x_min_v: Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable.
        :param str x_fapi_interaction_id: An [RFC4122](https://tools.ietf.org/html/rfc4122) UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a [RFC4122] UUID value is required to be provided in the response header to track the interaction.
        :param str x_fapi_auth_date: The time when the customer last logged in to the data recipient. Required for all resource calls (customer present and unattended). Not to be included for unauthenticated calls.
        :param str x_fapi_customer_ip_address: The customer's original IP address if the customer is currently logged in to the data recipient. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls.
        :param str x_cds_client_headers: The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the data recipient. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls.
        :return: ResponseBankingScheduledPaymentsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_v', 'product_category', 'open_status', 'is_owned', 'page', 'page_size', 'x_min_v', 'x_fapi_interaction_id', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_cds_client_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_scheduled_payments_bulk" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_v' is set
        if ('x_v' not in params or
                params['x_v'] is None):
            raise ValueError("Missing the required parameter `x_v` when calling `list_scheduled_payments_bulk`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_category' in params:
            query_params.append(('product-category', params['product_category']))  # noqa: E501
        if 'open_status' in params:
            query_params.append(('open-status', params['open_status']))  # noqa: E501
        if 'is_owned' in params:
            query_params.append(('is-owned', params['is_owned']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page-size', params['page_size']))  # noqa: E501

        header_params = {}
        if 'x_v' in params:
            header_params['x-v'] = params['x_v']  # noqa: E501
        if 'x_min_v' in params:
            header_params['x-min-v'] = params['x_min_v']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_cds_client_headers' in params:
            header_params['x-cds-client-headers'] = params['x_cds_client_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/banking/payments/scheduled', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseBankingScheduledPaymentsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_scheduled_payments_specific_accounts(self, account_ids, x_v, **kwargs):  # noqa: E501
        """Get Scheduled Payments For Specific Accounts  # noqa: E501

        Obtain scheduled payments for a specified list of accounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_scheduled_payments_specific_accounts(account_ids, x_v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestAccountIds account_ids: Array of specific accountIds to obtain scheduled payments for.  The accounts specified are the source of funds for the payments returned (required)
        :param str x_v: Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (required)
        :param int page: Page of results to request (standard pagination)
        :param int page_size: Page size to request. Default is 25 (standard pagination)
        :param str x_min_v: Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable.
        :param str x_fapi_interaction_id: An [RFC4122](https://tools.ietf.org/html/rfc4122) UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a [RFC4122] UUID value is required to be provided in the response header to track the interaction.
        :param str x_fapi_auth_date: The time when the customer last logged in to the data recipient. Required for all resource calls (customer present and unattended). Not to be included for unauthenticated calls.
        :param str x_fapi_customer_ip_address: The customer's original IP address if the customer is currently logged in to the data recipient. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls.
        :param str x_cds_client_headers: The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the data recipient. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls.
        :return: ResponseBankingScheduledPaymentsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_scheduled_payments_specific_accounts_with_http_info(account_ids, x_v, **kwargs)  # noqa: E501
        else:
            (data) = self.list_scheduled_payments_specific_accounts_with_http_info(account_ids, x_v, **kwargs)  # noqa: E501
            return data

    def list_scheduled_payments_specific_accounts_with_http_info(self, account_ids, x_v, **kwargs):  # noqa: E501
        """Get Scheduled Payments For Specific Accounts  # noqa: E501

        Obtain scheduled payments for a specified list of accounts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_scheduled_payments_specific_accounts_with_http_info(account_ids, x_v, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestAccountIds account_ids: Array of specific accountIds to obtain scheduled payments for.  The accounts specified are the source of funds for the payments returned (required)
        :param str x_v: Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (required)
        :param int page: Page of results to request (standard pagination)
        :param int page_size: Page size to request. Default is 25 (standard pagination)
        :param str x_min_v: Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder should respond with a 406 Not Acceptable.
        :param str x_fapi_interaction_id: An [RFC4122](https://tools.ietf.org/html/rfc4122) UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a [RFC4122] UUID value is required to be provided in the response header to track the interaction.
        :param str x_fapi_auth_date: The time when the customer last logged in to the data recipient. Required for all resource calls (customer present and unattended). Not to be included for unauthenticated calls.
        :param str x_fapi_customer_ip_address: The customer's original IP address if the customer is currently logged in to the data recipient. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls.
        :param str x_cds_client_headers: The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the data recipient. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls.
        :return: ResponseBankingScheduledPaymentsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_ids', 'x_v', 'page', 'page_size', 'x_min_v', 'x_fapi_interaction_id', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_cds_client_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_scheduled_payments_specific_accounts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_ids' is set
        if ('account_ids' not in params or
                params['account_ids'] is None):
            raise ValueError("Missing the required parameter `account_ids` when calling `list_scheduled_payments_specific_accounts`")  # noqa: E501
        # verify the required parameter 'x_v' is set
        if ('x_v' not in params or
                params['x_v'] is None):
            raise ValueError("Missing the required parameter `x_v` when calling `list_scheduled_payments_specific_accounts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page-size', params['page_size']))  # noqa: E501

        header_params = {}
        if 'x_v' in params:
            header_params['x-v'] = params['x_v']  # noqa: E501
        if 'x_min_v' in params:
            header_params['x-min-v'] = params['x_min_v']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_cds_client_headers' in params:
            header_params['x-cds-client-headers'] = params['x_cds_client_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account_ids' in params:
            body_params = params['account_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/banking/payments/scheduled', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseBankingScheduledPaymentsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
