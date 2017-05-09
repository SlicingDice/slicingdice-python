#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Base SlicingDice Exception
class SlicingDiceException(Exception):
    def __init__(self, *args, **kwargs):
        super(SlicingDiceException, self).__init__(self, *args, **kwargs)


# Base SlicingDice Exception
class SlicingDiceHTTPError(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(SlicingDiceHTTPError, self).__init__(self, *args, **kwargs)


# Authentication and Authorization errors
class AuthMissingHeaderException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(AuthMissingHeaderException, self).__init__(self, *args, **kwargs)


class AuthAPIKeyException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(AuthAPIKeyException, self).__init__(self, *args, **kwargs)


class AuthInvalidAPIKeyException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(AuthInvalidAPIKeyException, self).__init__(self, *args, **kwargs)


class AuthIncorrectPermissionException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(AuthIncorrectPermissionException, self).__init__(
            self, *args, **kwargs)


class AuthInvalidRemoteException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(AuthInvalidRemoteException, self).__init__(
            self, *args, **kwargs)


class CustomKeyInvalidColumnCreationException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(CustomKeyInvalidColumnCreationException, self).__init__(
            self, *args, **kwargs)


class CustomKeyInvalidPermissionForColumnException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(CustomKeyInvalidPermissionForColumnException, self).__init__(
            self, *args, **kwargs)


class CustomKeyInvalidOperationException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(CustomKeyInvalidOperationException, self).__init__(
            self, *args, **kwargs)


class CustomKeyNotPermittedException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(CustomKeyNotPermittedException, self).__init__(
            self, *args, **kwargs)


class CustomKeyRouteNotPermittedException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(CustomKeyRouteNotPermittedException, self).__init__(
            self, *args, **kwargs)


class DemoApiInvalidEndpointException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(DemoApiInvalidEndpointException, self).__init__(
            self, *args, **kwargs)


# Request validations
class RequestMissingContentTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(RequestMissingContentTypeException, self).__init__(
            self, *args, **kwargs)


class RequestIncorrectContentTypeValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(RequestIncorrectContentTypeValueException, self).__init__(
            self, *args, **kwargs)


class RequestRateLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(RequestRateLimitException, self).__init__(
            self, *args, **kwargs)


class RequestInvalidJsonException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(RequestInvalidJsonException, self).__init__(
            self, *args, **kwargs)


class RequestInvalidHttpMethodException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(RequestInvalidHttpMethodException, self).__init__(
            self, *args, **kwargs)


class RequestInvalidEndpointException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(RequestInvalidEndpointException, self).__init__(
            self, *args, **kwargs)


class RequestIncorrectHttpException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(RequestIncorrectHttpException, self).__init__(
            self, *args, **kwargs)


class RequestExceedLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(RequestExceedLimitException, self).__init__(
            self, *args, **kwargs)


# Account Errors
class AccountMissingPaymentMethodException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(AccountMissingPaymentMethodException, self).__init__(
            self, *args, **kwargs)


class AccountPaymentRequiredException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(AccountPaymentRequiredException, self).__init__(
            self, *args, **kwargs)


class AccountBannedException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(AccountBannedException, self).__init__(
            self, *args, **kwargs)


class AccountDisabledException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(AccountDisabledException, self).__init__(
            self, *args, **kwargs)


# Column errors
class ColumnMissingParamException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnMissingParamException, self).__init__(
            self, *args, **kwargs)


class ColumnTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnTypeException, self).__init__(
            self, *args, **kwargs)


class ColumnIntegerValuesException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnIntegerValuesException, self).__init__(
            self, *args, **kwargs)


class ColumnAlreadyExistsException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnAlreadyExistsException, self).__init__(
            self, *args, **kwargs)


class ColumnLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnLimitException, self).__init__(
            self, *args, **kwargs)


class ColumnTimeSeriesLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnTimeSeriesLimitException, self).__init__(
            self, *args, **kwargs)


class ColumnTimeSeriesSystemLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnTimeSeriesSystemLimitException, self).__init__(
            self, *args, **kwargs)


class ColumnDecimalTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnDecimalTypeException, self).__init__(
            self, *args, **kwargs)


class ColumnStorageValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnStorageValueException, self).__init__(
            self, *args, **kwargs)


class ColumnInvalidApiNameException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnInvalidApiNameException, self).__init__(
            self, *args, **kwargs)


class ColumnInvalidNameException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnInvalidNameException, self).__init__(
            self, *args, **kwargs)


class ColumnInvalidDescriptionException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnInvalidDescriptionException, self).__init__(
            self, *args, **kwargs)


class ColumnExceedDescriptionlengthException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnExceedDescriptionlengthException, self).__init__(
            self, *args, **kwargs)


class ColumnInvalidCardinalityException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnInvalidCardinalityException, self).__init__(
            self, *args, **kwargs)


class ColumnDecimalLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnDecimalLimitException, self).__init__(
            self, *args, **kwargs)


class ColumnRangeLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnRangeLimitException, self).__init__(
            self, *args, **kwargs)


class ColumnExceededMaxNameLenghtException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnExceededMaxNameLenghtException, self).__init__(
            self, *args, **kwargs)


