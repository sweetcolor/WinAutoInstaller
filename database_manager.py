import psycopg2
import os


class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name

    def connect(self):
        psycopg2.connect(database=self.database_name, user='postgres', password='1')

    def create(self):
        #TODO create db, didn't work login user
        #not work
        #psycopg2.connect(database='test1', user='postgres', password='1')
        #not work
        # from subprocess import PIPE, Popen, STDOUT
        # s = Popen('python add.py', shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        # r = s.communicate(input=b'1\n')
        # print(r[0].decode())
        pass
