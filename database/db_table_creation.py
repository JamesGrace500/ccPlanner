from .db_connections import db_conn_def
import datetime
from dateutil import parser



def create_password_table():
    sql = '''
    CREATE TABLE passwords (
    pass_id  INTEGER PRIMARY KEY NOT NULL,
    scenario_id INTEGER NOT NULL,
    password TEXT 
    );
    '''
    print(db_conn_def("create", sql=sql, table_name="passwords"))


def create_assumptions_table():
    sql = '''
    CREATE TABLE assumptions (
    ass_id INTEGER PRIMARY KEY NOT NULL,
    scenario_id INTEGER NOT NULL, 
    ass_no INTEGER NOT NULL,
    assumption TEXT NOT NULL
    );
    '''
    print(db_conn_def("create", sql=sql, table_name="assumptions"))


def create_bankholidays_table():
    sql = '''
    CREATE TABLE bankholidays (
    bh_id INTEGER PRIMARY KEY NOT NULL, 
    date_date TEXT NOT NULL,
    bh_status INTEGER NOT NULL    
    );
    '''
    print(db_conn_def("create", sql=sql, table_name="bankholidays"))


def create_skills_table():
    sql = '''
    CREATE TABLE skills (
    skill_id INTEGER PRIMARY KEY NOT NULL,
    scenario_id INTEGER NOT NULL,
    skill_name TEXT NOT NULL,
    queue_id INTEGER NOT NULL
    );
    '''
    print(db_conn_def("create", sql=sql, table_name="skills"))


def create_queue_table():
    sql = '''
    CREATE TABLE queues (
    queue_id INTEGER NOT NULL,
    scenario_id INTEGER NOT NULL,
    queue_name TEXT NOT NULL
    );
    '''
    print(db_conn_def("create", sql=sql, table_name="queues"))


def create_intraweek_table():
    sql = '''
    CREATE TABLE intraweek (
    iw_id INTEGER PRIMARY KEY NOT NULL, 
    scenario_id INTEGER NOT NULL,
    day_id INTEGER NOT NULL, 
    percent REAL NOT NULL
    );
    '''
    print(db_conn_def("create", sql=sql, table_name="intraweek"))


def create_daysofweek_table():
    sql = '''
    CREATE TABLE daysofweek (
    day_id INTEGER PRIMARY KEY NOT NULL, 
    day TEXT NOT NULL
    );'''
    print(db_conn_def("create", sql=sql, table_name="daysofweek"))
    days = {
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday',
        7: 'sunday'
    }
    for key, item in days.items():
        sql = 'INSERT INTO daysofweek (day_id, day) VALUES ({b1},"{b2}")'.format(b1=key, b2=item)
        print(db_conn_def('insert', sql=sql, table_name='daysofweek'))


def create_targets_table():
    sql = '''
    CREATE TABLE targets (
     target_id INTEGER PRIMARY KEY NOT NULL, 
     scenario_id INTEGER NOT NULL,
     targettype_id INTEGER NOT NULL, 
     max_occ REAL NOT NULL,
     asa INTEGER NOT NULL, 
     perc_in_asa REAL NOT NULL, 
     cust_patience INTEGER NOT NULL,
     perc_pca REAL NOT NULL
     );
    '''
    print(db_conn_def("create", sql=sql, table_name="targets"))


def create_targettypes_table():
    sql = '''
    CREATE TABLE targettypes (
    targettype_id INTEGER PRIMARY KEY NOT NULL, 
    target_type TEXT NOT NULL
    );
    '''
    print(db_conn_def("create", sql=sql, table_name="targettypes"))
    types = {
        1: 'PCA',
        2: ' ASA'
    }
    for key, item in types.items():
        sql = 'INSERT INTO targettypes (targettype_id,target_type) VALUES ({b1},"{b2}")'.format(b1=key, b2=item)
        print(db_conn_def('insert', sql=sql, table_name='targettypes'))


def create_staffdetails_table():
    sql = '''
    CREATE TABLE staffdetails (
    staff_id INTEGER PRIMARY KEY NOT NULL,
    shifted_hours REAL NOT NULL, 
    paid_hours REAL NOT NULL, 
    working_hours REAL NOT NULL
    );
    '''
    print(db_conn_def("create", sql=sql, table_name="staffdetails"))


