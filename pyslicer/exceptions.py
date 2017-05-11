#!/usr/bin/env python
# -*- coding: utf-8 -*-


# General SlicingDice Exception

class SlicingDiceException(Exception):
    def __init__(self, *args, **kwargs):
        self.code = kwargs.pop('code', None)
        self.message = kwargs.pop('message', None)
        self.more_info = kwargs.pop('more-info', None)
        super(SlicingDiceException, self).__init__(self, *args, **kwargs)

    def __str__(self):
        return "SlicingDiceException(code={}, message={}, more_info={})".format(
            self.code, self.message, self.more_info)


# Specific SlicingDice Exceptions

class SlicingDiceHTTPError(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(SlicingDiceHTTPError, self).__init__(self, *args, **kwargs)


class DemoUnavailableException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(DemoUnavailableException, self).__init__(self, *args, **kwargs)


class RequestRateLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(RequestRateLimitException, self).__init__(self, *args, **kwargs)


class RequestBodySizeExceededException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(RequestBodySizeExceededException, self).__init__(self, *args, **kwargs)


class IndexEntitiesLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexEntitiesLimitException, self).__init__(self, *args, **kwargs)


class IndexColumnsLimitException(SlicingDiceException):
    def __init__(self, *args, **kwargs):
        super(IndexColumnsLimitException, self).__init__(self, *args, **kwargs)