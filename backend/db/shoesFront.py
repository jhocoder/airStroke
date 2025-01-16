import sqlite3
from flask import request
from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv("DB_PATH")


def get_connection():
    conn = sqlite3.connect(database)
    return conn, conn.cursor()

def getAll(page_num):
    conn, mycursor = get_connection()

    mycursor.execute("SELECT COUNT(*) AS total FROM zapati")
    count = mycursor.fetchone()[0]
    per_page = 6
    offset = (page_num - 1) * per_page
    querySql = "SELECT * FROM zapati ORDER BY id LIMIT {} OFFSET {}".format(per_page, offset)
    mycursor.execute(querySql)
    results = mycursor.fetchall()
    conn.close()
    total_pages = (count + per_page - 1) // per_page

    return {"products": results, "totalPages": total_pages}


    

def getShoesProduct(num):
    conn, mycursor = get_connection()
    mycursor.execute("SELECT * FROM zapati WHERE id = ?", (num,))
    product = mycursor.fetchone()
    conn.close()
    return product


def getAsc():
    conn, mycursor = get_connection()
    mycursor.execute("SELECT * FROM zapati ORDER BY price asc")
    results = mycursor.fetchall()
    conn.close()
    return results

def getDesc():
    conn, mycursor = get_connection()
    mycursor.execute("SELECT * FROM zapati ORDER BY price desc")
    results = mycursor.fetchall()
    conn.close()
    return results

