import psycopg2


class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.cursor = None
        self.connection = None
        self.prepare_database()

    def prepare_database(self):
        self.connect()
        self.create_tables()

    def connect(self):
        self.connection = psycopg2.connect(database=self.database_name, user='postgres', password='1')
        self.cursor = self.connection.cursor()

    def create_tables(self):
        file_sql = filter(bool, open('db/create_db.sql').read().split(';'))
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
