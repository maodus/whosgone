'''
Copyright (c) 2023, Nicholas Maodus
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
'''

import configparser
import os

CONF_PATH = "config.ini"

class Config:
    def __init__(self):
        self.conf_parser = configparser.ConfigParser() 

    # Create the config if it doesnt exist or read it if it does
    def initialize(self):
        if not os.path.exists(CONF_PATH):
            self.reset_config()
            with open(CONF_PATH, "w") as config_file:
                self.conf_parser.write(config_file)
        else:
            self.conf_parser.read(CONF_PATH)

    ## Reset the config to default settings
    def reset_config(self):
        self.conf_parser["Settings"] = {"UseHTMLOutput" : "yes"}

    def use_html(self):
        return self.conf_parser.getboolean("Settings", "UseHTMLOutput")