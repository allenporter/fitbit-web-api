# coding: utf-8

"""
    Fitbit Web API Explorer

    Fitbit provides a Web API for accessing data from Fitbit activity trackers, Aria scale, and manually entered logs. Anyone can develop an application to access and modify a Fitbit user's data on their behalf, so long as it complies with Fitbit Platform Terms of Service. These Swagger UI docs do not currently support making Fitbit API requests directly. In order to make a request, construct a request for the appropriate endpoint using this documentation, and then add an Authorization header to each request with an access token obtained using the steps outlined here: https://dev.fitbit.com/build/reference/web-api/developer-guide/authorization/.  # noqa: E501

    OpenAPI spec version: 1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class FoodItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"food_id": "int", "amount": "int", "unit_id": "int"}

    attribute_map = {"food_id": "foodId", "amount": "amount", "unit_id": "unitId"}

    def __init__(self, food_id=None, amount=None, unit_id=None):  # noqa: E501
        """FoodItem - a model defined in Swagger"""  # noqa: E501
        self._food_id = None
        self._amount = None
        self._unit_id = None
        self.discriminator = None
        if food_id is not None:
            self.food_id = food_id
        if amount is not None:
            self.amount = amount
        if unit_id is not None:
            self.unit_id = unit_id

    @property
    def food_id(self):
        """Gets the food_id of this FoodItem.  # noqa: E501


        :return: The food_id of this FoodItem.  # noqa: E501
        :rtype: int
        """
        return self._food_id

    @food_id.setter
    def food_id(self, food_id):
        """Sets the food_id of this FoodItem.


        :param food_id: The food_id of this FoodItem.  # noqa: E501
        :type: int
        """

        self._food_id = food_id

    @property
    def amount(self):
        """Gets the amount of this FoodItem.  # noqa: E501


        :return: The amount of this FoodItem.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FoodItem.


        :param amount: The amount of this FoodItem.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def unit_id(self):
        """Gets the unit_id of this FoodItem.  # noqa: E501


        :return: The unit_id of this FoodItem.  # noqa: E501
        :rtype: int
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this FoodItem.


        :param unit_id: The unit_id of this FoodItem.  # noqa: E501
        :type: int
        """

        self._unit_id = unit_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(FoodItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FoodItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
