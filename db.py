import click
import os
import sqlite3
from flask import current_app, g #check doc if you wanna 

def get_db_con(pragma_foreign_keys = True):#connects to the database engine
    if 'db_con' not in g:
        g.db_con = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db_con.row_factory = sqlite3.Row
        if pragma_foreign_keys:# tells SQLite to enforce foreign key constraints, which by default is turned off
            g.db_con.execute('PRAGMA foreign_keys = ON;')
    return g.db_con

def close_db_con(e=None):#close the database connection
    db_con = g.pop('db_con', None)
    if db_con is not None:
        db_con.close()

@click.command('init-db')
def init_db():  #database has to be initiated once, not everytime the app is started
    try:
        os.makedirs(current_app.instance_path)          #creates a folder at location current_app.instance.path (instanz)
    except OSError:
        pass
    db_con = get_db_con()
    with current_app.open_resource('sql/drop_tables.sql') as f: #executes sql statement from drop_tables.sql to create an empty database
        db_con.executescript(f.read().decode('utf8'))
    with current_app.open_resource('sql/create_tables.sql') as f:
        db_con.executescript(f.read().decode('utf8'))
    click.echo('Database has been initialized.')

def insert_sample():
    db_con = get_db_con()
    with current_app.open_resource('sql/insert_sample.sql') as f:
        db_con.executescript(f.read().decode('utf8'))

