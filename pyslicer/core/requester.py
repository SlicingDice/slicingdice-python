#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

import pyslicer.exceptions as exceptions


class Requester(object):
    def __init__(self, use_ssl, timeout):
        self.use_ssl = use_ssl
        self.timeout = timeout
        self.session = requests.Session()

    def post(self, url, data, headers):
        """Executes a post request result object"""
        try:
            return self.session.post(
                url,
                data=data,
                verify=self.use_ssl,
                headers=headers,
                timeout=self.timeout)
        except requests.ConnectionError as e:
            raise exceptions.SlicingDiceHTTPError(e)
        except requests.Timeout as e:
            raise exceptions.SlicingDiceHTTPError(e)

    def put(self, url, data, headers):
        """Returns a put request result object"""
        try:
            return self.session.put(
                url,
                data=data,
                verify=self.use_ssl,
                headers=headers,
                timeout=self.timeout)
        except requests.ConnectionError as e:
            raise exceptions.SlicingDiceHTTPError(e)
        except requests.Timeout as e:
            raise exceptions.SlicingDiceHTTPError(e)

    def get(self, url, headers):
        """Returns a get request result object"""
        try:
            return self.session.get(
                url,
                verify=self.use_ssl,
                headers=headers,
                timeout=self.timeout)
        except requests.ConnectionError as e:
            raise exceptions.SlicingDiceHTTPError(e)
        except requests.Timeout as e:
            raise exceptions.SlicingDiceHTTPError(e)

    def delete(self, url, headers):
        """Returns a delete request result object"""
        try:
            return self.session.delete(
                url,
                verify=self.use_ssl,
                headers=headers,
                timeout=self.timeout)
        except requests.ConnectionError as e:
            raise exceptions.SlicingDiceHTTPError(e)
        except requests.Timeout as e:
            raise exceptions.SlicingDiceHTTPError(e)
