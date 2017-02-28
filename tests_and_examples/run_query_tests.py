"""Tests SlicingDice endpoints.

This script tests SlicingDice by running tests suites, each composed by:
    - Creating fields
    - Indexing data
    - Querying
    - Comparing results

All tests are stored in JSON files at ./examples named as the query being
tested:
    - count_entity.json
    - count_event.json

In order to execute the tests, simply replace API_KEY by the demo API key and
run the script with:
    $ python run_tests.py
"""

import json
import os
import sys
import time

from pyslicer import SlicingDice
from pyslicer.exceptions import SlicingDiceException

# Suppress HTTPS warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class SlicingDiceTester(object):
    """Test orchestration class."""
    def __init__(self, api_key, verbose=False, endpoint_test=True):
        self.client = SlicingDice(api_key)
        self.endpoint_test = endpoint_test

        # Translation table for fields with timestamp
        self.field_translation = {}

        self.sleep_time = int(os.environ.get("CLIENT_SLEEP_TIME", 5))  # seconds
        self.path = 'examples/'  # Directory containing examples to test
        self.extension = '.json'  # Examples file format

        self.num_successes = 0
        self.num_fails = 0
        self.failed_tests = []

        self.verbose = verbose

    def run_tests(self, query_type):
        """Run all tests for a given query type.

        Parameters:
        query_type -- String containing the name of the query that will be
            tested. This name must match the JSON file name as well.
        """
        test_data = self.load_test_data(query_type)
        num_tests = len(test_data)

        for i, test in enumerate(test_data):
            self._empty_field_translation()

            print '({}/{}) Executing test "{}"'.format(i + 1, num_tests,
                                                       test['name'])

            if 'description' in test:
                print '  Description: {}'.format(test['description'])

            print '  Query type: {}'.format(query_type)

            auto_create = test['index'].get('auto-create-fields', False)
            try:
                if auto_create:
                    self.get_fields_from_index_data(test)
                else:
                    self.create_fields(test)
                self.index_data(test)
                result = self.execute_query(query_type, test)
            except SlicingDiceException as e:
                result = {'result': {'error': str(e)}}

            self.compare_result(query_type, test, result)
            print

    def _empty_field_translation(self):
        """Empty field translation table so tests don't intefere each other."""
        self.field_translation = {}

    def load_test_data(self, query_type):
        """Load all test data from JSON file for a given query type.

        Parameters:
        query_type -- String containing the name of the query that will be
            tested. This name must match the JSON file name as well.

        Return:
        Test data as a dictionary.
        """
        filename = self.path + query_type + self.extension
        return json.load(open(filename))

    def create_fields(self, test):
        """Create fields for a given test.

        Parameters:
        test -- Dictionary containing test name, fields metadata, data to be
            indexed, query, and expected results.
        """
        is_singular = len(test['fields']) == 1
        field_or_fields = 'field' if is_singular else 'fields'
        print '  Creating {} {}'.format(len(test['fields']), field_or_fields)

        for field in test['fields']:
            self._append_timestamp_to_field_name(field)
            self.client.create_field(field, test=self.endpoint_test)

            if self.verbose:
                print '    - {}'.format(field['api-name'])

    def _append_timestamp_to_field_name(self, field):
        """Append integer timestamp to field name.

        This technique allows the same test suite to be executed over and over
        again, since each execution will use different field names.

        Parameters:
        field -- Dictionary containing field data, such as "name" and
            "api-name".
        """
        old_name = '"{}"'.format(field['api-name'])

        timestamp = self._get_timestamp()
        field['name'] += timestamp
        field['api-name'] += timestamp
        new_name = '"{}"'.format(field['api-name'])

        self.field_translation[old_name] = new_name

    @staticmethod
    def _get_timestamp():
        """Get integer timestamp in string format.

        Return:
        String with integer timestamp.
        """
        # Appending integer timestamp including second decimals
        return str(int(time.time() * 10))

    def get_fields_from_index_data(self, test):
        """Get all field names from index data and translate them.

        Parameters:
        test -- Dictionary containing test name, fields metadata, data to be
            indexed, query, and expected results.
        """
        print '  Auto-creating fields'
        for entity, data in test['index'].items():
            if entity != 'auto-create-fields':
                for field in data.keys():
                    if field not in self.field_translation:
                        self._append_timestamp_to_field_name(
                            {"api-name": field, "name": field})

    def index_data(self, test):
        """Index data to SlicingDice.

        Parameters:
        test -- Dictionary containing test name, fields metadata, data to be
            indexed, query, and expected results.
        auto_create -- Auto create a field if not exists.
        """
        is_singular = len(test['index']) == 1
        entity_or_entities = 'entity' if is_singular else 'entities'
        print '  Indexing {} {}'.format(len(test['index']), entity_or_entities)

        index_data = self._translate_field_names(test['index'])

        if self.verbose:
            print '    - {}'.format(index_data)

        self.client.index(index_data, test=self.endpoint_test)

        # Wait a few seconds so the data can be indexed by SlicingDice
        time.sleep(self.sleep_time)

    def execute_query(self, query_type, test):
        """Execute query at SlicingDice.

        Parameters:
        query_type -- String containing the name of the query that will be
            tested. This name must match the JSON file name as well.
        test -- Dictionary containing test name, fields metadata, data to be
            indexed, query, and expected results.
        """
        query_data = self._translate_field_names(test['query'])
        print '  Querying'

        if self.verbose:
            print '    - {}'.format(query_data)

        if query_type == 'count_entity':
            result = self.client.count_entity(
                query_data, test=self.endpoint_test)
        elif query_type == 'count_event':
            result = self.client.count_event(
                query_data, test=self.endpoint_test)
        elif query_type == 'top_values':
            result = self.client.top_values(
                query_data, test=self.endpoint_test)
        elif query_type == 'aggregation':
            result = self.client.aggregation(
                query_data, test=self.endpoint_test)
        elif query_type == 'score':
            result = self.client.score(
                query_data, test=self.endpoint_test)
        elif query_type == 'result':
            result = self.client.result(
                query_data, test=self.endpoint_test)

        return result

    def _translate_field_names(self, json_data):
        """Translate field name to match field name with timestamp.

        Parameters:
        json_data -- JSON data to have the field name translated.

        Return:
        JSON data with new field name.
        """
        data_string = json.dumps(json_data)

        for old_name, new_name in self.field_translation.items():
            data_string = data_string.replace(old_name, new_name)

        return json.loads(data_string)

    def compare_result(self, query_type, test, result):
        """Compare query expected and received results, exiting if they differ.

        Parameters:
        query_type -- String containing the name of the query that will be
            tested. This name must match the JSON file name as well.
        test -- Dictionary containing test name, fields metadata, data to be
            indexed, query, and expected results.
        result -- Dictionary containing received result after querying
            SlicingDice.
        """
        expected = self._translate_field_names(test['expected'])

        for key, value in expected.items():
            if value == 'ignore':
                continue

            if value != result[key]:
                time.sleep(self.sleep_time * 3)
                test['query'].update({"bypass-cache": True})
                result2 = self.execute_query(query_type, test)
                if value == result2[key]:
                    print "  Passed at second try"
                    continue
                self.num_fails += 1
                self.failed_tests.append(test['name'])

                print '  Expected: "{}": {}'.format(key, value)
                print '  Result:   "{}": {}'.format(key, result[key])
                print '  Status: Failed'
                return

        self.num_successes += 1

        print '  Status: Passed'


