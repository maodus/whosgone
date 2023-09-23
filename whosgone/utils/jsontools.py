'''
Copyright (c) 2023, Nicholas Maodus
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
'''

import json
from whosgone.core.ig import IGUser

# Creates a set containing IGUsers that represent each user in the givin data set
# data is a json string of either the main user's followers or following
# relationship specifies whether we are reading the main users followers or following...
#   relationship can either be "relationships_following" or "relationships_followers"
def instantiate_users(data, relationship):
    json_data = json.loads(data)

    if relationship in json_data:
        json_data = json_data[relationship]

    users = set()
    
    for user_data in json_data:
        user = user_data["string_list_data"][0] # We only need the info regarding the user
        iguser = IGUser(user["value"], str(user["timestamp"]))
        users.add(iguser)

    return users
