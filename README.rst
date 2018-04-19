makegitignore.py
----------------


It's a really simple script to generate a default ``.gitignore`` file

GPL 3.0 or later.

Installation and running
========================

I've "installed" it on Linux in a directory ``~/scripts`` by running

::

$ ln makegitignore.py ~/scripts

from with the repository directory.

You also need to ensure that ``makegitignore.py`` is executable:

::

$ chmod u+x ~/scripts/makegitignore.py

Then, you can run it by:

::

$ python3 ~/scripts/makegitignore.py

If python3 is your default python, ``python ~/scripts/makegitignore.py``
would be the better way to spell this.

If you include the scripts directory in your path, say by including the
line

::

 export PATH="$HOME/scripts:$PATH"

in your ``~/.bashrc`` you can then run the script simply by running

::

$  makegitignore.py

Run it as

::

$  makegitignore.py -h

to get a brief help message explaining the command line arguments.
