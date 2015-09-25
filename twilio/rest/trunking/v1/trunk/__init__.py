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
from twilio.rest.trunking.v1.trunk.credential_list import CredentialListList
from twilio.rest.trunking.v1.trunk.ip_access_control_list import IpAccessControlListList
from twilio.rest.trunking.v1.trunk.origination_url import OriginationUrlList
from twilio.rest.trunking.v1.trunk.phone_number import PhoneNumberList


class TrunkList(ListResource):

    def __init__(self, version):
        """
        Initialize the TrunkList
        
        :param Version version: Version that contains the resource
        
        :returns: TrunkList
        :rtype: TrunkList
        """
        super(TrunkList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = '/Trunks'.format(**self._kwargs)

    def create(self, friendly_name=values.unset, domain_name=values.unset,
               disaster_recovery_url=values.unset,
               disaster_recovery_method=values.unset, recording=values.unset,
               secure=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'DomainName': domain_name,
            'DisasterRecoveryUrl': disaster_recovery_url,
            'DisasterRecoveryMethod': disaster_recovery_method,
            'Recording': recording,
            'Secure': secure,
        })
        
        return self._version.create(
            TrunkInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            TrunkInstance,
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
            TrunkInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a TrunkContext
        
        :param sid: Contextual sid
        
        :returns: TrunkContext
        :rtype: TrunkContext
        """
        return TrunkContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.TrunkList>'


class TrunkContext(InstanceContext):

    def __init__(self, version, sid):
        super(TrunkContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'sid': sid,
        }
        self._uri = "/Trunks/{sid}".format(**self._kwargs)
        
        # Dependents
        self._origination_urls = None
        self._credentials_lists = None
        self._ip_access_control_lists = None
        self._phone_numbers = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            TrunkInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._version.delete("delete", self._uri)

    def update(self, friendly_name=values.unset, domain_name=values.unset,
               disaster_recovery_url=values.unset,
               disaster_recovery_method=values.unset, recording=values.unset,
               secure=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'DomainName': domain_name,
            'DisasterRecoveryUrl': disaster_recovery_url,
            'DisasterRecoveryMethod': disaster_recovery_method,
            'Recording': recording,
            'Secure': secure,
        })
        
        return self._version.update(
            TrunkInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def origination_urls(self):
        if self._origination_urls is None:
            self._origination_urls = OriginationUrlList(
                self._version,
                trunk_sid=self._kwargs['sid'],
            )
        return self._origination_urls

    @property
    def credentials_lists(self):
        if self._credentials_lists is None:
            self._credentials_lists = CredentialListList(
                self._version,
                trunk_sid=self._kwargs['sid'],
            )
        return self._credentials_lists

    @property
    def ip_access_control_lists(self):
        if self._ip_access_control_lists is None:
            self._ip_access_control_lists = IpAccessControlListList(
                self._version,
                trunk_sid=self._kwargs['sid'],
            )
        return self._ip_access_control_lists

    @property
    def phone_numbers(self):
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(
                self._version,
                trunk_sid=self._kwargs['sid'],
            )
        return self._phone_numbers


class TrunkInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        super(TrunkInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'domain_name': payload['domain_name'],
            'disaster_recovery_method': payload['disaster_recovery_method'],
            'disaster_recovery_url': payload['disaster_recovery_url'],
            'friendly_name': payload['friendly_name'],
            'secure': payload['secure'],
            'recording': payload['recording'],
            'auth_type': payload['auth_type'],
            'auth_type_set': payload['auth_type_set'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'sid': payload['sid'],
            'url': payload['url'],
            'links': payload['links'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = TrunkContext(
                self._version,
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def domain_name(self):
        """ The domain_name """
        return self._properties['domain_name']

    @property
    def disaster_recovery_method(self):
        """ The disaster_recovery_method """
        return self._properties['disaster_recovery_method']

    @property
    def disaster_recovery_url(self):
        """ The disaster_recovery_url """
        return self._properties['disaster_recovery_url']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def secure(self):
        """ The secure """
        return self._properties['secure']

    @property
    def recording(self):
        """ The recording """
        return self._properties['recording']

    @property
    def auth_type(self):
        """ The auth_type """
        return self._properties['auth_type']

    @property
    def auth_type_set(self):
        """ The auth_type_set """
        return self._properties['auth_type_set']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def url(self):
        """ The url """
        return self._properties['url']

    @property
    def links(self):
        """ The links """
        return self._properties['links']

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()

    def update(self, friendly_name=values.unset, domain_name=values.unset,
               disaster_recovery_url=values.unset,
               disaster_recovery_method=values.unset, recording=values.unset,
               secure=values.unset):
        self._context.update(
            friendly_name=friendly_name,
            domain_name=domain_name,
            disaster_recovery_url=disaster_recovery_url,
            disaster_recovery_method=disaster_recovery_method,
            recording=recording,
            secure=secure,
        )

    @property
    def origination_urls(self):
        return self._context.origination_urls

    @property
    def credentials_lists(self):
        return self._context.credentials_lists

    @property
    def ip_access_control_lists(self):
        return self._context.ip_access_control_lists

    @property
    def phone_numbers(self):
        return self._context.phone_numbers
