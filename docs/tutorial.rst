Freedesktop Secrets Tutorial
============================

This tutorial will guide you through the basic steps
on how to use Freedesktop Secrets API using the python-sdbus
binds.

.. note::
    This tutorial will use blocking API for simplicity.
    Async API can be easily used instead.

Creating a new session
----------------------

To interact with the secrets API a process needs to acquire
a new session.

Secrets API supports an in-transit encryption but its not required.
Most of secrets implementations should support plain mode without
encryption. This is the simplest way to use secrets API.

.. code-block:: python

    secrets_service = SecretService()

    session_algorithm = 'plain'  # Plain mode, no encryption
    session_input = ('s', '')  # Variant of an empty string

    # With plain algorithm we only need session path
    # output of algorithm negotiation can be ignored (assigned to _)
    _, my_session_path = secrets_service.open_session(
        session_algorithm,
        session_input,
    )

Session is identified by an object path. In this case the session path is
stored in the ``my_session_path`` variable.

Session can be closed manually using :py:meth:`SecretSessionInterface.close`
method or automatically when process that acquired session disconnects from the
bus.

Acquiring default collection
----------------------------

Unless you need to store multiple secrets it is better to find a default collection.

This collection should always be present.

.. code-block:: python

    default_collection_path = secrets_service.read_alias('default')

    default_collection = SecretCollection(default_collection_path)

Creating secrets
----------------

:py:meth:`SecretCollectionInterface.create_item` should be used to create new items.

The secret can be created with properties to uniquely identify it. Each property
name must be prefixed with ``org.freedesktop.Secret.Item.`` string. For example,
secret attributes would be ``org.freedesktop.Secret.Item.Attributes``. See example.

The secret data itself is a tuple of session path, encryption parameters bytes
(empty in case of plain mode), bytes of value and content type string. (for example,
``text/plain; charset=utf8``)

Last argument is a boolean whether or not to replace existing secret with same
attributes.

.. code-block:: python

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

Searching secrets
-----------------

After getting a collection you can either search the items using
:py:meth:`SecretCollectionInterface.search_items` or iterate over
:py:meth:`SecretCollectionInterface.items` property and examine
each secret individually.

Each secret has a dictionary of attributes which can be used to uniquely identify
a secret.

.. code-block:: python

    found_secrets_paths = default_collection.search_items(
        {
            "Attribute1": "Value1",
            "Attribute2": "Value2",
        }
    )

Getting secrets
---------------

After finding the secret path in order to get the secret you should
use the :py:meth:`SecretItemInterface.get_secret` method to get secret data.

Secret data contains tuple of session path, encryption parameters bytes
(empty in case of plain mode), secret value bytes and content type string.

.. code-block:: python

    secret = SecretItem(new_secret_path)

    session_path, params, value, content_type = secret.get_secret(my_session_path)

.. note::
    See `secrets specification <https://specifications.freedesktop.org/secret-service/latest/index.html>`_
    for more in depth look.
