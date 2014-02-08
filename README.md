irc
===

This is the code for a bot client service implemented in Python using standard libraries (so far).

Using it as-is is pretty standard, just go in and change server/nickname settings. However be careful because not all IRC networks are created equal, so the way I register and log in the bot may not work with everything yet.

I have tested it on a friend's server as well as freenode. Freenode currently isn't working properly. This is partly due to how I parse messages, but also how freenode formats them. I need to work on it more and hopefully get this settled.

Functions right now:

* @quote *username* "string" <-- the quotes will automatically be appended
* @rem *username* <-- this will perform a look-up on the dictionary. if a key matching the input username is found, then the value will be printed as *username* said "something here"
* @quit <-- this will end the service loop if you don't need the bot anymore.

The bot script now handles a persistive dictionary. So when the bot quits, it'll serialize its current dictionary to a JSON file. When the script starts, it'll deserialize and load the current dictionary JSON into memory.

The @quote function will save the desired user's quote into a dictionary. For example, if you type:
@quote joshwertheim I love to sleep in!

Then that quote will be saved into the dictionary and serialized to a JSON file as:
{"joshwertheim": "I\" love\" to\" sleep\" in!\""}

Also up for consideration is how I should handle the bot possibly being run for multiple channels or servers.
