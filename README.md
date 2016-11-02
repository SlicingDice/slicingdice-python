# SlicingDice Official Python Client (v1.0)

Official Python client for [SlicingDice](http://www.slicingdice.com/), Data Warehouse and Analytics Database as a Service.

## Documentation

If you are new to SlicingDice, check our [quickstart guide](http://panel.slicingdice.com/docs/#quickstart-guide) and learn to use it in 15 minutes.

Please refer to the [SlicingDice official documentation](http://panel.slicingdice.com/docs/) for more information on [analytics databases](http://panel.slicingdice.com/docs/#analytics-concepts), [data modeling](http://panel.slicingdice.com/docs/#data-modeling), [indexing](http://panel.slicingdice.com/docs/#data-indexing), [querying](http://panel.slicingdice.com/docs/#data-querying), [limitations](http://panel.slicingdice.com/docs/#current-slicingdice-limitations) and [API details](http://panel.slicingdice.com/docs/#api-details).

## Tests and Examples

Whether you want to test the client installation or simply check more examples on how the client works, take a look at the [tests and examples directory](tests_and_examples/).

## Installing

In order to install the Python client, you only need to use [`pip`](https://packaging.python.org/installing/).

```bash
pip install pyslicer
```

## Usage

```python
from pyslicer import SlicingDice

# Configure the client
client = SlicingDice(master_key='API_KEY')

# Indexing data
index_data = {
    'user1@slicingdice.com': {
        'age': 22
    },
    'auto-create-fields': True
}
client.index(index_data)

# Querying data
query_data = {
    'users-between-20-and-40': [
        {
            'age': {
                'range': [
                    20,
                    40
                ]
            }
        }
    ]
}
print client.count_entity(query_data)
```

## Reference

`SlicingDice` encapsulates logic for sending requests to the API. Its methods are thin layers around the [API endpoints](http://panel.slicingdice.com/docs/#api-details-api-endpoints), so their parameters and return values are JSON-like `dict` objects with the same syntax as the [API endpoints](http://panel.slicingdice.com/docs/#api-details-api-endpoints)

### Attributes

* `keys (str)` - [API key](http://panel.slicingdice.com/docs/#api-details-api-connection-api-keys) to authenticate requests with the SlicingDice API.

### Constructor

`__init__(self, write_key=None, read_key=None, master_key=None, custom_key=None, use_ssl=False, timeout=60)`
* `write_key (str)` - [API key](http://panel.slicingdice.com/docs/#api-details-api-connection-api-keys) to authenticate requests with the SlicingDice API.
* `read_key (str)` - [API key](http://panel.slicingdice.com/docs/#api-details-api-connection-api-keys) to authenticate requests with the SlicingDice API.
* `master_key (str)` - [API key](http://panel.slicingdice.com/docs/#api-details-api-connection-api-keys) to authenticate requests with the SlicingDice API.
* `custom_key (str)` - [API key](http://panel.slicingdice.com/docs/#api-details-api-connection-api-keys) to authenticate requests with the SlicingDice API.
* `use_ssl (bool)` - Define if the requests verify SSL for HTTPS requests.
* `timeout (int)` - Amount of time, in seconds, to wait for results for each request.

### `get_projects()`
Get all created projects, both active and inactive ones. This method corresponds to a [GET request at /project](http://panel.slicingdice.com/docs/#api-details-api-endpoints-get-project).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_API_KEY')
print sd.get_projects()
```

#### Output example

```json
{
    "active": [
        {
            "name": "Project 1",
            "description": "My first project",
            "data-expiration": 30,
            "created-at": "2016-04-05T10:20:30Z"
        }
    ],
    "inactive": [
        {
            "name": "Project 2",
            "description": "My second project",
            "data-expiration": 90,
            "created-at": "2016-04-05T10:20:30Z"
        }
    ]
}
```

### `get_fields(test=False)`
Get all created fields, both active and inactive ones. This method corresponds to a [GET request at /field](http://panel.slicingdice.com/docs/#api-details-api-endpoints-get-field).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_API_KEY')
print sd.get_fields()
```

#### Output example

```json
{
    "active": [
        {
          "name": "Model",
          "api-name": "car-model",
          "description": "Car models from dealerships",
          "type": "string",
          "category": "general",
          "cardinality": "high",
          "storage": "latest-value"
        }
    ],
    "inactive": [
        {
          "name": "Year",
          "api-name": "car-year",
          "description": "Year of manufacture",
          "type": "integer",
          "category": "general",
          "storage": "latest-value"
        }
    ]
}
```

### `create_field(json_data, test=False)`
Create a new field. This method corresponds to a [POST request at /field](http://panel.slicingdice.com/docs/#api-details-api-endpoints-post-field).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_API_KEY')
field = {
    'name': 'Year',
    'api-name': 'year',
    'type': 'integer',
    'description': 'Year of manufacturing',
    'storage': 'latest-value'
}
print sd.create_field(field)
```

#### Output example

```json
{
    "status": "success",
    "api-name": "year"
}
```

### `index(json_data, auto_create_fields=False, test=False)`
Index data to existing entities or create new entities, if necessary. This method corresponds to a [POST request at /index](http://panel.slicingdice.com/docs/#api-details-api-endpoints-post-index).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_OR_WRITE_API_KEY')
index_data = {
    'user1@slicingdice.com': {
        'car-model': 'Ford Ka',
        'year': 2016
    },
    'user2@slicingdice.com': {
        'car-model': 'Honda Fit',
        'year': 2016
    },
    'user3@slicingdice.com': {
        'car-model': 'Toyota Corolla',
        'year': 2010,
        'test-drives': [
            {
                'value': 'NY',
                'date': '2016-08-17T13:23:47+00:00'
            }, {
                'value': 'NY',
                'date': '2016-08-17T13:23:47+00:00'
            }, {
                'value': 'CA',
                'date': '2016-04-05T10:20:30Z'
            }
        ]
    },
    'user4@slicingdice.com': {
        'car-model': 'Ford Ka',
        'year': 2005,
        'test-drives': {
            'value': 'NY',
            'date': '2016-08-17T13:23:47+00:00'
        }
    }
}
print sd.index(index_data)
```

#### Output example

```json
{
    "status": "success",
    "indexed-entities": 4,
    "indexed-fields": 10,
    "took": 0.023
}
```

### `exists_entity(ids, test=False)`
Verify which entities exist in a project given a list of entity IDs. This method corresponds to a [POST request at /query/exists/entity](http://panel.slicingdice.com/docs/#api-details-api-endpoints-post-query-exists-entity).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_OR_READ_API_KEY')
ids = [
    'user1@slicingdice.com',
    'user2@slicingdice.com',
    'user3@slicingdice.com'
]
print sd.exists_entity(ids)
```

#### Output example

```json
{
    "status": "success",
    "exists": [
        "user1@slicingdice.com",
        "user2@slicingdice.com"
    ],
    "not-exists": [
        "user3@slicingdice.com"
    ],
    "took": 0.103
}
```

### `count_entity_total(test=False)`
Count the number of indexed entities. This method corresponds to a [GET request at /query/count/entity/total](http://panel.slicingdice.com/docs/#api-details-api-endpoints-get-query-count-entity-total).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_OR_READ_API_KEY')
print sd.count_entity_total()
```

#### Output example

```json
{
    "status": "success",
    "result": {
        "total": 42
    },
    "took": 0.103
}
```

### `count_entity(json_data, test=False)`
Count the number of entities attending the given query. This method corresponds to a [POST request at /query/count/entity](http://panel.slicingdice.com/docs/#api-details-api-endpoints-post-query-count-entity).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_OR_READ_API_KEY')
query = {
    'users-from-ny-or-ca': [
        {
            'state': {
                'equals': 'NY'
            }
        },
        'or',
        {
            'state-origin': {
                'equals': 'CA'
            }
        },
    ],
    'users-from-ny': [
        {
            'state': {
                'equals': 'NY'
            }
        }
    ],
    'bypass-cache': False
}
print sd.count_entity(query)
```

#### Output example

```json
{
    "status": "success",
    "result": {
        "users-from-ny-or-ca": 175,
        "users-from-ny": 296
    },
    "took": 0.103
}
```

### `count_event(json_data, test=False)`
Count the number of occurrences for time-series events attending the given query. This method corresponds to a [POST request at /query/count/event](http://panel.slicingdice.com/docs/#api-details-api-endpoints-post-query-count-event).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_OR_READ_API_KEY')
query = {
    'users-from-ny-in-jan': [
        {
        'test-field': {
                'equals': 'NY',
                'between': [
                    '2016-01-01T00:00:00Z',
                    '2016-01-31T00:00:00Z'
                ],
                'minfreq': 2
            }
        }
    ],
    'users-from-ny-in-feb': [
        {
            'test-field': {
                'equals': 'NY',
                'between': [
                    '2016-02-01T00:00:00Z',
                    '2016-02-28T00:00:00Z'
                ],
                'minfreq': 2
            }
        }
    ],
    'bypass-cache': True
}
print sd.count_event(query)
```

#### Output example

```json
{
    "status": "success",
    "result": {
        "users-from-ny-in-jan": 175,
        "users-from-ny-in-feb": 296
    },
    "took": 0.103
}
```

### `top_values(json_data, test=False)`
Return the top values for entities attending the given query. This method corresponds to a [POST request at /query/top_values](http://panel.slicingdice.com/docs/#api-details-api-endpoints-post-query-top-values).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_OR_READ_API_KEY')
query = {
    'user-gender': {
        'gender': 2
    },
    'operating-systems': {
        'os': 3
    },
    'linux-operating-systems': {
        'os': 3,
        'contains': [
            'linux',
            'unix'
        ]
    }
}
print sd.top_values(query)
```

#### Output example

```json
{
    "status": "success",
    "result": {
        "user-gender": {
            "gender": [
                {
                    "quantity": 6.0,
                    "value": "male"
                }, {
                    "quantity": 4.0,
                    "value": "female"
                }
            ]
        },
        "operating-systems": {
            "os": [
                {
                    "quantity": 55.0,
                    "value": "windows"
                }, {
                    "quantity": 25.0,
                    "value": "macos"
                }, {
                    "quantity": 12.0,
                    "value": "linux"
                }
            ]
        },
        "linux-operating-systems": {
            "os": [
                {
                    "quantity": 12.0,
                    "value": "linux"
                }, {
                    "quantity": 3.0,
                    "value": "debian-linux"
                }, {
                    "quantity": 2.0,
                    "value": "unix"
                }
            ]
        }
    },
    "took": 0.103
}
```

### `aggregation(json_data, test=False)`
Return the aggregation of all fields in the given query. This method corresponds to a [POST request at /query/aggregation](http://panel.slicingdice.com/docs/#api-details-api-endpoints-post-query-aggregation).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_OR_READ_API_KEY')
query = {
    'query': [
        {
            'gender': 2
        },
        {
            'os': 2,
            'equals': [
                'linux',
                'macos',
                'windows'
            ]
        },
        {
            'browser': 2
        }
    ]
}
print sd.aggregation(query)
```

#### Output example

```json
{
    "status": "success",
    "result": {
        "gender": [
            {
                "quantity": 6,
                "value": "male",
                "os": [
                    {
                        "quantity": 5,
                        "value": "windows",
                        "browser": [
                            {
                                "quantity": 3,
                                "value": "safari"
                            }, {
                                "quantity": 2,
                                "value": "internet explorer"
                            }
                        ]
                    }, {
                        "quantity": 1,
                        "value": "linux",
                        "browser": [
                            {
                                "quantity": 1,
                                "value": "chrome"
                            }
                        ]
                    }
                ]
            }, {
                "quantity": 4,
                "value": "female",
                "os": [
                    {
                        "quantity": 3,
                        "value": "macos",
                        "browser": [
                            {
                                "quantity": 3,
                                "value": "chrome"
                            }
                        ]
                    }, {
                        "quantity": 1,
                        "value": "linux",
                        "browser": [
                            {
                                "quantity": 1,
                                "value": "chrome"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "took": 0.103
}
```

### `get_saved_queries(test=False)`
Get all saved queries. This method corresponds to a [GET request at /query/saved](http://panel.slicingdice.com/docs/#api-details-api-endpoints-get-query-saved).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_API_KEY')
print sd.get_saved_queries()
```

#### Output example

```json
{
    "status": "success",
    "saved-queries": [
        {
            "name": "users-in-ny-or-from-ca",
            "type": "count/entity",
            "query": [
                {
                    "state": {
                        "equals": "NY"
                    }
                },
                "or",
                {
                    "state-origin": {
                        "equals": "CA"
                    }
                }
            ],
            "cache-period": 100
        }, {
            "name": "users-from-ca",
            "type": "count/entity",
            "query": [
                {
                    "state": {
                        "equals": "NY"
                    }
                }
            ],
            "cache-period": 60
        }
    ],
    "took": 0.103
}
```

### `create_saved_query(json_data, test=False)`
Create a saved query at SlicingDice. This method corresponds to a [POST request at /query/saved](http://panel.slicingdice.com/docs/#api-details-api-endpoints-post-query-saved).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_API_KEY')
query = {
    'name': 'my-saved-query',
    'type': 'count/entity',
    'query': [
        {
            'state': {
                'equals': 'NY'
            }
        },
        'or',
        {
            'state-origin': {
                'equals': 'CA'
            }
        }
    ],
    'cache-period': 100
}
print sd.create_saved_query(query)
```

#### Output example

```json
{
    "status": "success",
    "name": "my-saved-query",
    "type": "count/entity",
    "query": [
        {
            "state": {
                "equals": "NY"
            }
        },
        "or",
        {
            "state-origin": {
                "equals": "CA"
            }
        }
    ],
    "cache-period": 100,
    "took": 0.103
}
```

### `update_saved_query(query_name, json_data, test=False)`
Update an existing saved query at SlicingDice. This method corresponds to a [PUT request at /query/saved/QUERY_NAME](http://panel.slicingdice.com/docs/#api-details-api-endpoints-put-query-saved-query-name).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_API_KEY')
new_query = {
    'type': 'count/entity',
    'query': [
        {
            'state': {
                'equals': 'NY'
            }
        },
        'or',
        {
            'state-origin': {
                'equals': 'CA'
            }
        }
    ],
    'cache-period': 100
}
print sd.update_saved_query('my-saved-query', new_query)
```

#### Output example

```json
{
    "status": "success",
    "name": "my-saved-query",
    "type": "count/entity",
    "query": [
        {
            "state": {
                "equals": "NY"
            }
        },
        "or",
        {
            "state-origin": {
                "equals": "CA"
            }
        }
    ],
    "cache-period": 100,
    "took": 0.103
}
```

### `get_saved_query(query_name, test=False)`
Executed a saved query at SlicingDice. This method corresponds to a [GET request at /query/saved/QUERY_NAME](http://panel.slicingdice.com/docs/#api-details-api-endpoints-get-query-saved-query-name).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_OR_READ_API_KEY')
print sd.get_saved_query('my-saved-query')
```

#### Output example

```json
{
    "status": "success",
    "type": "count/entity",
    "query": [
        {
            "state": {
                "equals": "NY"
            }
        },
        "or",
        {
            "state-origin": {
                "equals": "CA"
            }
        }
    ],
    "result": {
        "my-saved-query": 175
    },
    "took": 0.103
}
```

### `delete_saved_query(query_name, test=False)`
Delete a saved query at SlicingDice. This method corresponds to a [DELETE request at /query/saved/QUERY_NAME](http://panel.slicingdice.com/docs/#api-details-api-endpoints-delete-query-saved-query-name).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_API_KEY')
print sd.delete_saved_query('my-saved-query')
```

#### Output example

```json
{
    "status": "success",
    "deleted-query": "my-saved-query",
    "type": "count/entity",
    "query": [
        {
            "state": {
                "equals": "NY"
            }
        },
        "or",
        {
            "state-origin": {
                "equals": "CA"
            }
        }
    ],
    "took": 0.103
}
```

### `result(json_data, test=False)`
Retrieve indexed values for entities attending the given query. This method corresponds to a [POST request at /data_extraction/result](http://panel.slicingdice.com/docs/#api-details-api-endpoints-post-data-extraction-result).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_OR_READ_API_KEY')
query = {
    'query': [
        {
            'users-from-ny': {
                'equals': 'NY'
            }
        },
        'or',
        {
            'users-from-ca': {
                'equals': 'CA'
            }
        }
    ],
    'fields': ['name', 'year'],
    'limit': 2
}
print sd.result(query)
```

#### Output example

```json
{
    "status": "success",
    "data": {
        "user1@slicingdice.com": {
            "name": "John",
            "year": 2016
        },
        "user2@slicingdice.com": {
            "name": "Mary",
            "year": 2005
        }
    },
    "took": 0.103
}
```

### `score(json_data, test=False)`
Retrieve indexed values as well as their relevance for entities attending the given query. This method corresponds to a [POST request at /data_extraction/score](http://panel.slicingdice.com/docs/#api-details-api-endpoints-post-data-extraction-score).

#### Request example

```python
from pyslicer import SlicingDice
sd = SlicingDice('MASTER_OR_READ_API_KEY')
query = {
    'query': [
        {
            'users-from-ny': {
                'equals': 'NY'
            }
        },
        'or',
        {
            'users-from-ca': {
                'equals': 'CA'
            }
        }
    ],
    'fields': ['name', 'year'],
    'limit': 2
}
print sd.score(query)
```

#### Output example

```json
{
    "status": "success",
    "data": {
        "user1@slicingdice.com": {
            "name": "John",
            "year": 2016,
            "score": 2
        },
        "user2@slicingdice.com": {
            "name": "Mary",
            "year": 2005,
            "score": 1
        }
    },
    "took": 0.103
}
```

## License

[MIT](https://opensource.org/licenses/MIT)
