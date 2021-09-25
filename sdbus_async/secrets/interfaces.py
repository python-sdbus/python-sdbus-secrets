
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

from typing import Any, Dict, List, Tuple

from sdbus import (
    DbusInterfaceCommonAsync,
    dbus_method_async,
    dbus_property_async,
    dbus_signal_async,
)


class SecretServiceInterface(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.Secret.Service',
):
    """Secrets daemon interface.

    Used to create new sessions and etc...
    """

    @dbus_method_async(
        input_signature='sv',
        result_signature='vo',
    )
    async def open_session(
        self,
        algorithm: str,
        input: Tuple[str, Any],
    ) -> Tuple[Tuple[str, Any], str]:
        """Create new session.

        :param str algorithm: Session algorithm.
            The ``plain`` algorithm type with no encryption
            is always supported.
        :param Tuple[str,Any] input: Input arguments for the algorithm.
        :returns: Tuple of output of the algorithm negotiation
            and object path of the new session.
        :rtype: Tuple[Tuple[str,Any],str]
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='a{sv}s',
        result_signature='oo',
    )
    async def create_collection(
        self,
        properties: Dict[str, Tuple[str, Any]],
        alias: str,
    ) -> Tuple[str, str]:
        """Create a new collection with the specified properties.

        If new collection object path is ``/`` promting is necessary.

        If the returned prompt object path is ``/`` no prompt is needed.

        :param Dict[str,Tuple[str,Any]] properties: Dict of variants
            with properties of the new collection.
        :param str alias: Set this to an empty string if the new collection
            should not be associated with a well known alias.
            (such as ``default``)
        :returns: Tuple of object path of new collection and possible
            object path of prompt object.
        :rtype: Tuple[str,str]
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='a{ss}',
        result_signature='aoao',
    )
    async def search_items(
        self,
        attributes: Dict[str, str],
    ) -> Tuple[List[str], List[str]]:
        """Find items in any collection.

        :param Dict[str,str] attributes: Attributes that should match.
        :returns: Two arrays of matched object paths.
            First arrays contains unlocked items and second locked ones.
        :rtype: Tuple[List[str],List[str]]
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ao',
        result_signature='aoo',
    )
    async def unlock(
        self,
        objects: List[str],
    ) -> Tuple[List[str], str]:
        """Unlock the specified objects.

        :param List[str] objects: List of object paths to unlock
        :returns: List of objects unlocked without prompt and
            a path to prompt object. (has a value of ``/``
            if no prompt needed)
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ao',
        result_signature='aoo',
    )
    async def lock(
        self,
        objects: List[str],
    ) -> Tuple[List[str], str]:
        """Lock items.

        :param List[str] objects: List of object paths to lock
        :returns: List of objects locked without prompt and
            a path to prompt object. (has a value of ``/``
            if no prompt needed)
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='aoo',
        result_signature='a{o(oayays)}',
    )
    async def get_secrets(
        self,
        items: List[str],
        session: str,
    ) -> Dict[str, Tuple[str, bytes, bytes, str]]:
        """Retrieve multiple secrets from different items.

        :param List[str] items: List of object paths to items.
        :param str session: Object path of current session.
        :returns: Dictionary with keys as requested object paths
            and values as secret items data.
        :rtype: Dict[str,Tuple[str,bytes,bytes,str]]
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def read_alias(
        self,
        name: str,
    ) -> str:
        """Get the collection with the given alias.

        :param str name: An alias, such as ``default``.
        :retuns: Object path to collection or ``/`` if no such
            alias exists.
        :rtype: str
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='so',
    )
    async def set_alias(
        self,
        name: str,
        collection: str,
    ) -> None:
        """Setup a collection alias.

        :param str name: The alias to use.
        :param str collection: Object path to collection to
            apply alias to.
        """
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ao',
    )
    def collections(self) -> List[str]:
        """Object paths of all collections."""
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='o',
    )
    def collection_created(self) -> str:
        """Signal when collection has been created.

        Signal data is an object path to new collection.
        """
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='o',
    )
    def collection_deleted(self) -> str:
        """Signal when collection was deleted.

        Signal data is an object path of removed collection.
        """
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='o',
    )
    def collection_changed(self) -> str:
        """Signal when a collection was modified.

        Signal data is the modified collection object path.
        """
        raise NotImplementedError


class SecretCollectionInterface(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.Secret.Collection',
):
    """Collection of items containing secrets."""

    @dbus_method_async(
        result_signature='o',
    )
    async def delete(
        self,
    ) -> str:
        """Delete this collection.

        :returns: Object path of the prompt or ``/`` if no
            prompt is needed.
        :rtype: str
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='a{ss}',
        result_signature='ao',
    )
    async def search_items(
        self,
        attributes: Dict[str, str],
    ) -> List[str]:
        """Search for items in this collection.

        :param Dict[str,str] attributes: Attributes that should match.
        :returns: List of matched items object paths.
        :rtype: List[str]
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='a{sv}(oayays)b',
        result_signature='oo',
    )
    async def create_item(
        self,
        properties: Dict[str, Tuple[str, Any]],
        secret: Tuple[str, bytes, bytes, str],
        replace: bool,
    ) -> Tuple[str, str]:
        """Create new item.

        :param Dict[str,Tuple[str,Any]] properties: Set properties of the new
            item. The keys are names of properties with prefixed with
            ``org.freedesktop.Secret.Item.``. For example, ``label`` property
            will have a ``org.freedesktop.Secret.Item.Label`` key.
        :param Tuple[str,bytes,bytes,str] secret: Secret data.
            Secret data contains tuple of session path,
            encryption parameters bytes (empty in case of plain mode),
            secret value bytes and content type string.
        :param bool replace: Replace existing item with same attributes.
        :returns: Object path of new item or ``/`` if prompt needed and
            object path of prompt or ``/`` if prompt is not needed.
        :rtype: Tuple[str,str]
        """
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ao',
    )
    def items(self) -> List[str]:
        """List of object paths of items in this colletion."""
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def label(self) -> str:
        """Display name of this collection."""
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def locked(self) -> bool:
        """Whether the collection is locked or not."""
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def created(self) -> int:
        """Unix time of creation."""
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def modified(self) -> int:
        """Unix time of last modified."""
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='o',
    )
    def item_created(self) -> str:
        """Signal when new item was created.

        Signal data is object path of new item.
        """
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='o',
    )
    def item_deleted(self) -> str:
        """Signal when item was deleted.

        Signal data is object path of deleted item.
        """
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='o',
    )
    def item_changed(self) -> str:
        """Signal when an item was changed.

        Signal data is object path of changed item.
        """
        raise NotImplementedError


class SecretItemInterface(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.Secret.Item',
):
    """Item containing a secret."""

    @dbus_method_async(
        result_signature='o',
    )
    async def delete(
        self,
    ) -> str:
        """Delete this item.

        :returns: Path to prompt or ``/`` if no prompt necessary.
        :rtype: str
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
        result_signature='(oayays)',
    )
    async def get_secret(
        self,
        session: str,
    ) -> Tuple[str, bytes, bytes, str]:
        """Get secret of this item.

        :returns: Secret data.
            Secret data contains tuple of session path,
            encryption parameters bytes (empty in case of plain mode),
            secret value bytes and content type string.
        :rtype: Tuple[str,bytes,bytes,str]
        """
        raise NotImplementedError

    @dbus_method_async(
        input_signature='(oayays)',
    )
    async def set_secret(
        self,
        secret: Tuple[str, bytes, bytes, str],
    ) -> None:
        """Set the secret for this item.

        :param Tuple[str,bytes,bytes,str] secret: Secret data.
            Secret data contains tuple of session path,
            encryption parameters bytes (empty in case of plain mode),
            secret value bytes and content type string.
        """
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def locked(self) -> bool:
        """Is secret locked?"""
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a{ss}',
    )
    def attributes(self) -> Dict[str, str]:
        """Item attributes."""
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def label(self) -> str:
        """Item display name."""
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def created(self) -> int:
        """Unix time of creation."""
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def modified(self) -> int:
        """Unix time of last modified."""
        raise NotImplementedError


class SecretSessionInterface(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.Secret.Session',
):
    """Session state between client and service."""

    @dbus_method_async(
    )
    async def close(
        self,
    ) -> None:
        """Close this session."""
        raise NotImplementedError


class SecretPromptInterface(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.Secret.Prompt',
):
    """Prompt necessary to complete and operation."""

    @dbus_method_async(
        input_signature='s',
    )
    async def prompt(
        self,
        window_id: str,
    ) -> None:
        """Preform a prompt.

        :param str window_id: Platform specific window handle to use
            for showing the prompt.
        """
        raise NotImplementedError

    @dbus_method_async(
    )
    async def dismiss(
        self,
    ) -> None:
        """Dismiss the prompts."""
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='bv',
    )
    def completed(self) -> Tuple[bool, Tuple[str, Any]]:
        """Signal when prompt is completed.

        Signal data is:

        * Boolean whether the prompt was dismissed or not.
        * Possibly empty, operation specific result.
        """
        raise NotImplementedError
