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


class CustomKeyInvalidcolumnCreationException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(CustomKeyInvalidcolumnCreationException, self).__init__(
            self, *args, **kwargs)


class CustomKeyInvalidPermissionForcolumnException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(CustomKeyInvalidPermissionForcolumnException, self).__init__(
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


# column errors
class columnMissingParamException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnMissingParamException, self).__init__(
            self, *args, **kwargs)


class columnTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnTypeException, self).__init__(
            self, *args, **kwargs)


class columnIntegerValuesException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnIntegerValuesException, self).__init__(
            self, *args, **kwargs)


class columnAlreadyExistsException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnAlreadyExistsException, self).__init__(
            self, *args, **kwargs)


class columnLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnLimitException, self).__init__(
            self, *args, **kwargs)


class columnTimeSeriesLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnTimeSeriesLimitException, self).__init__(
            self, *args, **kwargs)


class columnTimeSeriesSystemLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnTimeSeriesSystemLimitException, self).__init__(
            self, *args, **kwargs)


class columnDecimalTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnDecimalTypeException, self).__init__(
            self, *args, **kwargs)


class columnStorageValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnStorageValueException, self).__init__(
            self, *args, **kwargs)


class columnInvalidApiNameException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnInvalidApiNameException, self).__init__(
            self, *args, **kwargs)


class columnInvalidNameException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnInvalidNameException, self).__init__(
            self, *args, **kwargs)


class columnInvalidDescriptionException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnInvalidDescriptionException, self).__init__(
            self, *args, **kwargs)


class columnExceedDescriptionlengthException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnExceedDescriptionlengthException, self).__init__(
            self, *args, **kwargs)


class columnInvalidCardinalityException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnInvalidCardinalityException, self).__init__(
            self, *args, **kwargs)


class columnDecimalLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnDecimalLimitException, self).__init__(
            self, *args, **kwargs)


class columnRangeLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnRangeLimitException, self).__init__(
            self, *args, **kwargs)


class columnExceededMaxNameLenghtException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnExceededMaxNameLenghtException, self).__init__(
            self, *args, **kwargs)


class columnExceededMaxApiNameLenghtException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnExceededMaxApiNameLenghtException, self).__init__(
            self, *args, **kwargs)


class columnEmptyEntityIdException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnEmptyEntityIdException, self).__init__(
            self, *args, **kwargs)


class columnExceededPermitedValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnExceededPermitedValueException, self).__init__(
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


class InsertcolumnNameTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertcolumnNameTypeException, self).__init__(
            self, *args, **kwargs)


class InsertcolumnTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertcolumnTypeException, self).__init__(
            self, *args, **kwargs)


class InsertEntityNameTooBigException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertEntityNameTooBigException, self).__init__(
            self, *args, **kwargs)


class InsertcolumnValueTooBigException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertcolumnValueTooBigException, self).__init__(
            self, *args, **kwargs)


class InsertTimeSeriesDateFormatException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertTimeSeriesDateFormatException, self).__init__(
            self, *args, **kwargs)


class InsertcolumnNotActiveException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertcolumnNotActiveException, self).__init__(
            self, *args, **kwargs)


class InsertIdLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertIdLimitException, self).__init__(
            self, *args, **kwargs)


class InsertcolumnLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertcolumnLimitException, self).__init__(
            self, *args, **kwargs)


class InsertDateFormatException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertDateFormatException, self).__init__(
            self, *args, **kwargs)


class InsertcolumnStringEmptyValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertcolumnStringEmptyValueException, self).__init__(
            self, *args, **kwargs)


class InsertcolumnTimeseriesInvalidParameterException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertcolumnTimeseriesInvalidParameterException, self).__init__(
            self, *args, **kwargs)


class InsertcolumnNumericInvalidValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertcolumnNumericInvalidValueException, self).__init__(
            self, *args, **kwargs)


class InsertcolumnTimeseriesMissingValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InsertcolumnTimeseriesMissingValueException, self).__init__(
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


class QueryDataExtractioncolumnLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryDataExtractioncolumnLimitException, self).__init__(
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


class QueryParameterInvalidcolumnUsageException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryParameterInvalidcolumnUsageException, self).__init__(
            self, *args, **kwargs)


class QueryInvalidcolumnUsageException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryInvalidcolumnUsageException, self).__init__(
            self, *args, **kwargs)


# Internal errors
class InternalException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InternalException, self).__init__(
            self, *args, **kwargs)


class columnCreateInternalException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnCreateInternalException, self).__init__(
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


class InvalidcolumnTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidcolumnTypeException, self).__init__(self, *args, **kwargs)


class InvalidcolumnException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidcolumnException, self).__init__(self, *args, **kwargs)


class InvalidcolumnNameException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidcolumnNameException, self).__init__(self, *args, **kwargs)


class InvalidcolumnDescriptionException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidcolumnDescriptionException, self).__init__(
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


class columnInvalidRangeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(columnInvalidRangeException, self).__init__(
            self, *args, **kwargs)
