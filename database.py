import sqlite3
import base64


class EmbdedDatabase:

    __connection = None
    __cursor = None

    def __init__(self):
        pass


    def open(self,  drop_exist):
        self.__connection = sqlite3.connect("test.db")
        self.__cursor = self.__connection.cursor()
        # self.__cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{%s}'" %("people"))

        if drop_exist:
            self.clean()

        self.__cursor.execute('''CREATE TABLE  if not exists people
                             (id integer PRIMARY KEY AUTOINCREMENT, name text, embd)''')
        self.__connection.commit()

    def insert(self, name, embd):
        name = name.encode("utf-8").encode("base64")
        embd = embd.encode("utf-8").encode("base64")

        self.__cursor.execute("insert into people values(null, '%s', '%s')" % (name, embd))
        self.__connection.commit()

    def get_embd(self):
        self.__cursor.execute("select * from people")
        ret = self.__cursor.fetchall()
        arr = []
        for i in ret:
            name = str(i[1]).decode("base64")
            embd = str(i[2]).decode("base64")
            arr.append([name, embd])

        return arr

    def release(self):
        self.__connection.commit()
        self.__connection.close()

    def clean(self):
        self.__cursor.execute("drop table if exists people")
        self.__connection.commit()


if __name__ == "__main__":
    a = EmbdedDatabase()
    a.insert("name1", "embd1")
    a.insert("name2", "embd2")
    a.insert("name3", "embd3")
    a.insert("name4", "embd4")
    a.get_embd()

