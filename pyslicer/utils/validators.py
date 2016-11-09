#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

import pyslicer.exceptions as exceptions

from pyslicer.utils.data_utils import is_str_empty


class SDBaseValidator(object):
    """Base field, query and index validator."""
    __metaclass__ = abc.ABCMeta

    def __init__(self, dictionary):
        if not all(dictionary) or not all(dictionary.values()):
            raise exceptions.InvalidIndexException(
                "This query has invalid keys or values.")
        self.data = dictionary

    @abc.abstractmethod
    def validator(self):
        pass


class SavedQueryValidator(SDBaseValidator):
    def __init__(self, dictionary_query):
        """
        Parameters:
            dictionary_query(dict) -- A dict query
        """
        super(SavedQueryValidator, self).__init__(dictionary_query)
        self._list_query_types = [
            "count/entity", "count/event", "count/entity/total",
            "aggregation", "top_values"]

    def _has_valid_type(self):
        """Check if query type is valid
        Returns:
            true if have query type valid
        """
        query_type = self.data['type']
        if query_type not in self._list_query_types:
            raise exceptions.InvalidQueryTypeException(
                "This dictionary don't have query type valid.")
        return True

    def validator(self):
        """
        Returns:
            true if query is valid
        """
        if self._has_valid_type():
            return True
        return False


class QueryCountValidator(SDBaseValidator):
    def __init__(self, queries):
        """
        Parameters:
            queries(dict) -- A dict query
        """
        super(QueryCountValidator, self).__init__(queries)

    def validator(self):
        if len(self.data) > 10:
            raise exceptions.MaxLimitException(
                "The query count entity has a limit of 10 queries by request.")
        return True


class QueryValidator(SDBaseValidator):
    def __init__(self, queries):
        """
        Parameters:
            queries(dict) -- A dict query
        """
        super(QueryValidator, self).__init__(queries)

    def exceeds_queries_limit(self):
        """Check if query exceeds the limit of 5 queries per request

        Returns:
            true if exceeds the limit
        """
        if len(self.data) > 5:
            return True
        return False

    def exceeds_fields_limit(self):
        """Check if query exceeds the limit of 5 fields per request

        Returns:
            false if don't exceeds the limit
        """
        for key, value in self.data.iteritems():
            if len(value) > 6:
                raise exceptions.MaxLimitException(
                    "The query '{0}' exceeds the limit of fields "
                    "per query in request".format(key))
            if 'contains' not in value and 'equal' not in value:
                raise exceptions.InvalidQueryException(
                    "Each query only can have a 'contain' or a 'equal'.")

        return False

    def exceeds_values_contains_limit(self):
        """Check if query exceeds the limit of 5 contains values per query

        Returns:
            false if don't exceeds the limit
        """
        for key, value in self.data.iteritems():
            if "contains" in value and len(value['contains']) > 5:
                raise exceptions.MaxLimitException(
                    "The query '{0}' exceeds the limit of contains "
                    "per query in request".format(key))
        return False

    def validator(self):
        """Returns true if query is ok"""
        if not (self.exceeds_queries_limit() and
                self.exceeds_fields_limit() and
                self.exceeds_values_contains_limit()):
            return True
        return False


class QueryDataExtractionValidator(SDBaseValidator):
    def __init__(self, queries):
        """
        Parameters:
            queries(dict) -- A dict query
        """
        super(QueryDataExtractionValidator, self).__init__(queries)

    def _valid_keys(self):
        if "fields" in self.data:
            value = self.data["fields"]
            if type(value) != list:
                raise exceptions.InvalidQueryException(
                    "The key 'fields' in query has a invalid value.")
            else:
                if len(value) > 10:
                    raise exceptions.InvalidQueryException(
                        "The key 'fields' in data extraction result must "
                        "have up to 10 fields.")
        if "limit" in self.data:
            limit = self.data['limit']
            if type(limit) != int:
                raise exceptions.InvalidQueryException(
                    "The key 'limit' in query has a invalid value.")
            if limit > 100:
                raise exceptions.InvalidQueryException(
                    "The field 'limit' has a value max of 100.")
        return True

    def validator(self):
        if self._valid_keys():
            return True
        return False


