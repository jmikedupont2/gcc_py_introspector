=========
 gcc.tree
=========

SYNOPSIS
========

.. code::

    gcc.tree [options] [<path> <path> ...]

    gcc.tree --help

DESCRIPTION
===========

``gcc.tree`` is a command-line utility for reverse engineering c code and implementing compiler plugins in other languages.
By default it includes plugins written by the author. It will also
run third-party extensions if they are found and installed.

OPTIONS
=======

It is important to note that third-party extensions may add options which are
not represented here. To see all options available in your installation, run::

    gcc.tree --help

All options available as of gcc.tree 3.1.0::

    --version             show program's version number and exit
    -h, --help            show this help message and exit
    -v, --verbose         Print more information about what is happening in
                          gcc.tree. This option is repeatable and will increase
                          verbosity each time it is repeated.
    -q, --quiet           Report only file names, or nothing. This option is
                          repeatable.
    --filename=patterns   Only check for filenames matching the patterns in this
                          comma-separated list. (Default: *.c)
    --stdin-display-name=STDIN_DISPLAY_NAME
                          The name used when reporting errors from code passed
                          via stdin. This is useful for editors piping the file
                          contents to gcc.tree. (Default: stdin)
    --statistics          Count errors and warnings.
    --enable-extensions=ENABLE_EXTENSIONS
                          Enable plugins and extensions that are otherwise
                          disabled by default
    --exit-zero           Exit with status code "0" even if there are errors.
    --install-hook=INSTALL_HOOK
                          Install a hook that is run prior to a commit for the
                          supported version control system.
    -j JOBS, --jobs=JOBS  Number of subprocesses to use to run checks in
                          parallel. This is ignored on Windows. The default,
                          "auto", will auto-detect the number of processors
                          available to use. (Default: auto)
    --output-file=OUTPUT_FILE
                          Redirect report to a file.
    --tee                 Write to stdout and output-file.
    --append-config=APPEND_CONFIG
                          Provide extra config files to parse in addition to the
                          files found by gcc.tree by default. These files are the
                          last ones read and so they take the highest precedence
                          when multiple files provide the same option.
    --config=CONFIG       Path to the config file that will be the authoritative
                          config source. This will cause gcc.tree to ignore all
                          other configuration files.
    --isolated            Ignore all configuration files.
    --benchmark           Print benchmark information about this run of gcc.tree
    --bug-report          Print information necessary when preparing a bug
                          report

EXAMPLES
========

Simply running gcc.tree against the current directory::

    gcc.tree .

Running gcc.tree against a specific path::

    gcc.tree path/to/file.tu

Generate information for a bug report::

    gcc.tree --bug-report

SEE ALSO
========

gcc.tree documentation: https://jmikedupont2.github.io/gcc_py_introspector/


BUGS
====

Please report all bugs to https://github.com/jmikedupont2/gcc_py_introspector
