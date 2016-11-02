import collections
import json


def generate_name(query_type, test):
    name = generate_start(query_type)
    name += ' '

    fields = generate_fields(test['fields'])
    if fields:
        name += fields

    operators = generate_operators(test['query'])
    if operators:
        name += ', ' + operators

    parameters = generate_parameters(test['query'])
    if parameters:
        name += ' and ' + parameters

    end = generate_end(test)
    if end:
        name += ' ' + end

    name += '.'

    return name


def generate_start(query_type):
    query_name = query_type.upper()
    return 'Test for a \"{}\" query'.format(query_name.replace('_', ' '))


def generate_fields(fields):
    if len(fields) == 0:
        return 'using automatically created fields'

    text = 'using field'
    if len(fields) > 1:
        text += 's'

    text += ' '

    for i, field in enumerate(fields):
        field_name = field['type'].upper()
        is_last_word = i == len(fields) - 1
        is_second_last_word = i == len(fields) - 2

        text += '"{}"'.format(field_name)

        if is_second_last_word:
            text += ' and '
        elif len(fields) > 2 and not is_last_word:
            text += ', '

    return text


def generate_operators(query):
    query_string = json.dumps(query)
    valid_operators = ['and', 'or', 'not', 'freqgroup']
    existing_operators = [operator for operator in valid_operators
                          if '"{}"'.format(operator) in query_string]

    text = 'operator'

    if len(existing_operators) == 0:
        return ''
    if len(existing_operators) > 1:
        text += 's'

    text += ' '

    for i, operator in enumerate(existing_operators):
        operator_name = operator.upper()
        is_last_word = i == len(existing_operators) - 1
        is_second_last_word = i == len(existing_operators) - 2

        text += '"{}"'.format(operator_name)

        if is_second_last_word:
            text += ' and '
        elif len(existing_operators) > 2 and not is_last_word:
            text += ', '

    return text


def generate_parameters(query):
    query_string = json.dumps(query)
    valid_parameters = [
        'equals', 'not-equals', 'range', 'gt', 'gte', 'lt', 'lte', 'between',
        'minfreq', 'starts-with', 'ends-with', 'contains', 'not-contains',
        'precision']
    existing_parameters = [parameter for parameter in valid_parameters
                           if '"{}"'.format(parameter) in query_string]

    text = 'parameter'

    if len(existing_parameters) == 0:
        return ''
    if len(existing_parameters) > 1:
        text += 's'

    text += ' '

    for i, parameter in enumerate(existing_parameters):
        parameter_name = parameter.upper()
        is_last_word = i == len(existing_parameters) - 1
        is_second_last_word = i == len(existing_parameters) - 2

        text += '"{}"'.format(parameter_name)

        if is_second_last_word:
            text += ' and '
        elif len(existing_parameters) > 2 and not is_last_word:
            text += ', '

    return text


def generate_end(test):
    text = ''

    timezone = generate_timezone(test)
    if timezone:
        text = 'with ' + timezone

    relative_time = generate_relative_time(test)
    if relative_time:
        if text:
            text += ' and ' + relative_time
        else:
            text += 'with ' + relative_time

    return text


def generate_timezone(test):
    text = ''
    index_string = json.dumps(test['index'])
    query_string = json.dumps(test['query'])

    if ':00Z' in index_string:
        text += 'UTC timezone when indexing'
    elif '+03:00' in index_string:
        text += '+3h timezone when indexing'
    elif '-03:00' in index_string:
        text += '-3h timezone when indexing'

    if text and ':00Z' in query_string or '+03:00' in query_string or '-03:00' in query_string:
        text += ' and querying'
    else:
        if ':00Z' in query_string:
            text += 'UTC timezone when querying'
        elif '+03:00' in query_string:
            text += '+3h timezone when querying'
        elif '-03:00' in query_string:
            text += '-3h timezone when querying'

    return text


def generate_relative_time(test):
    text = []
    query_string = json.dumps(test['query'])

    if 'now' in query_string:
        text.append('"NOW"')
    elif 'today' in query_string:
        text.append('"TODAY"')
    elif 'yesterday' in query_string:
        text.append('"YESTERDAY"')

    if '-30sec' in query_string:
        text.append('"SECONDS"')
    elif '-1min' in query_string:
        text.append('"MINUTE"')
    elif '-3hr' in query_string:
        text.append('"HOUR"')
    elif '-1d' in query_string:
        text.append('"DAY"')
    elif '+1w' in query_string or '-1w' in query_string:
        text.append('"WEEK"')
    elif '-1m' in query_string:
        text.append('"MONTH"')
    elif '-1y' in query_string:
        text.append('"YEAR"')

    text = ' and '.join(text)

    if text:
        text = 'relative interval containing ' + text

    return text


def main():
    query_types = [
        # 'tests',
        'count_entity',
        'count_event',
        'aggregation',
        # 'top_values',
    ]

    for query_type in query_types:
        tests = json.load(
            open('examples/{}.json'.format(query_type)),
            object_pairs_hook=collections.OrderedDict)

        for i in range(len(tests)):
            tests[i]['name'] = generate_name(query_type, tests[i])

        for test in tests:
            print test['name']

        json.dump(tests,
                  open('examples/{}.json'.format(query_type), 'w'),
                  indent=4)


if __name__ == '__main__':
    main()
