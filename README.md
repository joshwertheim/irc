irc
===

This is the code for a bot client service implemented in Python using standard libraries (so far).

Using it as-is is pretty standard, just go in and change server/nickname settings. However be careful because not all IRC networks are created equal, so the way I register and log in the bot may not work with everything yet.

I have tested it on a friend's server as well as freenode. Freenode currently isn't working properly. This is partly due to how I parse messages, but also how freenode formats them. I need to work on it more and hopefully get this settled.

Functions right now:

* @quote *username* "string" <-- the quotes will automatically be appended
* @quit <-- this will end the service loop if you don't need the bot anymore.

The @quote function will save the desired user's quote into a dictionary. For example, if you type:
@quote joshwertheim I love to sleep in!

Then that quote will be saved into the dictionary and serialized to a JSON file as:
{"joshwertheim": "I\" love\" to\" sleep\" in!\""}

My next commit should provide functionality for importing the current JSON dictionary for continual use. Not sure if I should only allow one quote per a user or not. Also up for consideration is how I should handle the bot possibly being run for multiple channels or servers.

I also want to implement a function for searching for a given user's stored quote (if one exists). This will likely look like: @rem *username* and will perform a look-up using the dictionary.
