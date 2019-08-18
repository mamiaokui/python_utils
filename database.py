import sqlite3
import base64
import numpy as np


class EmbdingDatabase:

    __connection = None
    __cursor = None
    __database_name = None

    def __init__(self, dbname="test.db"):
        self.__database_name = dbname

    def open(self,  drop_exist=False):
        self.__connection = sqlite3.connect(self.__database_name)
        self.__cursor = self.__connection.cursor()

        if drop_exist:
            self.clean()

        self.__cursor.execute('''CREATE TABLE  if not exists people
                             (id integer PRIMARY KEY AUTOINCREMENT, name text, embd)''')
        self.__connection.commit()

    def insert(self, name, embd):
        name = base64.b64encode(name.encode())
        name = name.decode()
        embd = embd.tostring()
        embd = base64.b64encode(embd)
        embd = embd.decode()
        #name = name.encode("utf-8").encode("base64")
        #embd = embd.encode("utf-8").encode("base64")
        command = "insert into people values(null, '%s', '%s')" % (name, embd)
        self.__cursor.execute(command)
        self.__connection.commit()

    def get_embd(self):
        self.__cursor.execute("select * from people")
        ret = self.__cursor.fetchall()
        arr = []
        for i in ret:
            name = base64.b64decode(str(i[1]))
            embd = base64.b64decode(str(i[2]))
            embd = np.fromstring(embd)
            arr.append([name, embd])

        return arr

    def release(self):
        self.__connection.commit()
        self.__connection.close()

    def clean(self):
        self.__cursor.execute("drop table if exists people")
        self.__connection.commit()


if __name__ == "__main__":
    a = EmbdingDatabase()
    a.insert("name1", "embd1")
    a.insert("name2", "embd2")
    a.insert("name3", "embd3")
    a.insert("name4", "embd4")
    a.get_embd()

