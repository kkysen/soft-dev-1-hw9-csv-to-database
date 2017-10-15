import os

from csv2db import Database

if __name__ == '__main__':
    with Database('test.db', debug=True) as db:
        db.add_csv('peeps.csv', types=('TEXT', 'INT', 'INT PRIMARY KEY'))

        dir_path = 'baseball/'
        for csv in os.listdir(dir_path):
            db.add_csv(dir_path + csv)