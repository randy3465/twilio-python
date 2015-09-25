# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.api.v2010.account.call.feedback import FeedbackContext
from twilio.rest.api.v2010.account.call.feedback_summary import FeedbackSummaryList
from twilio.rest.api.v2010.account.call.notification import NotificationList
from twilio.rest.api.v2010.account.call.recording import RecordingList
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class CallList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the CallList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: CallList
        :rtype: CallList
        """
        super(CallList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls.json'.format(**self._kwargs)
        
        # Components
        self._feedback_summaries = None

    def create(self, to, from_, method=values.unset, fallback_url=values.unset,
               fallback_method=values.unset, status_callback=values.unset,
               status_callback_method=values.unset, send_digits=values.unset,
               if_machine=values.unset, timeout=values.unset, record=values.unset,
               url=values.unset, application_sid=values.unset):
        data = values.of({
            'To': to,
            'From': from_,
            'Url': url,
            'ApplicationSid': application_sid,
            'Method': method,
            'FallbackUrl': fallback_url,
            'FallbackMethod': fallback_method,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'SendDigits': send_digits,
            'IfMachine': if_machine,
            'Timeout': timeout,
            'Record': record,
        })
        
        return self._version.create(
            CallInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, to=values.unset, from_=values.unset,
             parent_call_sid=values.unset, status=values.unset,
             start_time=values.unset, end_time=values.unset, limit=None,
             page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'To': to,
            'From': from_,
            'ParentCallSid': parent_call_sid,
            'Status': status,
            'StartTime': serialize.iso8601_date(start_time),
            'EndTime': serialize.iso8601_date(end_time),
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            CallInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, to=values.unset, from_=values.unset,
             parent_call_sid=values.unset, status=values.unset,
             start_time=values.unset, end_time=values.unset, page_token=None,
             page_number=None, page_size=None, **kwargs):
        params = values.of({
            'To': to,
            'From': from_,
            'ParentCallSid': parent_call_sid,
            'Status': status,
            'StartTime': serialize.iso8601_date(start_time),
            'EndTime': serialize.iso8601_date(end_time),
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            CallInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    @property
    def feedback_summaries(self):
        if self._feedback_summaries is None:
            self._feedback_summaries = FeedbackSummaryList(self._version, **self._kwargs)
        return self._feedback_summaries

    def __call__(self, sid):
        """
        Constructs a CallContext
        
        :param sid: Contextual sid
        
        :returns: CallContext
        :rtype: CallContext
        """
        return CallContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CallList>'


class CallContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        super(CallContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/Calls/{sid}.json".format(**self._kwargs)
        
        # Dependents
        self._recordings = None
        self._notifications = None
        self._feedback = None

    def delete(self):
        return self._version.delete("delete", self._uri)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            CallInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, url=values.unset, method=values.unset, status=values.unset,
               fallback_url=values.unset, fallback_method=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        data = values.of({
            'Url': url,
            'Method': method,
            'Status': status,
            'FallbackUrl': fallback_url,
            'FallbackMethod': fallback_method,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })
        
        return self._version.update(
            CallInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def recordings(self):
        if self._recordings is None:
            self._recordings = RecordingList(
                self._version,
                account_sid=self._kwargs['account_sid'],
                call_sid=self._kwargs['sid'],
            )
        return self._recordings

    @property
    def notifications(self):
        if self._notifications is None:
            self._notifications = NotificationList(
                self._version,
                account_sid=self._kwargs['account_sid'],
                call_sid=self._kwargs['sid'],
            )
        return self._notifications

    @property
    def feedback(self):
        if self._feedback is None:
            self._feedback = FeedbackContext(
                self._version,
                account_sid=self._kwargs['account_sid'],
                call_sid=self._kwargs['sid'],
            )
        return self._feedback


class CallInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        super(CallInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'annotation': payload['annotation'],
            'answered_by': payload['answered_by'],
            'api_version': payload['api_version'],
            'caller_name': payload['caller_name'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'direction': payload['direction'],
            'duration': payload['duration'],
            'end_time': deserialize.rfc2822_datetime(payload['end_time']),
            'forwarded_from': payload['forwarded_from'],
            'from_': payload['from'],
            'from_formatted': payload['from_formatted'],
            'group_sid': payload['group_sid'],
            'parent_call_sid': payload['parent_call_sid'],
            'phone_number_sid': payload['phone_number_sid'],
            'price': payload['price'],
            'price_unit': payload['price_unit'],
            'sid': payload['sid'],
            'start_time': deserialize.rfc2822_datetime(payload['start_time']),
            'status': payload['status'],
            'subresource_uris': payload['subresource_uris'],
            'to': payload['to'],
            'to_formatted': payload['to_formatted'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = CallContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def annotation(self):
        """ The annotation """
        return self._properties['annotation']

    @property
    def answered_by(self):
        """ The answered_by """
        return self._properties['answered_by']

    @property
    def api_version(self):
        """ The api_version """
        return self._properties['api_version']

    @property
    def caller_name(self):
        """ The caller_name """
        return self._properties['caller_name']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def direction(self):
        """ The direction """
        return self._properties['direction']

    @property
    def duration(self):
        """ The duration """
        return self._properties['duration']

    @property
    def end_time(self):
        """ The end_time """
        return self._properties['end_time']

    @property
    def forwarded_from(self):
        """ The forwarded_from """
        return self._properties['forwarded_from']

    @property
    def from_(self):
        """ The from """
        return self._properties['from_']

    @property
    def from_formatted(self):
        """ The from_formatted """
        return self._properties['from_formatted']

    @property
    def group_sid(self):
        """ The group_sid """
        return self._properties['group_sid']

    @property
    def parent_call_sid(self):
        """ The parent_call_sid """
        return self._properties['parent_call_sid']

    @property
    def phone_number_sid(self):
        """ The phone_number_sid """
        return self._properties['phone_number_sid']

    @property
    def price(self):
        """ The price """
        return self._properties['price']

    @property
    def price_unit(self):
        """ The price_unit """
        return self._properties['price_unit']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def start_time(self):
        """ The start_time """
        return self._properties['start_time']

    @property
    def status(self):
        """ The status """
        return self._properties['status']

    @property
    def subresource_uris(self):
        """ The subresource_uris """
        return self._properties['subresource_uris']

    @property
    def to(self):
        """ The to """
        return self._properties['to']

    @property
    def to_formatted(self):
        """ The to_formatted """
        return self._properties['to_formatted']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def delete(self):
        self._context.delete()

    def fetch(self):
        self._context.fetch()

    def update(self, url=values.unset, method=values.unset, status=values.unset,
               fallback_url=values.unset, fallback_method=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        self._context.update(
            url=url,
            method=method,
            status=status,
            fallback_url=fallback_url,
            fallback_method=fallback_method,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
        )

    @property
    def recordings(self):
        return self._context.recordings

    @property
    def notifications(self):
        return self._context.notifications

    @property
    def feedback(self):
        return self._context.feedback
