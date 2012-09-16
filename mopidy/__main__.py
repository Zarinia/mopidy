import logging
import optparse
import os
import signal
import sys

import gobject
gobject.threads_init()


# Extract any non-GStreamer arguments, and leave the GStreamer arguments for
# processing by GStreamer. This needs to be done before GStreamer is imported,
# so that GStreamer doesn't hijack e.g. ``--help``.
# NOTE This naive fix does not support values like ``bar`` in
# ``--gst-foo bar``. Use equals to pass values, like ``--gst-foo=bar``.

def is_gst_arg(argument):
    return argument.startswith('--gst') or argument == '--help-gst'

gstreamer_args = [arg for arg in sys.argv[1:] if is_gst_arg(arg)]
mopidy_args = [arg for arg in sys.argv[1:] if not is_gst_arg(arg)]
sys.argv[1:] = gstreamer_args


# Add ../ to the path so we can run Mopidy from a Git checkout without
# installing it on the system.
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


from mopidy import (get_version, settings, OptionalDependencyError,
    SettingsError, DATA_PATH, SETTINGS_PATH, SETTINGS_FILE)
from mopidy.audio import Audio
from mopidy.utils import get_class
from mopidy.utils.deps import list_deps_optparse_callback
from mopidy.utils.log import setup_logging
from mopidy.utils.path import get_or_create_folder, get_or_create_file
from mopidy.utils.process import (exit_handler, stop_remaining_actors,
    stop_actors_by_class, DebugThread)
from mopidy.utils.settings import list_settings_optparse_callback


logger = logging.getLogger('mopidy.main')


def main():
    debug_thread = DebugThread()
    debug_thread.start()

    signal.signal(signal.SIGUSR1, debug_thread.handler)
    signal.signal(signal.SIGTERM, exit_handler)

    loop = gobject.MainLoop()
    try:
        options = parse_options()
        setup_logging(options.verbosity_level, options.save_debug_log)
        check_old_folders()
        setup_settings(options.interactive)
        setup_audio()
        setup_backend()
        setup_frontends()
        loop.run()
    except SettingsError as e:
        logger.error(e.message)
    except KeyboardInterrupt:
        logger.info(u'Interrupted. Exiting...')
    except Exception as e:
        logger.exception(e)
    finally:
        loop.quit()
        stop_frontends()
        stop_backend()
        stop_audio()
        stop_remaining_actors()


def parse_options():
    parser = optparse.OptionParser(version=u'Mopidy %s' % get_version())
    parser.add_option('--help-gst',
        action='store_true', dest='help_gst',
        help='show GStreamer help options')
    parser.add_option('-i', '--interactive',
        action='store_true', dest='interactive',
        help='ask interactively for required settings which are missing')
    parser.add_option('-q', '--quiet',
        action='store_const', const=0, dest='verbosity_level',
        help='less output (warning level)')
    parser.add_option('-v', '--verbose',
        action='count', default=1, dest='verbosity_level',
        help='more output (debug level)')
    parser.add_option('--save-debug-log',
        action='store_true', dest='save_debug_log',
        help='save debug log to "./mopidy.log"')
    parser.add_option('--list-settings',
        action='callback', callback=list_settings_optparse_callback,
        help='list current settings')
    parser.add_option('--list-deps',
        action='callback', callback=list_deps_optparse_callback,
        help='list dependencies and their versions')
    return parser.parse_args(args=mopidy_args)[0]


def check_old_folders():
    old_settings_folder = os.path.expanduser(u'~/.mopidy')

    if not os.path.isdir(old_settings_folder):
        return

    logger.warning(u'Old settings folder found at %s, settings.py should be '
        'moved to %s, any cache data should be deleted. See release notes '
        'for further instructions.', old_settings_folder, SETTINGS_PATH)


def setup_settings(interactive):
    get_or_create_folder(SETTINGS_PATH)
    get_or_create_folder(DATA_PATH)
    get_or_create_file(SETTINGS_FILE)
    try:
        settings.validate(interactive)
    except SettingsError, e:
        logger.error(e.message)
        sys.exit(1)


def setup_audio():
    Audio.start()


def stop_audio():
    stop_actors_by_class(Audio)

def setup_backend():
    get_class(settings.BACKENDS[0]).start()


def stop_backend():
    stop_actors_by_class(get_class(settings.BACKENDS[0]))


def setup_frontends():
    for frontend_class_name in settings.FRONTENDS:
        try:
            get_class(frontend_class_name).start()
        except OptionalDependencyError as e:
            logger.info(u'Disabled: %s (%s)', frontend_class_name, e)


def stop_frontends():
    for frontend_class_name in settings.FRONTENDS:
        try:
            stop_actors_by_class(get_class(frontend_class_name))
        except OptionalDependencyError:
            pass


if __name__ == '__main__':
    main()
