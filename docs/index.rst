******
Mopidy
******

Mopidy is an extensible music server written in Python.

Mopidy plays music from local disk, Spotify, SoundCloud, Google Play Music, and
more. You edit the playlist from any phone, tablet, or computer using a range
of MPD and web clients.

**Stream music from the cloud**

Vanilla Mopidy only plays music from your :ref:`local disk <ext-local>` and
:ref:`radio streams <ext-stream>`. Through :ref:`extensions <ext-backends>`,
Mopidy can play music from cloud services like Spotify, SoundCloud, and Google
Play Music. With Mopidy's extension support, backends for new music sources can
be easily added.

**Mopidy is just a server**

Mopidy is a Python application that runs in a terminal or in the background on
Linux computers or Macs that have network connectivity and audio output. Out of
the box, Mopidy is an :ref:`MPD <ext-mpd>` and :ref:`HTTP <ext-http>` server.
:ref:`Additional frontends <ext-frontends>` for controlling Mopidy can be
installed from extensions.

**Everybody use their favorite client**

You and the people around you can all connect their favorite :ref:`MPD
<mpd-clients>` or :ref:`web client <http-clients>` to the Mopidy server to
search for music and manage the playlist together. With a browser or MPD
client, which is available for all popular operating systems, you can control
the music from any phone, tablet, or computer.

**Mopidy on Raspberry Pi**

The :ref:`Raspberry Pi <raspberrypi-installation>` is a popular device to run
Mopidy on, either using Raspbian or Arch Linux. It is quite slow, but it is
very affordable. In fact, the Kickstarter funded Gramofon: Modern Cloud Jukebox
project used Mopidy on a Raspberry Pi to prototype the Gramofon device. Mopidy
is also a major building block in the Pi Musicbox integrated audio jukebox
system for Raspberry Pi.

**Mopidy is hackable**

Mopidy's extension support and :ref:`Python <api-ref>`, :ref:`JSON-RPC
<http-api>`, and :ref:`JavaScript APIs <mopidy-js>` makes Mopidy perfect for
building your own hacks. In one project, a Raspberry Pi was embedded in an old
cassette player. The buttons and volume control are wired up with GPIO on the
Raspberry Pi, and is used to control playback through a custom Mopidy
extension. The cassettes have NFC tags used to select playlists from Spotify.

**Getting started**

To get started with Mopidy, start by reading :ref:`installation`.

**Getting help**

If you get stuck, we usually hang around at ``#mopidy`` at `irc.freenode.net
<http://freenode.net/>`_ (with `searchable logs
<https://botbot.me/freenode/mopidy/>`_) and also have a `mailing list at Google
Groups <https://groups.google.com/forum/?fromgroups=#!forum/mopidy>`_. If you
stumble into a bug or got a feature request, please create an issue in the
`issue tracker <https://github.com/mopidy/mopidy/issues>`_. The `source code
<https://github.com/mopidy/mopidy>`_ may also be of help. If you want to stay
up to date on Mopidy developments, you can follow `@mopidy
<https://twitter.com/mopidy/>`_ on Twitter.


Usage
=====

.. toctree::
    :maxdepth: 2

    installation/index
    config
    running
    troubleshooting
    debian


.. _ext:

Extensions
==========

.. toctree::
    :maxdepth: 2

    ext/local
    ext/stream
    ext/http
    ext/mpd
    ext/softwaremixer
    ext/mixers
    ext/backends
    ext/frontends
    ext/web


Clients
=======

.. toctree::
    :maxdepth: 2

    clients/http
    clients/mpd
    clients/mpris
    clients/upnp


About
=====

.. toctree::
    :maxdepth: 1

    authors
    sponsors
    changelog
    versioning


Development
===========

.. toctree::
    :maxdepth: 1

    contributing
    devtools
    codestyle
    extensiondev


Reference
=========

.. toctree::
    :maxdepth: 2

    glossary
    command
    api/index
    modules/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
