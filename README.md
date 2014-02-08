irc
===

This is the code for a bot client service implemented in Python using standard libraries (so far).

Using it as-is is pretty standard, just go in and change server/nickname settings. However be careful because not all IRC networks are created equal, so the way I register and log in the bot may not work with everything yet.

I have tested it on a friend's server as well as freenode. Freenode should work okay, but it may not. I need to work on it more just in case there are problems during the process.

Functions right now:

* @quote *username* "string" <-- the quotes will automatically be appended
* @quit <-- this will end the service loop if you don't need the bot anymore.
