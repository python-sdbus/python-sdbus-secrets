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

from typing import Optional

from sdbus.sd_bus_internals import SdBus

from .interfaces import (
    SecretCollectionInterface,
    SecretItemInterface,
    SecretPromptInterface,
    SecretServiceInterface,
    SecretSessionInterface,
)

SECRET_SERVICE_BUS_NAME = 'org.freedesktop.secrets'
SECRET_SERVICE_PATH = '/org/freedesktop/secrets'


class SecretService(SecretServiceInterface):
    """Secret service main object.

    Implements :py:class:`SecretServiceInterface`

    Bus name and object path is predetermined at ``org.freedesktop.secrets``
    and ``/org/freedesktop/secrets`` respectively.
    """

    def __init__(self, bus: Optional[SdBus] = None) -> None:
        """
        :param SdBus bus: Use specific bus or session bus by default.
        """
        self._connect(
            SECRET_SERVICE_BUS_NAME,
            SECRET_SERVICE_PATH,
            bus)


class SecretCollection(SecretCollectionInterface):
    """Secrets collection.

    Implements :py:class:`SecretCollectionInterface`

    Bus name is predetermined at ``org.freedesktop.secrets``
    """

    def __init__(self,
                 collection_path: str,
                 bus: Optional[SdBus] = None) -> None:
        """
        :param str collection_path: Object path to collection.
        :param SdBus bus: Use specific bus or session bus by default.
        """
        self._connect(
            SECRET_SERVICE_BUS_NAME,
            collection_path,
            bus)


class SecretItem(SecretItemInterface):
    """Secrets item.

    Implements :py:class:`SecretItemInterface`

    Bus name is predetermined at ``org.freedesktop.secrets``
    """

    def __init__(self,
                 item_path: str,
                 bus: Optional[SdBus] = None) -> None:
        """
        :param str item_path: Object path to item.
        :param SdBus bus: Use specific bus or session bus by default.
        """
        self._connect(
            SECRET_SERVICE_BUS_NAME,
            item_path,
            bus)


class SecretPrompt(SecretPromptInterface):
    """Secrets prompt.

    Implements :py:class:`SecretPromptInterface`

    Bus name is predetermined at ``org.freedesktop.secrets``
    """

    def __init__(self,
                 prompt_path: str,
                 bus: Optional[SdBus] = None) -> None:
        """
        :param str prompt_path: Object path to prompt.
        :param SdBus bus: Use specific bus or session bus by default.
        """
        self._connect(
            SECRET_SERVICE_BUS_NAME,
            prompt_path,
            bus)


class SecretSession(SecretSessionInterface):
    """Secrets session.

    Implements :py:class:`SecretSessionInterface`

    Bus name is predetermined at ``org.freedesktop.secrets``
    """

    def __init__(self,
                 session_path: str,
                 bus: Optional[SdBus] = None) -> None:
        """
        :param str session_path: Object path to session.
        :param SdBus bus: Use specific bus or session bus by default.
        """
        self._connect(
            SECRET_SERVICE_BUS_NAME,
            session_path,
            bus)
