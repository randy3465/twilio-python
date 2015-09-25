# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class IpAddressList(ListResource):

    def __init__(self, version, account_sid, ip_access_control_list_sid):
        """
        Initialize the IpAddressList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        :param ip_access_control_list_sid: Contextual ip_access_control_list_sid
        
        :returns: IpAddressList
        :rtype: IpAddressList
        """
        super(IpAddressList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'ip_access_control_list_sid': ip_access_control_list_sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json'.format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            IpAddressInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            IpAddressInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, friendly_name, ip_address):
        data = values.of({
            'FriendlyName': friendly_name,
            'IpAddress': ip_address,
        })
        
        return self._version.create(
            IpAddressInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __call__(self, sid):
        """
        Constructs a IpAddressContext
        
        :param sid: Contextual sid
        
        :returns: IpAddressContext
        :rtype: IpAddressContext
        """
        return IpAddressContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAddressList>'


class IpAddressContext(InstanceContext):

    def __init__(self, version, account_sid, ip_access_control_list_sid, sid):
        super(IpAddressContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'ip_access_control_list_sid': ip_access_control_list_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json".format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            IpAddressInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, ip_address, friendly_name):
        data = values.of({
            'IpAddress': ip_address,
            'FriendlyName': friendly_name,
        })
        
        return self._version.update(
            IpAddressInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._version.delete("delete", self._uri)


class IpAddressInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, ip_access_control_list_sid,
                 sid=None):
        super(IpAddressInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'ip_address': payload['ip_address'],
            'ip_access_control_list_sid': payload['ip_access_control_list_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'ip_access_control_list_sid': ip_access_control_list_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = IpAddressContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['ip_access_control_list_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def ip_address(self):
        """ The ip_address """
        return self._properties['ip_address']

    @property
    def ip_access_control_list_sid(self):
        """ The ip_access_control_list_sid """
        return self._properties['ip_access_control_list_sid']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    def update(self, ip_address, friendly_name):
        self._context.update(
            ip_address,
            friendly_name,
        )

    def delete(self):
        self._context.delete()
