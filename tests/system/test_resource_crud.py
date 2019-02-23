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

import pytest


def test_crud_with_request_dict(identity):
    if len(identity.list_users({}).users) > 0:
        pytest.xfail(reason='Unexpected state.')
    try:
        user = identity.create_user({'user': {
            'display_name': 'Guido van Rossum',
            'email': 'guido@guido.fake',
        }})
        assert user.display_name == 'Guido van Rossum'
        assert user.email == 'guido@guido.fake'
        assert len(identity.list_users({}).users) == 1
        assert identity.get_user({
            'name': user.name,
        }).display_name == 'Guido van Rossum'
    finally:
        identity.delete_user({'name': user.name})


def test_crud_with_signatures(identity):
    if len(identity.list_users({}).users) > 0:
        pytest.xfail(reason='Unexpected state.')
    try:
        user = identity.create_user(
            display_name='Guido van Rossum',
            email='guido',
        )
        assert user.display_name == 'Guido van Rossum'
        assert user.email == 'guido@guido.fake'
        assert len(identity.list_users({}).users) == 1
        assert identity.get_user(name=user.name).email == 'guido@guido.fake'
    finally:
        identity.delete_user(name=user.name)
