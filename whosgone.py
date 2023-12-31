'''
Copyright (c) 2023, Nicholas Maodus
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
'''

from whosgone.utils import IGExtractor
from whosgone.core.output import TextOutput, HTMLOutput
from whosgone.core import settings
import os

if __name__ == "__main__":
    settings.initialize()

    zip_path = input("Please enter the file path for your instagram data file: ")
    while not os.path.exists(zip_path) or not zip_path.endswith(".zip"):
        zip_path = input("Input was invalid, please try again: ")

    igextract = IGExtractor(zip_path)

    followers = igextract.get_followers()
    following = igextract.get_following()

    output = None
        
    if settings.use_html():
        output = HTMLOutput(followers, following)
    else:
        output = TextOutput(followers, following)

    output.create_output()
