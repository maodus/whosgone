'''
Copyright (c) 2023, Nicholas Maodus
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
'''

from abc import ABC, abstractmethod

class OutputBase(ABC):
    def __init__(self, followers, following):
        self.follower_len = len(followers)
        self.following_len = len(following)

        self.non_followers = following - followers
        self.non_following = followers - following

    @abstractmethod
    def create_output(self):
        pass
