initial lines


pip install flask

pip install pytest

___________________
run hot reload server

./bin/server-debug.sh

Test
----

::

    $ pip install '.[test]'
    $ pytest

Run with coverage report::

    $ coverage run -m pytest
    $ coverage report
    $ coverage html  # open htmlcov/index.html in a browser