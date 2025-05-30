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


def getAsc(page_num):
    conn, mycursor = get_connection()
    mycursor.execute("SELECT COUNT(*) as TotalAsc FROM zapati")
    count = mycursor.fetchone()[0]
    per_page = 6
    offset = ( page_num - 1) * per_page
    querySql = "SELECT * from zapati ORDER BY price asc LIMIT {} OFFSET {}".format(per_page, offset)
    mycursor.execute(querySql)
    results = mycursor.fetchall()
    conn.close()
    total_pages = (count + per_page - 1) // per_page
    return {"products": results, "totalPages": total_pages}


def getDesc(page_num):
    conn, mycursor = get_connection()
    
    mycursor.execute("SELECT COUNT(*) as TotalDesc FROM zapati")
    count = mycursor.fetchone()[0]
    per_page = 6
    offset = ( page_num - 1) * per_page
    querySql = "SELECT * from zapati ORDER BY price desc LIMIT {} OFFSET {}".format(per_page, offset)
    mycursor.execute(querySql)
    results = mycursor.fetchall()
    conn.close()
    total_pages = (count + per_page - 1) // per_page
    
    return {"products": results, "totalPages": total_pages}

def addUser(nombre, apellido, email, password):
    conn, mycursor = get_connection()
    try:
        mycursor.execute(
            "INSERT INTO users (nombre, apellido, email, password) VALUES (?, ?, ?, ?)",
            (nombre, apellido, email, password),
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return False
    finally:
        conn.close()


    
