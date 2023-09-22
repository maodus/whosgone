'''
Copyright (c) 2023, Nicholas Maodus
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
'''

from whosgone.core.output import OutputBase

class TextOutput(OutputBase):
    def __init__(self, followers, following):
        super().__init__(followers, following)

    def create_output(self):
        print(f"Users that don't follow you back ({len(self.non_followers)}/{self.following_len}): ")

        for i, user in enumerate(self.non_followers):
            print(f"{i + 1}. {user}")

        print(f"\nUsers that you dont follow back ({len(self.non_following)}/{self.follower_len}): ")

        for i, user in enumerate(self.non_following):
            print(f"{i + 1}. {user}")