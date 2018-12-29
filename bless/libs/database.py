import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from bless.libs import utils

def check_db(qry, db, db_name):
    db.execute(qry)
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
    # data_finish = list()
    for tables in obj_database['tables']:
        config_table = list()
        for column in obj_database['tables'][tables]:
            data_f = {
                "column": column,
                "rules": obj_database['tables'][tables][column]
            }
            config_table.append(data_f)
        query = create_table(tables, config_table)
        execute_query(query,db)


def create_table(tables, config_table):
    query = "CREATE TABLE "+tables
    str_config = ""
    pkey_config = ""
    unique_config= ""
    family_config = ""
    foreign_config = ""

    for k_column in config_table:
        check_foreign = None
        not_null = ""
        default = ""
        pmr_key = ""
        type_data = ""
        try:
            if k_column['rules']['notNull']:
                not_null="NOT NULL"
            else:
                not_null = "NULL"
        except Exception:
            pass

        if k_column['rules']['type']=='serial':
            default = "DEFAULT unique_rowid()"
            type_data = "int"
        else:
            type_data = k_column['rules']['type']
        try:
            if k_column['rules']['primaryKey']:
                pmr_key ="CONSTRAINT "+tables+"_pk PRIMARY KEY ("+k_column['column']+" ASC)"
            else:
                pmr_key = ""
        except Exception:
            pass

        try:
            if k_column['rules']['unique']:
                unique_config +="UNIQUE INDEX "+tables+"_un ("+k_column['column']+" ASC),\n"
            else:
                unique_config = ""
        except Exception:
            pass
        
        try:
            check_foreign = k_column['rules']['foreignKey']
        except Exception:
            check_foreign

        if check_foreign:
            foreign_config += "CONSTRAINT "+tables+"_"+k_column['rules']['foreignKey']['reference']+"_fk FOREIGN KEY ("+k_column['rules']['foreignKey']['field']+") REFERENCES "+k_column['rules']['foreignKey']['reference']+" ("+k_column['rules']['foreignKey']['field']+") ON DELETE "+k_column['rules']['foreignKey']['on_delete']+" ON UPDATE "+k_column['rules']['foreignKey']['on_update']+",\n"


        str_config += k_column['column']+" "+type_data+" "+not_null+" "+default+",\n"
        pkey_config += pmr_key
        family_config += k_column['column']+","
    family_config = "FAMILY \"primary\" ("+family_config[:-1]+")"
    query_fix = query+" (\n"+str_config+"\n"+pkey_config+",\n"+foreign_config+unique_config+"\n"+family_config+")"
    return query_fix


def execute_query(query, db):
    try:
        db.execute(query)
        return db
    except (Exception, psycopg2.DatabaseError) as e:
        raise e