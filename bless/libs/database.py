import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from bless.libs import utils

def check_db(qry, db, db_name):
    db.execute(qry)
    data_set = list()
    for row in db.fetchall():
        if row[0] == db_name:
            return True
        else:
            return False

def database_setting(config):
    conn = psycopg2.connect(
        user=config['username'],
        sslmode=config['ssl'],
        port=config['port'],
        host=config['host']
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    db = conn.cursor()
    if check_db('SHOW DATABASES', db, config['name']):
        conn = psycopg2.connect(
            database=config['name'],
            user=config['username'],
            sslmode=config['ssl'],
            port=config['port'],
            host=config['host']
        )
    else:
        try:
            db.execute("CREATE DATABASE "+config['name'])
        except (Exception, psycopg2.DatabaseError) as e:
            raise e
        conn = psycopg2.connect(
            database=config['name'],
            user=config['username'],
            sslmode=config['ssl'],
            port=config['port'],
            host=config['host']
        )
    db = conn.cursor()
    conn.set_session(autocommit=True)
    return db

def database_parse(config, obj_database):
    db = database_setting(config)
    data_finish = list()
    for tables in obj_database['tables']:
        config_table = list()
        for column in obj_database['tables'][tables]:            
            data_f = {
                "column": column,
                "rules": obj_database['tables'][tables][column]
            }
            config_table.append(data_f)
        create_table(tables, config_table)

def create_table(tables, config_table):
    print("TABLE : ", tables)
    print("config : ", config_table)

