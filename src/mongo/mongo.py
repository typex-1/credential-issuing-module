# coding: utf-8

import pymongo
from flask import json

class DBConnectionError(Exception):
    pass


class DB(object):

    def __init__(self, host_port='', user=None,pwd=None, database='',condition=''):
        connectUrl = "mongodb://"+user+":"+pwd+"@"+host_port+"/admin?"+condition
        try:
            self._conn = pymongo.MongoClient(connectUrl)
        except Exception:
            self._conn = None
            raise DBConnectionError('Host: {0} connection error: {1}'.format(host_port, ""))
        self._db = self._conn.get_database(database)
        #if user:
        #    if not self._db.authenticate(user, pwd):
        #        raise DBAuthenticatedError('Authentication failure')
        
    def get(self):
        return self._db

    def close(self):
        if self._conn:
            self._conn.close()

    def __del__(self):
        self.close()

if __name__ == '__main__':
    test = DB(host_port='', user='', pwd='', database='',condition='').get()
    #print test
    cursor = test.users.find({},{"_id":0})
    records = list(cursor)
    rjon = json.dumps(records)
    #print rjon
