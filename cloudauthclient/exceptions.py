# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2013 Penguin Computing, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

class ClientException(Exception):
    """Base exception class for all exceptions this library raises"""
    pass


class NoEndpointError(ClientException):
    """No endpoint/URL found"""
    pass


class AuthenticationError(ClientException):
    """Could not authenticate with CloudAuth"""
    pass
