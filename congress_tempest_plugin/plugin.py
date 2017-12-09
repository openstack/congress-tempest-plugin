# Copyright 2015 Intel
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


import os

from tempest import config
from tempest.test_discover import plugins

from congress_tempest_plugin import config as config_congress


class CongressTempestPlugin(plugins.TempestPlugin):
    def load_tests(self):
        base_path = os.path.split(os.path.dirname(
            os.path.abspath(__file__)))[0]
        test_dir = "congress_tempest_plugin/tests"
        full_test_dir = os.path.join(base_path, test_dir)
        return full_test_dir, base_path

    def register_opts(self, conf):
        config.register_opt_group(conf,
                                  config_congress.service_available_group,
                                  config_congress.ServiceAvailableGroup)
        config.register_opt_group(conf, config_congress.congressha_group,
                                  config_congress.CongressHAGroup)

    def get_opt_lists(self):
        return [
            (config_congress.congressha_group.name,
             config_congress.CongressHAGroup),
            (config_congress.service_available_group.name,
             config_congress.ServiceAvailableGroup)
        ]
