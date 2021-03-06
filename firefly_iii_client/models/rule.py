# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from firefly_iii_client.configuration import Configuration


class Rule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'actions': 'list[RuleAction]',
        'active': 'bool',
        'created_at': 'datetime',
        'description': 'str',
        'order': 'int',
        'rule_group_id': 'int',
        'rule_group_title': 'str',
        'stop_processing': 'bool',
        'strict': 'bool',
        'title': 'str',
        'trigger': 'str',
        'triggers': 'list[RuleTrigger]',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'actions': 'actions',
        'active': 'active',
        'created_at': 'created_at',
        'description': 'description',
        'order': 'order',
        'rule_group_id': 'rule_group_id',
        'rule_group_title': 'rule_group_title',
        'stop_processing': 'stop_processing',
        'strict': 'strict',
        'title': 'title',
        'trigger': 'trigger',
        'triggers': 'triggers',
        'updated_at': 'updated_at'
    }

    def __init__(self, actions=None, active=None, created_at=None, description=None, order=None, rule_group_id=None, rule_group_title=None, stop_processing=None, strict=None, title=None, trigger=None, triggers=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Rule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._actions = None
        self._active = None
        self._created_at = None
        self._description = None
        self._order = None
        self._rule_group_id = None
        self._rule_group_title = None
        self._stop_processing = None
        self._strict = None
        self._title = None
        self._trigger = None
        self._triggers = None
        self._updated_at = None
        self.discriminator = None

        self.actions = actions
        if active is not None:
            self.active = active
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if order is not None:
            self.order = order
        self.rule_group_id = rule_group_id
        if rule_group_title is not None:
            self.rule_group_title = rule_group_title
        if stop_processing is not None:
            self.stop_processing = stop_processing
        if strict is not None:
            self.strict = strict
        self.title = title
        self.trigger = trigger
        self.triggers = triggers
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def actions(self):
        """Gets the actions of this Rule.  # noqa: E501


        :return: The actions of this Rule.  # noqa: E501
        :rtype: list[RuleAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Rule.


        :param actions: The actions of this Rule.  # noqa: E501
        :type: list[RuleAction]
        """
        if self.local_vars_configuration.client_side_validation and actions is None:  # noqa: E501
            raise ValueError("Invalid value for `actions`, must not be `None`")  # noqa: E501

        self._actions = actions

    @property
    def active(self):
        """Gets the active of this Rule.  # noqa: E501

        Whether or not the rule is even active. Default is true.  # noqa: E501

        :return: The active of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Rule.

        Whether or not the rule is even active. Default is true.  # noqa: E501

        :param active: The active of this Rule.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def created_at(self):
        """Gets the created_at of this Rule.  # noqa: E501


        :return: The created_at of this Rule.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Rule.


        :param created_at: The created_at of this Rule.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this Rule.  # noqa: E501


        :return: The description of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rule.


        :param description: The description of this Rule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def order(self):
        """Gets the order of this Rule.  # noqa: E501


        :return: The order of this Rule.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Rule.


        :param order: The order of this Rule.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def rule_group_id(self):
        """Gets the rule_group_id of this Rule.  # noqa: E501

        ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory.  # noqa: E501

        :return: The rule_group_id of this Rule.  # noqa: E501
        :rtype: int
        """
        return self._rule_group_id

    @rule_group_id.setter
    def rule_group_id(self, rule_group_id):
        """Sets the rule_group_id of this Rule.

        ID of the rule group under which the rule must be stored. Either this field or rule_group_title is mandatory.  # noqa: E501

        :param rule_group_id: The rule_group_id of this Rule.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and rule_group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_group_id`, must not be `None`")  # noqa: E501

        self._rule_group_id = rule_group_id

    @property
    def rule_group_title(self):
        """Gets the rule_group_title of this Rule.  # noqa: E501

        Title of the rule group under which the rule must be stored. Either this field or rule_group_id is mandatory.  # noqa: E501

        :return: The rule_group_title of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._rule_group_title

    @rule_group_title.setter
    def rule_group_title(self, rule_group_title):
        """Sets the rule_group_title of this Rule.

        Title of the rule group under which the rule must be stored. Either this field or rule_group_id is mandatory.  # noqa: E501

        :param rule_group_title: The rule_group_title of this Rule.  # noqa: E501
        :type: str
        """

        self._rule_group_title = rule_group_title

    @property
    def stop_processing(self):
        """Gets the stop_processing of this Rule.  # noqa: E501

        If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false.  # noqa: E501

        :return: The stop_processing of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._stop_processing

    @stop_processing.setter
    def stop_processing(self, stop_processing):
        """Sets the stop_processing of this Rule.

        If this value is true and the rule is triggered, other rules  after this one in the group will be skipped. Default value is false.  # noqa: E501

        :param stop_processing: The stop_processing of this Rule.  # noqa: E501
        :type: bool
        """

        self._stop_processing = stop_processing

    @property
    def strict(self):
        """Gets the strict of this Rule.  # noqa: E501

        If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true.  # noqa: E501

        :return: The strict of this Rule.  # noqa: E501
        :rtype: bool
        """
        return self._strict

    @strict.setter
    def strict(self, strict):
        """Sets the strict of this Rule.

        If the rule is set to be strict, ALL triggers must hit in order for the rule to fire. Otherwise, just one is enough. Default value is true.  # noqa: E501

        :param strict: The strict of this Rule.  # noqa: E501
        :type: bool
        """

        self._strict = strict

    @property
    def title(self):
        """Gets the title of this Rule.  # noqa: E501


        :return: The title of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Rule.


        :param title: The title of this Rule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def trigger(self):
        """Gets the trigger of this Rule.  # noqa: E501

        Which action is necessary for the rule to fire? Use either store-journal or update-journal.  # noqa: E501

        :return: The trigger of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this Rule.

        Which action is necessary for the rule to fire? Use either store-journal or update-journal.  # noqa: E501

        :param trigger: The trigger of this Rule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and trigger is None:  # noqa: E501
            raise ValueError("Invalid value for `trigger`, must not be `None`")  # noqa: E501
        allowed_values = ["store-journal", "update-journal"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and trigger not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `trigger` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger, allowed_values)
            )

        self._trigger = trigger

    @property
    def triggers(self):
        """Gets the triggers of this Rule.  # noqa: E501


        :return: The triggers of this Rule.  # noqa: E501
        :rtype: list[RuleTrigger]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this Rule.


        :param triggers: The triggers of this Rule.  # noqa: E501
        :type: list[RuleTrigger]
        """
        if self.local_vars_configuration.client_side_validation and triggers is None:  # noqa: E501
            raise ValueError("Invalid value for `triggers`, must not be `None`")  # noqa: E501

        self._triggers = triggers

    @property
    def updated_at(self):
        """Gets the updated_at of this Rule.  # noqa: E501


        :return: The updated_at of this Rule.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Rule.


        :param updated_at: The updated_at of this Rule.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Rule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rule):
            return True

        return self.to_dict() != other.to_dict()
