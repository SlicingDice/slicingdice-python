#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ujson
import requests

import pyslicer.exceptions as exceptions

from pyslicer.core.handler_response import SDHandlerResponse
from pyslicer.core.requester import Requester


class SlicingDiceAPI(object):
    """A python interface to make requests in Slicing Dice API"""

    BASE_URL = os.environ.get(
        'SD_API_ADDRESS',
        'https://api.slicingdice.com/v1')

    def __init__(
        self, master_key=None, write_key=None, read_key=None,
            custom_key=None, use_ssl=False, timeout=60):
        """Instantiate a new SlicerDicer object.

        Keyword arguments:
        key(string or SlicerKey) -- Key(s) to access API
        timeout(int) -- Define timeout to request,
            defaults 30 secs(Optional).
        use_ssl(bool) -- Define if the request uses verification SSL for
            HTTPS requests. Defaults False.(Optional)
        """
        self.keys = self._organize_keys(
            master_key, custom_key, read_key, write_key)
        self._api_key = self._get_key()[0]
        self._requester = Requester(use_ssl, timeout)
        self.__status_code = None
        self.__headers = None

    @property
    def status_code(self):
        return self.__status_code

    @property
    def headers(self):
        return self.__headers

    def _organize_keys(self, master_key, custom_key, read_key, write_key):
        return {
            "master_key": master_key,
            "custom_key": custom_key,
            "read_key": read_key,
            "write_key": write_key
        }

    def _get_key(self):
        if self.keys["master_key"] is not None:
            return [self.keys["master_key"], 2]
        elif self.keys["custom_key"] is not None:
            return [self.keys["custom_key"], 2]
        elif self.keys["write_key"] is not None:
            return [self.keys["write_key"], 1]
        elif self.keys["read_key"] is not None:
            return [self.keys["read_key"], 0]
        raise exceptions.InvalidSlicingDiceKeysException("You need put a key.")

    def _check_key(self, key_level):
        """Select automatically a key to make the request in Slicing Dice

        Keyword arguments:
        need_write(bool) -- Define if this request needs write in Slicing
            Dice API.
        """
        current_key_level = self._get_key()
        if current_key_level[1] == 2:
            return current_key_level[0]
        if current_key_level[1] != key_level:
            raise exceptions.InvalidSlicingDiceKeysException(
                "This key is not allowed to perform this operation.")
        return current_key_level[0]

    def _make_request(self, url, req_type, key_level, json_data=None):
        """Returns a object request result"""
        self._check_key(key_level)
        headers = {'Content-Type': 'application/json',
                   'Authorization': self._api_key}

        req = None

        if req_type == "post":
            req = self._requester.post(
                url,
                data=json_data,
                headers=headers)
        elif req_type == "get":
            req = self._requester.get(
                url,
                headers=headers)

        elif req_type == "delete":
            req = self._requester.get(
                url,
                headers=headers)

        elif req_type == "put":
            req = self._requester.put(
                url,
                data=json_data,
                headers=headers)

        return self._handler_request(req)

    def _handler_request(self, req):
        """Handler request response"""
        if req is None:
            raise exceptions.SlicingDiceException("Bad request.")

        try:
            result = ujson.loads(req.text)
        except ValueError:
            raise exceptions.InternalException

        sd_response = SDHandlerResponse(
            result=result,
            status_code=req.status_code,
            headers=req.headers)

        if sd_response.request_successful():
            if self._check_request(req):
                self._set_properties_values(sd_response)
                return sd_response.result

    def _check_request(self, request):
        """Check if the request was successful

        Keyword arguments:
        request -- A object request result
        """
        if request.status_code is not requests.codes.ok:
            raise exceptions.SlicingDiceHTTPError(
                "HTTP status code: {}".format(request.status_code))
        return True

    def _set_properties_values(self, sd_response):
        """Set current status code and header request response in objects

        Keyword arguments:
        sd_response -- A request object
        """
        self.__status_code = int(sd_response.status_code)
        self.__headers = dict(sd_response.headers)
