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


class CustomKeyInvalidPermissionForFieldException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(CustomKeyInvalidPermissionForFieldException, self).__init__(
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


# Field errors
class FieldMissingParamException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldMissingParamException, self).__init__(
            self, *args, **kwargs)


class FieldTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldTypeException, self).__init__(
            self, *args, **kwargs)


class FieldIntegerValuesException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldIntegerValuesException, self).__init__(
            self, *args, **kwargs)


class FieldAlreadyExistsException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldAlreadyExistsException, self).__init__(
            self, *args, **kwargs)


class FieldLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldLimitException, self).__init__(
            self, *args, **kwargs)


class FieldTimeSeriesLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldTimeSeriesLimitException, self).__init__(
            self, *args, **kwargs)


class FieldTimeSeriesSystemLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldTimeSeriesSystemLimitException, self).__init__(
            self, *args, **kwargs)


class FieldDecimalTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldDecimalTypeException, self).__init__(
            self, *args, **kwargs)


class FieldStorageValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldStorageValueException, self).__init__(
            self, *args, **kwargs)


class FieldInvalidApiNameException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldInvalidApiNameException, self).__init__(
            self, *args, **kwargs)


class FieldInvalidNameException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldInvalidNameException, self).__init__(
            self, *args, **kwargs)


class FieldInvalidDescriptionException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldInvalidDescriptionException, self).__init__(
            self, *args, **kwargs)


class FieldInvalidCardinalityException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldInvalidCardinalityException, self).__init__(
            self, *args, **kwargs)


class FieldDecimalLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldDecimalLimitException, self).__init__(
            self, *args, **kwargs)


class FieldRangeLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldRangeLimitException, self).__init__(
            self, *args, **kwargs)


# Index errors
class IndexEntityKeyTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexEntityKeyTypeException, self).__init__(
            self, *args, **kwargs)


class IndexEntityValueTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexEntityValueTypeException, self).__init__(
            self, *args, **kwargs)


class IndexFieldNameTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexFieldNameTypeException, self).__init__(
            self, *args, **kwargs)


class IndexFieldTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexFieldTypeException, self).__init__(
            self, *args, **kwargs)


class IndexEntityNameTooBigException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexEntityNameTooBigException, self).__init__(
            self, *args, **kwargs)


class IndexFieldValueTooBigException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexFieldValueTooBigException, self).__init__(
            self, *args, **kwargs)


class IndexDateFormatException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexDateFormatException, self).__init__(
            self, *args, **kwargs)


class IndexFieldNotActiveException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexFieldNotActiveException, self).__init__(
            self, *args, **kwargs)


class IndexIdLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexIdLimitException, self).__init__(
            self, *args, **kwargs)


class IndexFieldLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexFieldLimitException, self).__init__(
            self, *args, **kwargs)


class IndexFieldStringEmptyValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexFieldStringEmptyValueException, self).__init__(
            self, *args, **kwargs)


class IndexFieldTimeseriesInvalidParameterException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexFieldTimeseriesInvalidParameterException, self).__init__(
            self, *args, **kwargs)


class IndexFieldNumericInvalidValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexFieldNumericInvalidValueException, self).__init__(
            self, *args, **kwargs)


class IndexFieldTimeseriesMissingValueException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexFieldTimeseriesMissingValueException, self).__init__(
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


class QueryFieldNotActiveException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryFieldNotActiveException, self).__init__(
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


class QueryDateFormatException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryDateFormatException, self).__init__(
            self, *args, **kwargs)


class QueryIntegerException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryIntegerException, self).__init__(
            self, *args, **kwargs)


class QueryFieldLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryFieldLimitException, self).__init__(
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


class QueryDataExtractionFieldLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(QueryDataExtractionFieldLimitException, self).__init__(
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


# Internal errors
class InternalException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InternalException, self).__init__(
            self, *args, **kwargs)


class FieldCreateInternalException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(FieldCreateInternalException, self).__init__(
            self, *args, **kwargs)


# CLIENT EXCEPTIONS
class EmptyParameterException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(EmptyParameterException, self).__init__(self, *args, **kwargs)


class WrongTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(WrongTypeException, self).__init__(self, *args, **kwargs)


class InvalidIndexException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidIndexException, self).__init__(self, *args, **kwargs)


class InvalidQueryTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidQueryTypeException, self).__init__(self, *args, **kwargs)


class InvalidFieldTypeException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidFieldTypeException, self).__init__(self, *args, **kwargs)


class InvalidFieldException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidFieldException, self).__init__(self, *args, **kwargs)


class InvalidFieldNameException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidFieldNameException, self).__init__(self, *args, **kwargs)


class InvalidFieldDescriptionException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(InvalidFieldDescriptionException, self).__init__(
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
