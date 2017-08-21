# coding: utf-8

"""
    Allele Calling Service

    The Allele Calling  service provides an API for converting raw sequence data to GFE and HLA allele calls.

    OpenAPI spec version: 0.0.3
    Contact: mhalagan@nmdp.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GfeCall(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'hla': 'str',
        'related_gfe': 'list[GfeTyping]',
        'act_version': 'str',
        'gfe_version': 'str',
        'gfedb_version': 'str'
    }

    attribute_map = {
        'hla': 'hla',
        'related_gfe': 'related_gfe',
        'act_version': 'act_version',
        'gfe_version': 'gfe_version',
        'gfedb_version': 'gfedb_version'
    }

    def __init__(self, hla=None, related_gfe=None, act_version=None, gfe_version=None, gfedb_version=None):
        """
        GfeCall - a model defined in Swagger
        """

        self._hla = None
        self._related_gfe = None
        self._act_version = None
        self._gfe_version = None
        self._gfedb_version = None

        if hla is not None:
          self.hla = hla
        if related_gfe is not None:
          self.related_gfe = related_gfe
        if act_version is not None:
          self.act_version = act_version
        if gfe_version is not None:
          self.gfe_version = gfe_version
        if gfedb_version is not None:
          self.gfedb_version = gfedb_version

    @property
    def hla(self):
        """
        Gets the hla of this GfeCall.

        :return: The hla of this GfeCall.
        :rtype: str
        """
        return self._hla

    @hla.setter
    def hla(self, hla):
        """
        Sets the hla of this GfeCall.

        :param hla: The hla of this GfeCall.
        :type: str
        """

        self._hla = hla

    @property
    def related_gfe(self):
        """
        Gets the related_gfe of this GfeCall.

        :return: The related_gfe of this GfeCall.
        :rtype: list[GfeTyping]
        """
        return self._related_gfe

    @related_gfe.setter
    def related_gfe(self, related_gfe):
        """
        Sets the related_gfe of this GfeCall.

        :param related_gfe: The related_gfe of this GfeCall.
        :type: list[GfeTyping]
        """

        self._related_gfe = related_gfe

    @property
    def act_version(self):
        """
        Gets the act_version of this GfeCall.

        :return: The act_version of this GfeCall.
        :rtype: str
        """
        return self._act_version

    @act_version.setter
    def act_version(self, act_version):
        """
        Sets the act_version of this GfeCall.

        :param act_version: The act_version of this GfeCall.
        :type: str
        """

        self._act_version = act_version

    @property
    def gfe_version(self):
        """
        Gets the gfe_version of this GfeCall.

        :return: The gfe_version of this GfeCall.
        :rtype: str
        """
        return self._gfe_version

    @gfe_version.setter
    def gfe_version(self, gfe_version):
        """
        Sets the gfe_version of this GfeCall.

        :param gfe_version: The gfe_version of this GfeCall.
        :type: str
        """

        self._gfe_version = gfe_version

    @property
    def gfedb_version(self):
        """
        Gets the gfedb_version of this GfeCall.

        :return: The gfedb_version of this GfeCall.
        :rtype: str
        """
        return self._gfedb_version

    @gfedb_version.setter
    def gfedb_version(self, gfedb_version):
        """
        Sets the gfedb_version of this GfeCall.

        :param gfedb_version: The gfedb_version of this GfeCall.
        :type: str
        """

        self._gfedb_version = gfedb_version

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GfeCall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other