class IndexValidator(SDBaseValidator):
    def __init__(self, dictionary_index):
        """
        Parameters:
            dictionary_index(dict) -- A dict query
        """
        super(IndexValidator, self).__init__(dictionary_index)

    def _has_empty_field(self):
        """Check empty fields in dictionary
        Returns:
            false if dictionary don't have empty fields
        """
        if not all(self.data) or not all(self.data.values()):
            raise exceptions.InvalidIndexException(
                "This index has invalid keys or values.")
        for id, value in self.data.iteritems():
            # Value is a dictionary when it is an entity being indexed:
            # "my-entity": {"year": 2016}
            # It can also be a parameter, such as "auto-create-fields":
            # "auto-create-fields": true
            if not isinstance(
                    value, (dict, bool)) or value is None or len(
                        str(value)) == 0:
                raise exceptions.WrongTypeException(
                    "The value for an id should be a dictionary")
        return False

    def validator(self):
        """
        Returns:
            true if query is valid
        """
        if not self._has_empty_field():
            return True


class FieldValidator(SDBaseValidator):
    def __init__(self, dictionary_field):
        """
        Parameters:
            dictionary_field(dict) -- A dict field
        """
        super(FieldValidator, self).__init__(dictionary_field)
        self._valid_type_fields = [
            "unique-id", "boolean", "string", "integer", "decimal",
            "enumerated", "date", "integer-time-series",
            "decimal-time-series", "string-time-series"
        ]

    def _validate_name(self):
        """Validate field name"""
        if 'name' not in self.data:
            raise exceptions.InvalidFieldException(
                "The field should have a name.")
        else:
            name = self.data['name']
            if is_str_empty(name):
                raise exceptions.InvalidFieldNameException(
                    "The field's name can't be empty/None.")
            elif len(name) > 80:
                raise exceptions.InvalidFieldNameException(
                    "The field's name have a very big name.(Max: 80 chars)")

    def _validate_description(self):
        """Validate field description"""
        description = self.data['description']
        if is_str_empty(description):
            raise exceptions.InvalidFieldDescriptionException(
                "The field's description can't be empty/None.")
        elif len(description) > 300:
            raise exceptions.InvalidFieldDescriptionException(
                "The field's description have a very big name.(Max: 300chars)")

    def _validate_field_type(self):
        """Validate field type"""
        if 'type' not in self.data:
            raise exceptions.InvalidFieldException(
                "The field should have a type.")
        type_field = self.data['type']
        if type_field not in self._valid_type_fields:
            raise exceptions.InvalidFieldTypeException(
                "This field have a invalid type.")

    def _validate_field_decimal_places(self):
        """Validate field decimal places"""
        decimal_types = ["decimal", "decimal-time-series"]
        if self.data['type'] not in decimal_types:
            raise exceptions.InvalidFieldException(
                "This field is only accepted on type 'decimal' or"
                "'decimal-time-series'")

    def _check_str_type_integrity(self):
        """Check if field string type has everything you need"""
        if 'cardinality' not in self.data:
            raise exceptions.InvalidFieldException(
                "The field with type string should have "
                "'cardinality' key.")
        cardinality_types = ["high", "low"]
        if self.data['cardinality'] not in cardinality_types:
            raise exceptions.InvalidFieldException(
                "The field 'cardinality' has invalid value.")

    def _validate_enumerate_type(self):
        if 'range' not in self.data:
            raise exceptions.InvalidFieldException(
                "The 'enumerate' type needs of the 'range' parameter.")

    def validator(self):
        """
        Returns:
            true if new field is valid
        """
        self._validate_name()
        self._validate_field_type()
        if self.data['type'] == "string":
            self._check_str_type_integrity()
        if self.data['type'] == "enumerated":
            self._validate_enumerate_type()
        if 'description' in self.data:
            self._validate_description()
        if 'decimal-place' in self.data:
            self._validate_field_decimal_places()
        # if 'storage' in self.data:
        #    self._validate_field_storage()
        return True