def create_openhours_table():
    sql = '''
    CREATE TABLE openhours (
    oh_id INTEGER PRIMARY KEY NOT NULL,
    scenario_id INTEGER NOT NULL,
    open_time TEXT NOT NULL,
    close_time TEXT NOT NULL
    );
    '''
    print(db_conn_def("create", sql=sql, table_name="openhours"))


def create_daysopen_table():
    sql = '''
    CREATE TABLE daysopen (
    do_id INTEGER PRIMARY KEY NOT NULL,
    scenario_id INTEGER NOT NULL, 
    day_id INTEGER NOT NULL, 
    open_state INTEGER NOT NULl
    );
    '''
    print(db_conn_def("create", sql=sql, table_name="daysopen"))


def create_shrinkage_table():
    sql = '''
    CREATE TABLE shrinkage (
    shrink_id INTEGER PRIMARY KEY NOT NULL,
    scenario_id INTEGER NOT NULL,
    shrinkage_name TEXT NOT NULL,
    percent_value REAL NOT NULL,
    shrinkage_type_id INTEGER NOT NULL
    );'''
    print(db_conn_def('create', sql=sql, table_name='shrinkage'))


def create_shrinkagetype_table():
    sql = '''
    CREATE TABLE shrinkagetype(
    shrinkage_type_id INTEGER PRIMARY KEY NOT NULL,
    shrinkage_type TEXT NOT NULL
    );'''
    print(db_conn_def('create', sql=sql, table_name='shrinkagetype'))

    shrink_types = {
        1: 'internal',
        2: 'external'
    }

    for key, item in shrink_types.items():
        sql = 'INSERT INTO shrinkagetype (shrinkage_type_id, shrinkage_type) VALUES ({b1}, "{b2}")'.format(b1=key,
                                                                                                           b2=item)
        print(db_conn_def('insert', sql=sql, table_name='shrinkagetype'))


def create_intervalvol_table():
    sql = '''
    CREATE TABLE intervalvol (
    intvol_id INTEGER PRIMARY KEY NOT NULL, 
    scenario_id INTEGER NOT NULL, 
    week_id TEXT NOT NULL, 
    day_id INTEGER NOT NULL,
    interval_id INTEGER NOT NULL, 
    skill_id INTEGER NOT NULL,
    volume INTEGER NOT NULL, 
    total_handle_time INTEGER NOT NULL
    );
    '''
    print(db_conn_def('create', sql=sql, table_name='intervalvol'))


def create_weeks_table():
    sql = '''
    CREATE TABLE weeks(
    week_id INTEGER PRIMARY KEY NOT NULL, 
    week TEXT NOT NULL
    );'''
    print(db_conn_def('create', sql=sql, table_name='weeks'))
    id_int = 1
    for i in range(900):
        start_date = parser.parse('2021-12-27')
        days_to_add = i * 7
        import_date = start_date + datetime.timedelta(days=days_to_add)
        sql = ' INSERT INTO weeks (week_id,week) VALUES ({b1},"{b2}")'.format(b1=id_int, b2=import_date)
        id_int += 1
        print(db_conn_def('insert', sql=sql, table_name='weeks'))


def create_invervals_table():
    sql = '''
    CREATE TABLE intervals (
    interval_id INTEGER PRIMARY KEY NOT NULL, 
    interval_start TEXT NOT NULL
    );
    '''
    print(db_conn_def('create', sql=sql, table_name='intervals'))
    # code about importing this as a CSV or should I just code it in here?  Will try code
    interval = datetime.timedelta()
    for i in range(96):
        int_id = i + 1
        minutes_to_add = i * 15
        time_change = datetime.timedelta(minutes=minutes_to_add)
        new_interval = interval + time_change
        sql = 'INSERT INTO intervals (interval_id, interval_start) VALUES ({b1}, "{b2}")'.format(b1=int_id, b2=new_interval)
        print(db_conn_def('insert', sql=sql, table_name="intervals"))


def create_all_tables():
    # make sure database is there
    print(db_conn_def("create database"))

    # Now we create each of the tables below.
    # There may be a better way to do this but this is how I know to do it
    # When moving to a stored database, if I do that is, will refactor to make it more clean

    create_password_table()
    create_assumptions_table()
    create_bankholidays_table()
    create_skills_table()
    create_queue_table()
    create_intraweek_table()
    create_daysofweek_table()
    create_targets_table()
    create_targettypes_table()
    create_staffdetails_table()
    create_openhours_table()
    create_daysopen_table()
    create_shrinkage_table()
    create_shrinkagetype_table()
    create_intervalvol_table()
    create_weeks_table()
    create_invervals_table()
