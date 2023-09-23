'''
Copyright (c) 2023, Nicholas Maodus
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
'''

import time
import os
from whosgone.core.output import OutputBase

class HTMLOutput(OutputBase):
    def __init__(self, followers, following):
        super().__init__(followers, following)

    def create_output(self):
        html_str = ""
        with open ("resources/template.html", "r") as template:
            html_str = template.read()
        
        f1_str = "" # Template str
        for i, user in enumerate(sorted(self.non_followers)):
            user_str = str(user)
            f1_str +=  f'<li><a target="_blank" rel="noopener" href="https://www.instagram.com/{user_str}">{user_str}</a></li>'

        f2_str = "" # Template str
        for i, user in enumerate(sorted(self.non_following)):
            user_str = str(user)
            f2_str +=  f'<li><a target="_blank" rel="noopener" href="https://www.instagram.com/{user_str}">{user_str}</a></li>'


        # Replace the template strings with real values
        html_str = html_str \
            .replace("{l1}", str(len(self.non_followers))) \
            .replace("{l2}", str(len(self.non_following))) \
            .replace("{f1}", f1_str) \
            .replace("{f2}", f2_str) \
        
        output_dir = "ig_results/"
        filename = f'ig_{time.strftime("%Y%m%d_%H%M%S")}.html'

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(f"{output_dir}{filename}", "w") as html:
            html.write(html_str)