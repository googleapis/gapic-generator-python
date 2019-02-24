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


def test_crud_with_request(identity):
    count = len(identity.list_users({}).users)
    user = identity.create_user({'user': {
        'display_name': 'Guido van Rossum',
        'email': 'guido@guido.fake',
    }})
    try:
        assert user.display_name == 'Guido van Rossum'
        assert user.email == 'guido@guido.fake'
        assert len(identity.list_users({}).users) == count + 1
        assert identity.get_user({
            'name': user.name,
        }).display_name == 'Guido van Rossum'
    finally:
        identity.delete_user({'name': user.name})


def test_crud_flattened(identity):
    count = len(identity.list_users({}).users)
    user = identity.create_user(
        display_name='Monty Python',
        email='monty@python.org',
    )
    try:
        assert user.display_name == 'Monty Python'
        assert user.email == 'monty@python.org'
        assert len(identity.list_users({}).users) == count + 1
        assert identity.get_user({
            'name': user.name,
        }).display_name == 'Monty Python'
    finally:
        identity.delete_user({'name': user.name})
