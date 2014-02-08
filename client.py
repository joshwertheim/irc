import sys
import socket
import string
import json

class IRCClient(object):
    """Creates an IRCClient instance with basic server config and functions"""

    SERVER = ""
    sock = ""
    INIT_CHANNEL = "#hellcat"

    def __init__(self):
        self.sock = socket.socket()

    def connect(self, server):
        self.SERVER = server
        self.sock.connect((self.SERVER, 6667))

class User(object):
    """Creates a User instance with basic user config and functions"""

    NICK = ""
    IDENT = ""
    REALNAME = ""
    PASS = ""

    def __init__(self, client, nickname, identity, fullname, password):
        self.NICK = nickname
        self.IDENT = identity
        self.REALNAME = fullname
        self.PASS = password

    def identify(self):
        client.sock.send("NICK %s\r\n" % self.NICK)
        client.sock.send("USER %s %s bla :%s\r\n" % (self.IDENT, client.SERVER, self.REALNAME))
        client.sock.send("PASS %s\r\n" % self.PASS)
        client.sock.send("JOIN %s\r\n" % client.INIT_CHANNEL)

    def joinInitialChans(self):
        client.sock.send("JOIN %s\r\n" % client.INIT_CHANNEL)


print "Enter your nickname:"
nickname = "spikebot" # raw_input()
print "Enter your identity:"
identity = "spikebot" # raw_input()
print "Enter your real name:"
fullname = "spikesbot" # raw_input()
print "Enter your password:"
password = raw_input() # some password 

client = IRCClient()
user = User(client, nickname, identity, fullname, password)
client.connect("irc.hellcat.net")
user.identify()

active = 1
readbuffer = ""

jsonData = open('quoteDatabase.json', 'rb')
quoteDatabase = json.load(jsonData)
jsonData.close()

while active:
    readbuffer = readbuffer + client.sock.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:

        if "Password accepted" in line:
            print "joining"
            user.joinInitialChans()
            message = "Hello, world. :O"
            client.sock.send("PRIVMSG #hellcat " + message + "\r\n")


        line = string.rstrip(line)
        line = string.split(line)

        print line

        if ":@quote" in line:
            quote = "\"" + " ".join(line[5:len(line)]) + "\""
            quoteDatabase[line[4]] = quote
            client.sock.send("PRIVMSG " + client.INIT_CHANNEL + " " + "This quote is now saved permanently to \"The Web.\"" + "\r\n")

        if ":@rem" in line and line[4] in quoteDatabase:
            client.sock.send("PRIVMSG " + client.INIT_CHANNEL + " " + line[4] + " said " + quoteDatabase[line[4]] + "\r\n")

        if(line[0] == "PING"):
            print(line)
            client.sock.send("PONG %s\r\n" % line[1])
            print("PONG %s\r\n" % line[1])

        if ":@quit" in line:
            active = 0

with open('quoteDatabase.json', 'wb') as export:
    json.dump(quoteDatabase, export)