# SPDX-License-Identifier: LGPL-2.1-or-later

# Copyright (C) 2020, 2021 igo95862

# This file is part of python-sdbus

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
from __future__ import annotations

from unittest import TestCase

from sdbus_block.secrets import (
    SecretService,
    SecretCollection,
    SecretItem,
)


class TestSecrets(TestCase):

    def test_print_list_of_secrets(self) -> None:
        secrets = SecretService()

        print('Default alias: ', secrets.read_alias('default'))

        print('Collections: ', secrets.collections)

    def test_open_session(self) -> None:
        secrets_service = SecretService()

        session_algorithm = 'plain'  # Plain mode, no encryption
        session_input = ('s', '')  # Vartiant of an empty string

        _, my_session_path = secrets_service.open_session(
            session_algorithm,
            session_input,
        )

        print('Opened session path: ', my_session_path)

    def test_find_default_collection(self) -> None:
        secrets_service = SecretService()

        default_collection = secrets_service.read_alias('default')
        print('Default collection: ', default_collection)

    def test_create_and_delete_secret(self) -> None:
        secrets_service = SecretService()

        session_algorithm = 'plain'  # Plain mode, no encryption
        session_input = ('s', '')  # Vartiant of an empty string

        _, my_session_path = secrets_service.open_session(
            session_algorithm,
            session_input,
        )

        default_collection_path = secrets_service.read_alias('default')
        default_collection = SecretCollection(default_collection_path)

        secret_properties_dict = {
            'org.freedesktop.Secret.Item.Label': ('s', 'MyItem'),
            'org.freedesktop.Secret.Item.Type': ('s', 'Test'),
            'org.freedesktop.Secret.Item.Attributes': ('a{ss}', {
                "Attribute1": "Value1",
                "Attribute2": "Value2",
            })
        }

        new_secret_path, prompt = default_collection.create_item(
            secret_properties_dict,
            (
                my_session_path,  # session path
                b'',  # encryption parameters, empty in plain mode
                b'my secret',  # secret value it self
                'text/plain; charset=utf8',  # content type
            ),
            False,  # do not replace secret with same attributes
        )

        print('New secret: ', new_secret_path)

        secret = SecretItem(new_secret_path)

        print('Secret data: ', secret.get_secret(my_session_path))

        secret.delete()
