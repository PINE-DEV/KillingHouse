from storm.locals import *

def init():
    # database = create_database("scheme://username:password@hostname:port/database_name")
    SCHEME = 'sqlite'
    USER = 'user'
    PASS = 'pass'
HOST = 'localhost'
PORT = '??'
DB_NAME = 'killerhouse'
database = create_database("{0}://{1}:{2}@{3}:{4}/{5}".format(SCHEME, USER, PASS, HOST, PORT, DB_NAME))

class DBObject():
    pass

class User(DBObject):
    __storm_table__ = 'user'

    name = '' # Name it is playing with
    games = [] # List of groups
    targets = {} # List of targets (one or none per group)

    def getTarget(groupId):
        # ONE TARGET
        # NO TARGET (IF USER IS DEAD)
        # EXCEPTION (IF USER NOT IN GAME)
        pass

class Game(DBObject):
    users = [] # List of users
    def getUsers():
        pass

class Target(DBObject):
    user = '' # ID (tg name?) of target user
    weapon = '' # Weapon to use
    location = '' # Location to use
