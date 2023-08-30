""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
import requests
from connectors.core.connector import get_logger, ConnectorError
logger = get_logger('binaryedge')


class BinaryEdge(object):

    def __init__(self, config):
        self.server_url = config.get('server_url').strip()
        self.api_key = config.get('api_key')
        self.headers = {'accept': 'application/json', 'X-Key': self.api_key}
        if not self.server_url.startswith('https://'):
            self.server_url = 'https://{0}/'.format(self.server_url)
        self.verify_ssl = config.get('verify_ssl')

    def make_api_call(self, endpoint=None, method='GET', headers=None, health_check=False):
        url = self.server_url + endpoint
        logger.debug('Final url to make rest call is: {0}'.format(url))
        if headers:
            self.headers.update(headers)
        try:
            logger.debug('Making a request with {0} method and {1} headers.'.format(method, self.headers))
            response = requests.request(method, url, headers=self.headers, verify=self.verify_ssl)
            if response.status_code in [200]:
                if health_check:
                    return response
                try:
                    logger.debug(
                        'Converting the response into JSON format after returning with status code: {0}'.format(
                            response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response})
        except Exception as e:
            logger.exception(str(e))
            raise ConnectorError(str(e))


def get_host_details(config, params):
    obj = BinaryEdge(config)
    endpoint = '/v2/query/ip/{0}'.format(params.get('ip_address'))
    return obj.make_api_call(endpoint=endpoint)


def get_ip_risk_score_details(config, params):
    obj = BinaryEdge(config)
    endpoint = '/v2/query/score/ip/{0}'.format(params.get('ip_address'))
    return obj.make_api_call(endpoint=endpoint)


def get_list_of_affect_cve_details(config, params):
    obj = BinaryEdge(config)
    endpoint = '/v2/query/cve/ip/{0}'.format(params.get('ip_address'))
    return obj.make_api_call(endpoint=endpoint)


def get_subdomain_details(config, params):
    obj = BinaryEdge(config)
    endpoint = '/v2/query/domains/subdomain/{0}'.format(params.get('domain'))
    return obj.make_api_call(endpoint=endpoint)


def get_dns_details(config, params):
    obj = BinaryEdge(config)
    endpoint = '/v2/query/domains/dns/{0}'.format(params.get('domain'))
    return obj.make_api_call(endpoint=endpoint)


def _check_health(config):
    try:
        obj = BinaryEdge(config)
        obj.make_api_call(endpoint='/v2/user/subscription', health_check=True)
        return True
    except Exception as err:
        logger.exception('Health check failed with: {0}'.format(err))
        raise ConnectorError('Health check failed with: {0}'.format(err))


operations = {
    'get_host_details': get_host_details,
    'get_ip_risk_score_details': get_ip_risk_score_details,
    "get_list_of_affect_cve_details": get_list_of_affect_cve_details,
    "get_subdomain_details": get_subdomain_details,
    "get_dns_details": get_dns_details
}