class ColumnExceededMaxApiNameLenghtException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnExceededMaxApiNameLenghtException, self).__init__(
            self, *args, **kwargs)


class ColumnEmptyEntityIdException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnEmptyEntityIdException, self).__init__(
            self, *args, **kwargs)


class ColumnExceededPermitedValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnExceededPermitedValueException, self).__init__(
            self, *args, **kwargs)


# Insertion errors
class InsertInvalidDecimalPlacesException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertInvalidDecimalPlacesException, self).__init__(
            self, *args, **kwargs)


class InsertEntityValueTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertEntityValueTypeException, self).__init__(
            self, *args, **kwargs)


class InsertColumnNameTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertColumnNameTypeException, self).__init__(
            self, *args, **kwargs)


class InsertColumnTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertColumnTypeException, self).__init__(
            self, *args, **kwargs)


class InsertEntityNameTooBigException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertEntityNameTooBigException, self).__init__(
            self, *args, **kwargs)


class InsertColumnValueTooBigException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertColumnValueTooBigException, self).__init__(
            self, *args, **kwargs)


class InsertTimeSeriesDateFormatException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertTimeSeriesDateFormatException, self).__init__(
            self, *args, **kwargs)


class InsertColumnNotActiveException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertColumnNotActiveException, self).__init__(
            self, *args, **kwargs)


class InsertIdLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertIdLimitException, self).__init__(
            self, *args, **kwargs)


class InsertColumnLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertColumnLimitException, self).__init__(
            self, *args, **kwargs)


class InsertDateFormatException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertDateFormatException, self).__init__(
            self, *args, **kwargs)


class InsertColumnStringEmptyValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertColumnStringEmptyValueException, self).__init__(
            self, *args, **kwargs)


class InsertColumnTimeseriesInvalidParameterException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertColumnTimeseriesInvalidParameterException, self).__init__(
            self, *args, **kwargs)


class InsertColumnNumericInvalidValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertColumnNumericInvalidValueException, self).__init__(
            self, *args, **kwargs)


class InsertColumnTimeseriesMissingValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertColumnTimeseriesMissingValueException, self).__init__(
            self, *args, **kwargs)


class QueryTimeSeriesInvalidPrecisionSecondsException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryTimeSeriesInvalidPrecisionSecondsException, self).__init__(
            self, *args, **kwargs)


class QueryTimeSeriesInvalidPrecisionMinutesException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryTimeSeriesInvalidPrecisionMinutesException, self).__init__(
            self, *args, **kwargs)


class QueryTimeSeriesInvalidPrecisionHoursException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryTimeSeriesInvalidPrecisionHoursException, self).__init__(
            self, *args, **kwargs)


class QueryRelativeIntervalException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryRelativeIntervalException, self).__init__(
            self, *args, **kwargs)


class QueryDateFormatException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryDateFormatException, self).__init__(
            self, *args, **kwargs)


# Query errors
class QueryMissingQueryException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryMissingQueryException, self).__init__(
            self, *args, **kwargs)


class QueryInvalidTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryInvalidTypeException, self).__init__(
            self, *args, **kwargs)


class QueryMissingTypeParamException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryMissingTypeParamException, self).__init__(
            self, *args, **kwargs)


class QueryInvalidOperatorException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryInvalidOperatorException, self).__init__(
            self, *args, **kwargs)


class QueryIncorrectOperatorUsageException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryIncorrectOperatorUsageException, self).__init__(
            self, *args, **kwargs)


class QueryColumnNotActiveException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryColumnNotActiveException, self).__init__(
            self, *args, **kwargs)


class QueryMissingOperatorException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryMissingOperatorException, self).__init__(
            self, *args, **kwargs)


class QueryIncompleteException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryIncompleteException, self).__init__(
            self, *args, **kwargs)


class QueryEventCountQueryException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryEventCountQueryException, self).__init__(
            self, *args, **kwargs)


class QueryInvalidMetricException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryInvalidMetricException, self).__init__(
            self, *args, **kwargs)


class QueryIntegerException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryIntegerException, self).__init__(
            self, *args, **kwargs)


class QueryColumnLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryColumnLimitException, self).__init__(
            self, *args, **kwargs)


class QueryLevelLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryLevelLimitException, self).__init__(
            self, *args, **kwargs)


class QueryBadAggsFormationException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryBadAggsFormationException, self).__init__(
            self, *args, **kwargs)


class QueryInvalidAggFilterException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryInvalidAggFilterException, self).__init__(
            self, *args, **kwargs)


class QueryMetricsLevelException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryMetricsLevelException, self).__init__(
            self, *args, **kwargs)


class QueryTimeSeriesException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryTimeSeriesException, self).__init__(
            self, *args, **kwargs)


class QueryMetricsTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryMetricsTypeException, self).__init__(
            self, *args, **kwargs)


class QueryContainsNumericException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryContainsNumericException, self).__init__(
            self, *args, **kwargs)


class QueryExistsEntityLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryExistsEntityLimitException, self).__init__(
            self, *args, **kwargs)


class QueryMultipleFiltersException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryMultipleFiltersException, self).__init__(
            self, *args, **kwargs)


class QueryContainsValueTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryContainsValueTypeException, self).__init__(
            self, *args, **kwargs)


class QueryMissingNameParamException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryMissingNameParamException, self).__init__(
            self, *args, **kwargs)


class QuerySavedAlreadyExistsException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QuerySavedAlreadyExistsException, self).__init__(
            self, *args, **kwargs)


class QuerySavedNotExistsException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QuerySavedNotExistsException, self).__init__(
            self, *args, **kwargs)


class QuerySavedInvalidTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QuerySavedInvalidTypeException, self).__init__(
            self, *args, **kwargs)


class MethodNotAllowedException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(MethodNotAllowedException, self).__init__(
            self, *args, **kwargs)


class QueryExistsMissingIdsException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryExistsMissingIdsException, self).__init__(
            self, *args, **kwargs)


class QueryInvalidFormatException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryInvalidFormatException, self).__init__(
            self, *args, **kwargs)


class QueryTopValuesParameterEmptyException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryTopValuesParameterEmptyException, self).__init__(
            self, *args, **kwargs)


class QueryDataExtractionLimitValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryDataExtractionLimitValueException, self).__init__(
            self, *args, **kwargs)


class QueryDataExtractionLimitValueTooBigException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryDataExtractionLimitValueTooBigException, self).__init__(
            self, *args, **kwargs)


class QueryDataExtractionLimitAndPageTokenValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryDataExtractionLimitAndPageTokenValueException,
              self).__init__(self, *args, **kwargs)


class QueryDataExtractionPageTokenValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryDataExtractionPageTokenValueException, self).__init__(
            self, *args, **kwargs)


class QueryDataExtractionColumnLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryDataExtractionColumnLimitException, self).__init__(
            self, *args, **kwargs)


class QueryExistsEntityEmptyException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryExistsEntityEmptyException, self).__init__(
            self, *args, **kwargs)


class QuerySavedInvalidQueryValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QuerySavedInvalidQueryValueException, self).__init__(
            self, *args, **kwargs)


class QuerySavedInvalidCachePeriodValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QuerySavedInvalidCachePeriodValueException, self).__init__(
            self, *args, **kwargs)


class QuerySavedInvalidNameException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QuerySavedInvalidNameException, self).__init__(
            self, *args, **kwargs)


class QueryCountInvalidParameterException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryCountInvalidParameterException, self).__init__(
            self, *args, **kwargs)


class QueryAggregationInvalidParameterException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryAggregationInvalidParameterException, self).__init__(
            self, *args, **kwargs)


class QueryAggregationInvalidFilterQueryException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryAggregationInvalidFilterQueryException, self).__init__(
            self, *args, **kwargs)


class QueryCountInvalidParameterErrorException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryCountInvalidParameterErrorException, self).__init__(
            self, *args, **kwargs)


class QueryInvalidMinfreqException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryInvalidMinfreqException, self).__init__(
            self, *args, **kwargs)


class QueryExceededMaxNumberQuerysException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryExceededMaxNumberQuerysException, self).__init__(
            self, *args, **kwargs)


class QueryInvalidOperatorUsageException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryInvalidOperatorUsageException, self).__init__(
            self, *args, **kwargs)


class QueryInvalidParameterUsageException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryInvalidParameterUsageException, self).__init__(
            self, *args, **kwargs)


class QueryParameterInvalidColumnUsageException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryParameterInvalidColumnUsageException, self).__init__(
            self, *args, **kwargs)


class QueryInvalidColumnUsageException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryInvalidColumnUsageException, self).__init__(
            self, *args, **kwargs)


# Internal errors
class InternalException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InternalException, self).__init__(
            self, *args, **kwargs)


class ColumnCreateInternalException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnCreateInternalException, self).__init__(
            self, *args, **kwargs)


# CLIENT EXCEPTIONS
class EmptyParameterException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(EmptyParameterException, self).__init__(self, *args, **kwargs)


class WrongTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(WrongTypeException, self).__init__(self, *args, **kwargs)


class InvalidInsertException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidInsertException, self).__init__(self, *args, **kwargs)


class InvalidQueryTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidQueryTypeException, self).__init__(self, *args, **kwargs)


class InvalidColumnTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidColumnTypeException, self).__init__(self, *args, **kwargs)


class InvalidColumnException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidColumnException, self).__init__(self, *args, **kwargs)


class InvalidColumnNameException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidColumnNameException, self).__init__(self, *args, **kwargs)


class InvalidColumnDescriptionException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidColumnDescriptionException, self).__init__(
            self, *args, **kwargs)


class InvalidQueryException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidQueryException, self).__init__(self, *args, **kwargs)


class MaxLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(MaxLimitException, self).__init__(self, *args, **kwargs)


class InvalidEntityExtistsException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidEntityExtistsException, self).__init__(
            self, *args, **kwargs)


class InvalidSlicingDiceKeysException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidSlicingDiceKeysException, self).__init__(
            self, *args, **kwargs)


class ColumnInvalidRangeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(ColumnInvalidRangeException, self).__init__(
            self, *args, **kwargs)
