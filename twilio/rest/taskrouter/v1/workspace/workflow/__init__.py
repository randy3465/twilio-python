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
from twilio.rest.taskrouter.v1.workspace.workflow.statistics import StatisticsContext


class WorkflowList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkflowList
        
        :param Version version: Version that contains the resource
        :param workspace_sid: Contextual workspace_sid
        
        :returns: WorkflowList
        :rtype: WorkflowList
        """
        super(WorkflowList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workflows'.format(**self._kwargs)

    def read(self, friendly_name=values.unset, limit=None, page_size=None,
             **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'FriendlyName': friendly_name,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            WorkflowInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, friendly_name=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            'FriendlyName': friendly_name,
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            WorkflowInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, friendly_name, configuration, assignment_callback_url,
               fallback_assignment_callback_url=values.unset,
               task_reservation_timeout=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'Configuration': configuration,
            'AssignmentCallbackUrl': assignment_callback_url,
            'FallbackAssignmentCallbackUrl': fallback_assignment_callback_url,
            'TaskReservationTimeout': task_reservation_timeout,
        })
        
        return self._version.create(
            WorkflowInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __call__(self, sid):
        """
        Constructs a WorkflowContext
        
        :param sid: Contextual sid
        
        :returns: WorkflowContext
        :rtype: WorkflowContext
        """
        return WorkflowContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowList>'


class WorkflowContext(InstanceContext):

    def __init__(self, version, workspace_sid, sid):
        super(WorkflowContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/Workflows/{sid}".format(**self._kwargs)
        
        # Dependents
        self._statistics = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            WorkflowInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, friendly_name=values.unset,
               assignment_callback_url=values.unset,
               fallback_assignment_callback_url=values.unset,
               configuration=values.unset, task_reservation_timeout=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'AssignmentCallbackUrl': assignment_callback_url,
            'FallbackAssignmentCallbackUrl': fallback_assignment_callback_url,
            'Configuration': configuration,
            'TaskReservationTimeout': task_reservation_timeout,
        })
        
        return self._version.update(
            WorkflowInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._version.delete("delete", self._uri)

    @property
    def statistics(self):
        if self._statistics is None:
            self._statistics = StatisticsContext(
                self._version,
                workspace_sid=self._kwargs['workspace_sid'],
                workflow_sid=self._kwargs['sid'],
            )
        return self._statistics


class WorkflowInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, sid=None):
        super(WorkflowInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'assignment_callback_url': payload['assignment_callback_url'],
            'configuration': payload['configuration'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'document_content_type': payload['document_content_type'],
            'fallback_assignment_callback_url': payload['fallback_assignment_callback_url'],
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'task_reservation_timeout': payload['task_reservation_timeout'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'workspace_sid': workspace_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = WorkflowContext(
                self._version,
                self._context_properties['workspace_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def assignment_callback_url(self):
        """ The assignment_callback_url """
        return self._properties['assignment_callback_url']

    @property
    def configuration(self):
        """ The configuration """
        return self._properties['configuration']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def document_content_type(self):
        """ The document_content_type """
        return self._properties['document_content_type']

    @property
    def fallback_assignment_callback_url(self):
        """ The fallback_assignment_callback_url """
        return self._properties['fallback_assignment_callback_url']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def task_reservation_timeout(self):
        """ The task_reservation_timeout """
        return self._properties['task_reservation_timeout']

    @property
    def workspace_sid(self):
        """ The workspace_sid """
        return self._properties['workspace_sid']

    def fetch(self):
        self._context.fetch()

    def update(self, friendly_name=values.unset,
               assignment_callback_url=values.unset,
               fallback_assignment_callback_url=values.unset,
               configuration=values.unset, task_reservation_timeout=values.unset):
        self._context.update(
            friendly_name=friendly_name,
            assignment_callback_url=assignment_callback_url,
            fallback_assignment_callback_url=fallback_assignment_callback_url,
            configuration=configuration,
            task_reservation_timeout=task_reservation_timeout,
        )

    def delete(self):
        self._context.delete()

    @property
    def statistics(self):
        return self._context.statistics
