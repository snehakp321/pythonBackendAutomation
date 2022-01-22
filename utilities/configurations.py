import configparser
from mysql.connector import Error
import mysql.connector


def getConfig():
    config = configparser.ConfigParser()
    config.read("/Users/snehaprakash/PycharmProjects/pythonBackendAutomation/utilities/properties.ini")
    return config


connect_config = {
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database'],
}


def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print('connection is successful')
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

