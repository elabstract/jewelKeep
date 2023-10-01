import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        return conn
    except Error as e:
        print(e)

def close_connection(conn):
    conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_user(conn, user):
    sql = ''' INSERT INTO users(name,email,password)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    return cur.lastrowid

def create_wishlist_item(conn, wishlist_item):
    sql = ''' INSERT INTO wishlist(user_id,item_name,item_price)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, wishlist_item)
    return cur.lastrowid

def create_store(conn, store):
    sql = ''' INSERT INTO stores(store_name,store_location)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, store)
    return cur.lastrowid

def update_user(conn, user):
    sql = ''' UPDATE users
              SET name = ? ,
                  email = ? ,
                  password = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, user)

def update_wishlist_item(conn, wishlist_item):
    sql = ''' UPDATE wishlist
              SET user_id = ? ,
                  item_name = ? ,
                  item_price = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, wishlist_item)

def update_store(conn, store):
    sql = ''' UPDATE stores
              SET store_name = ? ,
                  store_location = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, store)

def delete_user(conn, id):
    sql = 'DELETE FROM users WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))

def delete_wishlist_item(conn, id):
    sql = 'DELETE FROM wishlist WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))

def delete_store(conn, id):
    sql = 'DELETE FROM stores WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))