import ipaddress
import sqlite3

def inet_ntoa(string):
    return str(ipaddress.ip_address(string))

def inet_aton(string):
    return int(ipaddress.ip_address(string))

def connect_db(query, method):
    try:
        sqlite_connection = sqlite3.connect("DB/new.db")
        sqlite_connection.create_function('INET_NTOA', 1, inet_ntoa)
        sqlite_connection.create_function('INET_ATON', 1, inet_aton)
        cursor = sqlite_connection.cursor()
        # print("База данных подключена к SQLite")
        
        sqlite_select_query = query
        cursor.execute(sqlite_select_query)
        if method == 'all':
            records = cursor.fetchall()
            return records
        elif method == 'one':
            records = cursor.fetchone()
            return records
        elif method == 'commit':
            sqlite_connection.commit()
            
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQLite", error)