#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 PAL Robotics SL. All Rights Reserved
#
# Permission to use, copy, modify, and/or distribute this software for
# any purpose with or without fee is hereby granted, provided that the
# above copyright notice and this permission notice appear in all
# copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Authors:
# * Sammy Pfeiffer
'''
@author: Sammy Pfeiffer

Script that tries to load initially private motions
(in the case of working in PAL premises)
and if the package is not found loads the default
public ones
'''

from rospkg import RosPack, ResourceNotFound
from rosparam import upload_params
from yaml import load

PRIVATE_PKG_NAME = 'reemc_motions_proprietary'
PUBLIC_PKG_NAME = 'reemc_bringup'

PRIVATE_CONFIG_YAML = 'reemc_motions.yaml'
PUBLIC_CONFIG_YAML = 'reemc_motions.yaml'

def load_params_from_yaml(complete_file_path):
    '''Gets the params from a yaml file given the complete path of the
    file and uploads those to the param server.
    This is convenience function as rosparam.load_file does not
    give this functionality as found here:
    http://answers.ros.org/question/169866/load-yaml-with-code/'''
    f = open(full_path, 'r')
    yamlfile = load(f)
    f.close()
    upload_params('/', yamlfile )

if __name__ == '__main__':
    rp = RosPack()
    print "Loading public motions from: " + PUBLIC_PKG_NAME
    pub_pkg_path = rp.get_path(PUBLIC_PKG_NAME)
    pub_config_yaml = PUBLIC_CONFIG_YAML
    pub_full_path = pkg_path + '/config/' + pub_config_yaml
    load_params_from_yaml(pub_full_path)
    print "Trying to find private package: " + PRIVATE_PKG_NAME
    try:
        pkg_path = rp.get_path(PRIVATE_PKG_NAME)
        config_yaml = PRIVATE_CONFIG_YAML
	    full_path = pkg_path + '/config/' + config_yaml
	    print "Loading params from: " +  full_path
	    load_params_from_yaml(full_path)
    except ResourceNotFound:
        print "Not found, only using public motions."

    print "Finished."
    