# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from datetime import datetime

import google.showcase as showcase
from google.showcase_v1beta1 import User
from google.protobuf.timestamp_pb2 import Timestamp
from proto.datetime_helpers import DatetimeWithNanoseconds
import random

#from google.showcase import User <----- works in both nextgen and proto-plus clients
#from google.showcase_v1beta1 import User <----- works in both nextgen and proto-plus clients
#from google.showcase_v1beta1.types import User <----- works in both nextgen and proto-plus clients
#from google.showcase_v1beta1.types.identity import User <----- proto-plus clients only
#from google.showcase_v1beta1.types.identity_pb2 import User <----- protobuf clients only


def create_user_and_return_response(identity_client):
    user_name=f"test_user{random.randrange(1000)}"
    user = User(
        name=user_name, display_name=user_name, email=f"{user_name}@example.com"
    )
    return identity_client.create_user(
        request=showcase.CreateUserRequest(user=user)
    )

def test_list_users_response(identity):
    response = create_user_and_return_response(identity_client=identity)
    assert type(response.create_time) == DatetimeWithNanoseconds
    assert isinstance(response.create_time, datetime)

def test_list_users_response_next_gen(identity):
    response = create_user_and_return_response(identity_client=identity)
    assert type(response.create_time) == Timestamp
    assert isinstance(response.create_time.ToDatetime(), datetime)
    # Create a Timestamp from seconds
    assert Timestamp(seconds= 1335020400).ToDatetime() == datetime.fromtimestamp(timestamp=1335020400)
    # Create a Timestamp from datetime
    # This feature is still wonky
    # See https://github.com/protocolbuffers/protobuf/issues/3986
    # When this assert fails, the bug is fixed
    assert Timestamp().FromDatetime(datetime(2012, 4, 21, 15, 0)) != datetime(2012, 4, 21, 15, 0)

    # Instead this workaround is needed
    t = Timestamp()
    t.FromDatetime(datetime(2012, 4, 21, 15, 0))
    assert t.ToDatetime() == datetime(2012, 4, 21, 15, 0)

    


