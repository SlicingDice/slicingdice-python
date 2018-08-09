# Change Log

## [2.1.0]
### Added
- UPDATE support
- DELETE support

## [2.0.2]
### Updated
- Change SQL endpoint from `/query/sql` to `sql`
- Improve client tests

## [2.0.1]
### Updated
- Make client compatible with python 3
- Correct data extraction validator to accept columns: all
- Add support  for SQL queries on client
- Adapt test queries to the changes on SlicingDice API

## [2.0.0]
### Updated
- Update `exists_entity()` to receive `table` as parameter
- Update API errors code
- Remove auto_create_columns parameter from insert method
- Rename SlicingDice API endpoints

## [1.0.0]
### Added
- Thin layers around SlicingDice API endpoints
- Automatic regression test script run_query_tests.py with its JSON data
