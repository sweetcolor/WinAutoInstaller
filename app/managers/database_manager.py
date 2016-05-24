import psycopg2
import os
import string
import itertools


class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.cursor = None
        self.connection = None
        self.prepare_database()

    def prepare_database(self):
        self.connect()
        self.migrate()

    def connect(self):
        self.connection = psycopg2.connect(database=self.database_name, user='postgres', password='1')
        self.cursor = self.connection.cursor()

    def _connect_to_migration_db(self):
        self.migration_connection = psycopg2.connect(database='migration', user='postgres', password='1')
        self.migration_cursor = self.migration_connection.cursor()

    def migrate(self):
        self._connect_to_migration_db()
        self.migration_cursor.execute('SELECT name FROM migration."public".migration_winautoinstaller')
        migrated_file = set(itertools.chain(*self.migration_cursor.fetchall()))
        curr_dir = os.getcwd()
        os.chdir('db')
        for migration_file in sorted(os.listdir('.')):
            if migration_file not in migrated_file:
                self.execute_sql_file(migration_file)
                self.migration_cursor.execute(
                    'INSERT INTO migration_winautoinstaller (name) VALUES (%s)', (migration_file,)
                )
        self.migration_connection.commit()
        os.chdir(curr_dir)

    def execute_sql_file(self, file_sql):
        file_sql = filter(lambda x: x not in string.whitespace, open(file_sql).read().split(';'))
        for line in file_sql:
            self.cursor.execute(line)
        self.connection.commit()

    def get_hosts_list(self):
        self.cursor.execute('SELECT ip FROM hosts')
        return self.cursor.fetchall()

    def update_hosts_list(self, hosts_list):
        self.cursor.execute('DELETE FROM hosts')
        self.cursor.executemany('INSERT INTO hosts (hostname, ip) VALUES (%s, %s)', [host[:2] for host in hosts_list])
        self.connection.commit()

    def get_installers(self, where=list()):
        if where:
            self.cursor.execute('SELECT program, path_to_script, arguments FROM scripts WHERE program IN %s', (tuple(where),))
        else:
            self.cursor.execute('SELECT program, path_to_script, arguments FROM scripts')
        return self.cursor.fetchall()

    def get_scripts(self):
        self.cursor.execute('SELECT program FROM scripts')
        return self.cursor.fetchall()

    def insert_scripts(self, scripts_list):
        self.cursor.execute('DELETE FROM scripts')
        self.cursor.executemany('INSERT INTO scripts (program, path_to_script, arguments) VALUES (%s, %s, %s)',
                                scripts_list)
        self.connection.commit()

    def create(self):
        # TODO create db, didn't work login user
        # not work
        # psycopg2.connect(database='test1', user='postgres', password='1')
        # not work
        # from subprocess import PIPE, Popen, STDOUT
        # s = Popen('python add.py', shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        # r = s.communicate(input=b'1\n')
        # print(r[0].decode())
        pass
