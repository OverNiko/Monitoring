import ipaddress
import sqlite3

def inet_ntoa(string):
    return str(ipaddress.ip_address(string))

def inet_aton(string):
    return int(ipaddress.ip_address(string))

def connect_db(query, method):
    try:
        with sqlite3.connect("DB/new.db") as sqlite_connection:
            sqlite_connection.create_function('INET_NTOA', 1, inet_ntoa)
            sqlite_connection.create_function('INET_ATON', 1, inet_aton)
            cursor = sqlite_connection.cursor()
            cursor.execute(query)
            
            methods = {
                'all': cursor.fetchall,
                'one': cursor.fetchone,
                'commit': sqlite_connection.commit
            }
            
            if method in methods:
                return methods[method]()
            else:
                raise ValueError(f"Unknown method: {method}")
                
    except sqlite3.Error as error:
        print("Ошибка при подключении к SQLite", error)
    except ValueError as ve:
        print("Ошибка:", ve)