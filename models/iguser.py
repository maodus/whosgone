'''
Copyright (c) 2023, Nicholas Maodus
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
'''

# Represents an instagram user that is followed by or is following you
class IGUser:
    def __init__(self, name, interaction_date):
        self.name = name
        self.interaction_date = interaction_date

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, IGUser):
            return False
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)