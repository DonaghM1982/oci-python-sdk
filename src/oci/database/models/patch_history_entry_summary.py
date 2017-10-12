# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class PatchHistoryEntrySummary(object):

    def __init__(self):

        self.swagger_types = {
            'action': 'str',
            'id': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'patch_id': 'str',
            'time_ended': 'datetime',
            'time_started': 'datetime'
        }

        self.attribute_map = {
            'action': 'action',
            'id': 'id',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'patch_id': 'patchId',
            'time_ended': 'timeEnded',
            'time_started': 'timeStarted'
        }

        self._action = None
        self._id = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._patch_id = None
        self._time_ended = None
        self._time_started = None

    @property
    def action(self):
        """
        Gets the action of this PatchHistoryEntrySummary.
        The action being performed or was completed.

        Allowed values for this property are: "APPLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this PatchHistoryEntrySummary.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this PatchHistoryEntrySummary.
        The action being performed or was completed.


        :param action: The action of this PatchHistoryEntrySummary.
        :type: str
        """
        allowed_values = ["APPLY"]
        if action not in allowed_values:
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def id(self):
        """
        Gets the id of this PatchHistoryEntrySummary.
        The OCID of the patch history entry.


        :return: The id of this PatchHistoryEntrySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PatchHistoryEntrySummary.
        The OCID of the patch history entry.


        :param id: The id of this PatchHistoryEntrySummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this PatchHistoryEntrySummary.
        A descriptive text associated with the lifecycleState.
        Typically contains additional displayable text.


        :return: The lifecycle_details of this PatchHistoryEntrySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this PatchHistoryEntrySummary.
        A descriptive text associated with the lifecycleState.
        Typically contains additional displayable text.


        :param lifecycle_details: The lifecycle_details of this PatchHistoryEntrySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this PatchHistoryEntrySummary.
        The current state of the action.

        Allowed values for this property are: "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PatchHistoryEntrySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PatchHistoryEntrySummary.
        The current state of the action.


        :param lifecycle_state: The lifecycle_state of this PatchHistoryEntrySummary.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "SUCCEEDED", "FAILED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def patch_id(self):
        """
        Gets the patch_id of this PatchHistoryEntrySummary.
        The OCID of the patch.


        :return: The patch_id of this PatchHistoryEntrySummary.
        :rtype: str
        """
        return self._patch_id

    @patch_id.setter
    def patch_id(self, patch_id):
        """
        Sets the patch_id of this PatchHistoryEntrySummary.
        The OCID of the patch.


        :param patch_id: The patch_id of this PatchHistoryEntrySummary.
        :type: str
        """
        self._patch_id = patch_id

    @property
    def time_ended(self):
        """
        Gets the time_ended of this PatchHistoryEntrySummary.
        The date and time when the patch action completed.


        :return: The time_ended of this PatchHistoryEntrySummary.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this PatchHistoryEntrySummary.
        The date and time when the patch action completed.


        :param time_ended: The time_ended of this PatchHistoryEntrySummary.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def time_started(self):
        """
        Gets the time_started of this PatchHistoryEntrySummary.
        The date and time when the patch action started.


        :return: The time_started of this PatchHistoryEntrySummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this PatchHistoryEntrySummary.
        The date and time when the patch action started.


        :param time_started: The time_started of this PatchHistoryEntrySummary.
        :type: datetime
        """
        self._time_started = time_started

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other