import os


class Config:

    SECRET_KEY = os.urandom(12)

    #DB_USER = os.environ.get('DB_USER')
    #DB_PASS = os.environ.get('DB_PASS')
    DB_USER = 'admin'
    DB_PASS = 'rE)9z4v6(RHNP)ii4N*vU'

    # Connection to Postgres server
    SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASS + '@192.155.88.112:3306/courtfinder'
