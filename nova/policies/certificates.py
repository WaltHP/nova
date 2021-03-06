# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.policies import base


POLICY_ROOT = 'os_compute_api:os-certificates:%s'


certificates_policies = [
    base.create_rule_default(
        POLICY_ROOT % 'create',
        base.RULE_ADMIN_OR_OWNER,
        "Create a root certificate. This API is deprecated.",
        [
            {
                'method': 'POST',
                'path': '/os-certificates'
            }
        ]),
    base.create_rule_default(
        POLICY_ROOT % 'show',
        base.RULE_ADMIN_OR_OWNER,
        "Show details for a root certificate.  This API is deprecated.",
        [
            {
                'method': 'GET',
                'path': '/os-certificates/root'
            }
        ])
]


def list_rules():
    return certificates_policies
