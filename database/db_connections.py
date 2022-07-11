import sqlite3


def db_conn_def(query_type, table_name=False, sql=False):
    # if no sql then it means that DB is to be created or initialised
    if not sql:
        return create_db()

    if query_type == "select":
        return select_query(sql, table_name)

    if query_type == "delete":
        return delete_query(sql, table_name)

    if query_type == "update":
        return update_query(sql, table_name)

    if query_type == "insert":
        return insert_query(sql, table_name)

    if query_type == "create":
        return create_query(sql, table_name)


def update_query(sql, table_name):
    pass


def delete_query(sql, table_name):
    message = {}
    try:
        conn = sqlite3.connect('cc_planner.db')
        conn.execute(sql)
        conn.commit()
        message['status'] = 'record(s) successfully deleted from {b1} table'.format(b1=table_name)
    except sqlite3.Error as error:
        conn.rollback()
        message['status'] = 'there was a problem running the delete statement on the {b1} table. Error: {b2}'.format(b1=table_name, b2=error)
    finally:
        conn.close()

    return message['status']

def select_query(sql, table_name):

    return_load = {}

    try:
        conn = sqlite3.connect('cc_planner.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        headings = list(map(lambda x: x[0], cur.description))

        # convert rows to be passed back
        return_rows = []
        mapping_list = []
        for row_heading in headings:
            mapping_list.append(row_heading)
        return_rows.append(mapping_list)

        for i in rows:
            mapping_list = []
            for row_heading in headings:
                mapping_list.append(i[row_heading])
            return_rows.append(mapping_list)


    except sqlite3.Error as error:
        conn.rollback()
        return_load['status'] = "there was an error selecting data from the {b1} table.  Error:  {b2}".format(b1=table_name, b2=error)

    finally:
        conn.close()
        return_load['status'] = "successfully selected data from the {b1} table".format(b1=table_name)
        return_load['payload'] = return_rows

    return return_load


def create_db():
    message = {}
    try:
        conn = sqlite3.connect('cc_planner.db')
        cur = conn.cursor()
        conn_version = 'select sqlite_version();'
        cur.execute(conn_version)
        record = cur.fetchall()
        message['status'] = 'Database has been created:  SQLite Database is version: ' + str(record)
        cur.close()

    except sqlite3.Error as error:
        message['status'] = 'Error while connecting to the database' + error

    finally:
        if conn:
            conn.close()
            message['status'] = 'The SQLite connection is closed'

    return message


def create_query(sql, table_name):
    message = {}
    try:
        conn = sqlite3.connect('cc_planner.db')
        conn.execute(sql)
        conn.commit()
        message['status'] = 'The ' + str(table_name) + ' has been created'
    except sqlite3.Error as error:
        conn.rollback()
        message['status'] = 'The ' + str(table_name) + ' has failed. Error: ' + str(error)
    finally:
        conn.close()

    return message


def insert_query(sql, table_name):
    message = {}
    try:
        conn = sqlite3.connect('cc_planner.db')
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        message['status'] = 'The insert statement into {b1} was successful'.format(b1=table_name)
    except sqlite3.Error as error:
        conn.rollback()
        message['status'] = 'The insert statement into {b1} has failed. Error: {b2}'.format(b1=table_name, b2=error)
    finally:
        conn.close()

    return message
