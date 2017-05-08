#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2016 The Simbiose Ventures Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A library that provides a Python client to Slicing Dice API"""
import ujson

import pyslicer.utils.validators as validators
import pyslicer.exceptions as exceptions

from pyslicer.api import SlicingDiceAPI
from pyslicer.url_resources import URLResources


class SlicingDice(SlicingDiceAPI):
    """A python interface to Slicing Dice API

    Example usage:

        To create an object of the SliceDicer:

            from pyslicer.api import SlicingDice
            sd = SlicingDice('my-token')

        To create a field:

                field_json = {
                    'name': 'Pyslicer String Field',
                    'description': 'Pyslicer example description',
                    'type': 'string',
                    'cardinality': 'low'}
                print sd.create_field(field_json)

        To make a query:

                query_json = {
                    'type': 'count',
                    'select': [
                        {
                            "pyslicer-string-field":
                                {
                                    "equal": "test_value_1"
                                }
                        },
                        "or",
                        {
                            "pyslicer-string-field":
                                {
                                    "equal": "test_value_2"
                                }
                        },
                    ]
                }
                print sd.query(query_json)

        To insert data:

                inserting_json = {
                    'foo@bar.com': {
                        'pyslicer-string-field': 'test_value_1',
                        'pyslicer-integer-field': 42,
                    },
                    'baz@bar.com': {
                        'pyslicer-string-field': 'test_value_2',
                        'pyslicer-integer-field': 42,
                    },
                }
                print sd.insert(inserting_json)
    """
    def __init__(
        self, write_key=None, read_key=None, master_key=None,
            custom_key=None, use_ssl=True, timeout=60, uses_test_endpoint=False):
        """Instantiate a new SlicingDice object.

        Keyword arguments:
        key(string or SlicerKey obj) -- Key to access API
        use_ssl(bool) -- Define if the request uses verification SSL for
            HTTPS requests. Defaults False.(Optional)
        timeout(int) -- Define timeout to request,
            defaults 30 secs(default 30).
        test(bool) -- if true will use tests end-point (default False)
        """
        super(SlicingDice, self).__init__(
            master_key, write_key, read_key, custom_key, use_ssl, timeout)
        self.uses_test_endpoint = uses_test_endpoint

    def _count_query_wrapper(self, url, query):
        """Validate count query and make request.

        Keyword arguments:
        url(string) -- Url to make request
        query(dict) -- A count query
        """
        sd_count_query = validators.QueryCountValidator(query)
        if sd_count_query.validator():
            return self._make_request(
                url=url,
                json_data=ujson.dumps(query),
                req_type="post",
                key_level=0)

    def _data_extraction_wrapper(self, url, query):
        """Validate data extraction query and make request.

        Keyword arguments:
        url(string) -- Url to make request
        query(dict) -- A data extraction query
        """
        sd_extraction_result = validators.QueryDataExtractionValidator(query)
        if sd_extraction_result.validator():
            return self._make_request(
                url=url,
                json_data=ujson.dumps(query),
                req_type="post",
                key_level=0)

    def _wrapper_test(self):
        base_url = SlicingDice.BASE_URL
        if self.uses_test_endpoint:
            base_url += "/test"
        return base_url

    def _saved_query_wrapper(self, url, query, update=False):
        """Validate saved query and make request.

        Keyword arguments:
        url(string) -- Url to make request
        query(dict) -- A saved query
        update(bool) -- Indicates with operation is update a
            saved query or not.(default false)
        """
        req_type = "post"
        if update:
            req_type = "put"
        return self._make_request(
            url=url,
            json_data=ujson.dumps(query),
            req_type=req_type,
            key_level=2)

    def get_database(self):
        """Get a database associated with this client (related to keys passed on construction)"""
        url = SlicingDice.BASE_URL + URLResources.PROJECT
        return self._make_request(
            url=url,
            req_type="get",
            key_level=2
        )

    def create_field(self, data):
        """Create field in Slicing Dice

        Keyword arguments:
        data -- A dictionary or list on the Slicing Dice field
            format.
        """
        base_url = self._wrapper_test()
        sd_data = validators.FieldValidator(data)
        if sd_data.validator():
            url = base_url + URLResources.FIELD
            return self._make_request(
                url=url,
                req_type="post",
                json_data=ujson.dumps(data),
                key_level=1)

    def get_columns(self):
        """Get a list of fields"""
        base_url = self._wrapper_test()
        url = base_url + URLResources.FIELD
        return self._make_request(
            url=url,
            req_type="get",
            key_level=2)

    def insert(self, data):
        """Insert data into Slicing Dice API

        Keyword arguments:
        data -- A dictionary in the Slicing Dice data format
            format.
        """
        base_url = self._wrapper_test()
        sd_data = validators.InsertValidator(data)
        if sd_data.validator():
            url = base_url + URLResources.INSERT
            return self._make_request(
                url=url,
                json_data=ujson.dumps(data),
                req_type="post",
                key_level=1)

    def count_entity(self, query):
        """Make a count entity query

        Keyword arguments:
        query -- A dictionary in the Slicing Dice query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_COUNT_ENTITY
        return self._count_query_wrapper(url, query)

    def count_entity_total(self):
        """Make a count entity total query"""
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_COUNT_ENTITY_TOTAL
        return self._make_request(
            url=url,
            req_type="get",
            key_level=0)

    def count_event(self, query):
        """Make a count event query

        Keyword arguments:
        data -- A dictionary query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_COUNT_EVENT
        return self._count_query_wrapper(url, query)

    def aggregation(self, query):
        """Make a aggregation query

        Keyword arguments:
        query -- An aggregation query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_AGGREGATION
        if "query" not in query:
            raise exceptions.InvalidQueryException(
                "The aggregation query must have up the key 'query'.")
        fields = query["query"]
        if len(fields) > 5:
            raise exceptions.MaxLimitException(
                "The aggregation query must have up to 5 fields per request.")
        return self._make_request(
            url=url,
            json_data=ujson.dumps(query),
            req_type="post",
            key_level=0)

    def top_values(self, query):
        """Make a top values query

        Keyword arguments:
        query -- A dictionary query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_TOP_VALUES
        sd_query_top_values = validators.QueryValidator(query)
        if sd_query_top_values.validator():
            return self._make_request(
                url=url,
                json_data=ujson.dumps(query),
                req_type="post",
                key_level=0)

    def exists_entity(self, ids):
        """Make a exists entity query

        Keyword arguments:
        ids -- A list with entity to check if exists
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_EXISTS_ENTITY
        if len(ids) > 100:
            raise exceptions.MaxLimitException(
                "The query exists entity must have up to 100 ids.")
        query = {
            'ids': ids
        }
        return self._make_request(
            url=url,
            json_data=ujson.dumps(query),
            req_type="post",
            key_level=0)

    def get_saved_query(self, query_name):
        """Get a saved query

        Keyword arguments:
        query_name(string) -- The name of the saved query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_SAVED + query_name
        return self._make_request(
            url=url,
            req_type="get",
            key_level=0)

    def get_saved_queries(self):
        """Get all saved queries

        Keyword arguments:
        query_name(string) -- The name of the saved query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_SAVED
        return self._make_request(
            url=url,
            req_type="get",
            key_level=2)

    def delete_saved_query(self, query_name):
        """Delete a saved query

        Keyword arguments:
        query_name(string) -- The name of the saved query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_SAVED + query_name
        return self._make_request(
            url=url,
            req_type="delete",
            key_level=2
        )

    def create_saved_query(self, query):
        """Get a list of queries saved

        Keyword arguments:
        query -- A dictionary query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_SAVED
        return self._saved_query_wrapper(url, query)

    def update_saved_query(self, name, query):
        """Get a list of queries saved

        Keyword arguments:
        name -- The name of the saved query to update
        query -- A dictionary query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_SAVED + name
        return self._saved_query_wrapper(url, query, True)

    def result(self, query):
        """Get a data extraction result

        Keyword arguments:
        query -- A dictionary query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_DATA_EXTRACTION_RESULT
        return self._data_extraction_wrapper(url, query)

    def score(self, query):
        """Get a data extraction score

        Keyword arguments:
        query -- A dictionary query
        """
        base_url = self._wrapper_test()
        url = base_url + URLResources.QUERY_DATA_EXTRACTION_SCORE
        return self._data_extraction_wrapper(url, query)