def main():
    # SlicingDice queries to be tested. Must match the JSON file name.
    query_types = [
        'count_entity',
        'count_event',
        'top_values',
        'aggregation',
        'score',
        'result'
    ]

    # Testing class with demo API key or one of your API key
    # by enviroment variable
    # http://panel.slicingdice.com/docs/#api-details-api-connection-api-keys-demo-key

    API_KEY = os.environ.get(
        "SD_API_KEY",
        ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfX3NhbHQiOiJkZW1vMW0'
         'iLCJwZXJtaXNzaW9uX2xldmVsIjozLCJwcm9qZWN0X2lkIjoyMCwiY2xpZW5'
         '0X2lkIjoxMH0.xRBHeDxTzYAgFyuU94SWFbjITeoxgyRCQGdIee8qrLA'))

    # MODE_TEST give us if you want to use endpoint Test or Prod
    MODE_TEST = os.environ.get("MODE_TEST", "test")
    endpoint_test = False if MODE_TEST.lower() == 'prod' else True
    sd_tester = SlicingDiceTester(
        api_key=API_KEY,
        verbose=False,
        endpoint_test=endpoint_test)

    try:
        for query_type in query_types:
            sd_tester.run_tests(query_type)
    except KeyboardInterrupt:
        pass

    print 'Results:'
    print '  Successes:', sd_tester.num_successes
    print '  Fails:', sd_tester.num_fails

    for failed_test in sd_tester.failed_tests:
        print '    - {}'.format(failed_test)

    print

    if sd_tester.num_fails > 0:
        is_singular = sd_tester.num_fails == 1
        test_or_tests = 'test has' if is_singular else 'tests have'
        print 'FAIL: {} {} failed'.format(sd_tester.num_fails, test_or_tests)
        sys.exit(1)
    else:
        print 'SUCCESS: All tests passed'


if __name__ == '__main__':
    main()
