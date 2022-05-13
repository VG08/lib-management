#
# These are the imports
#
import sqlite3
from sqlite3 import Error
from datetime import date, timedelta, datetime
import time
import sys

#
# Function are defined here
#
def create_dbconnect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
#
#
# Function call to open up the SQLITE DB
db_file = r"lib.db"
conn = create_dbconnect (db_file)
#
#
def read_bookid():
    print ('ENTER A VALID BOOK ID')
    try:
        book_id = int(input())
    except ValueError:
        print ('WRONG ENTRY')
    return book_id
#
#
def check_bookid(book_id):
    with conn:
        sql = '''SELECT book_id FROM book_id where book_id = ?'''
        task = (book_id,)
        cur = conn.cursor()
        cur.execute(sql, task)
        rows = cur.fetchone()
        if rows == None:
            return(False)
        else:
            return(True)
#
#

def check_issue(book_id):
    with conn:
        sql = '''SELECT book_id FROM issue where book_id = ?'''
        task = (book_id,)
        cur = conn.cursor()
        cur.execute(sql, task)
        rows = cur.fetchone()
        if rows == None:
            return(False)
        else:
            return(True)
#
#
def check_subissue(sub_id):
    with conn:
        sql = '''SELECT sub_id FROM issue where sub_id = ?'''
        task = (sub_id,)
        cur = conn.cursor()
        cur.execute(sql, task)
        rows = cur.fetchone()
        if rows == None:
            return(False)
        else:
            return(True)
#
#
def check_subid(sub_id):
    with conn:
        sql = '''SELECT sub_id FROM sub where sub_id = ?'''
        task = (sub_id,)
        cur = conn.cursor()
        cur.execute(sql, task)
        rows = cur.fetchone()
        if rows == None:
            return(False)
        else:
            return(True)
#
#
def check_phone(sub_phone):
    with conn:
        sql = '''SELECT sub_phone FROM sub where sub_phone = ?'''
        task = (sub_phone,)
        cur = conn.cursor()
        cur.execute(sql, task)
        rows = cur.fetchone()
        if rows == None:
            return(False)
        else:
            return(True)



#
# Main program
#





option = 10
print("WELCOME TO VG LIBRARY SOFTWARE Copyright (c) 2020 VG08")
print('TYPE THE CORRESPONDING DIGIT TO THE COMMAND TO USE IT')

while not option == 0:




            try:

                print("HERE ARE THE COMMANDS")
                print(' 1:ISSUE A BOOK\n 2:RETURN A BOOK\n 3:ADD A SUBSCRIBER\n 4:REMOVE A SUBSCRIBER\n 5:ADD A BOOK\n 6:REMOVE A BOOK\n 7:SUBSCRIBER LIST\n 8:BOOK LIST\n 9:DEFAULTER LIST\n 10:SEE LIST OF ISSUED BOOKS\n 11:CHECK INFO OF A BOOK \n 0:EXIT')
                option = int(input())
            except ValueError:
                print('USE A VALID COMMAND')

            if option == 1:
                while True:
                    try:
                        print('ENTER BOOK ID')
                        SI = int(input())
                        if check_bookid(SI) == False:
                            print('PLEASE ENTER A VALID BOOK ID')
                            continue
                        if check_issue(SI) == True:
                            print('BOOK IS ALREADY ISSUED')
                            continue
                        break

                    except ValueError:
                        print('PLEASE ENTER A VALID BOOK ID')
                while True:
                    try:
                        print('ENTER SUBSCRIBER ID')
                        SP = int(input())
                        if check_subid(SP) == False:
                            print('PLEASE ENTER A VALID SUBSCRIBER ID')
                            continue
                        if check_subissue(SP) == True:
                            print('SUBSCRIBER ALREADY HAS A BOOK ISSUED')
                            continue
                        break


                    except ValueError:
                        print('PLEASE ENTER A VALID SUBSCRIBER ID')
                        continue 
                isd = date.today()
                dud = isd + timedelta(days=14)
                with conn:
                    sql = '''INSERT INTO issue  values( ?, ?, ?,? )'''
                    task = (SI, SP, isd, dud)
                    cur = conn.cursor()
                    cur.execute(sql, task)
                    conn.commit()
                    print('BOOK ISSUED')  
            
            
            if option == 2:

                while True:
                    try:
                        print('ENTER BOOK ID')
                        SI = int(input())
                        if check_bookid(SI) == False:
                            print('PLEASE ENETER A VALID BOOK ID')
                            continue
                        if check_issue(SI) == False:
                            print('THIS BOOK IS NOT ISSUED')
                            continue
                        break

                    except ValueError:
                        print('PLEASE ENTER A VALID BOOK ID')
                        continue
                with conn:
                    sql = '''DELETE FROM issue WHERE book_id = ? '''
                    task = (SI,)
                    cur = conn.cursor()
                    cur.execute(sql, task)
                    conn.commit()
                print('BOOK RETURNED')
            if option == 3:
                print('ENTER SUBSCRIBERS NAME')
                SN = input()
                while True:                    
                    try:
                        print('ENTER SUBSCRIBERS PHONE NUMBER')
                        SP = int(input())
                        if check_phone(SP) == True:
                            print('THIS PHONE NUMBER IS ALREADY REGISTERED TO A SUBSCRIBER')
                            continue
                        SP1 = SP 
                        count=0
                        while(SP1>0):
                            count=count+1
                            SP1=SP1//10
                        if not count == 10:
                            print('PLEASE ENTER A VALID PHONE NUMBER')
                            continue
                        break

                    except ValueError:
                        print('PHONE NUMBERS DON\'T HAVE ALPHABETS')
                        continue 

                print('ENTER SUBSCRIBERS ADDRESS')
                SA = input()
                with conn:
                    sql = '''INSERT INTO sub (sub_name, sub_phone, sub_add) values( ?, ?, ? )'''
                    task = (SN, SP, SA)
                    cur = conn.cursor()
                    cur.execute(sql, task)
                    conn.commit()
                    print('SUBSCRIBER ADDED')
            
            if option == 4:
                while True:
                    try:
                        print('ENTER SUBSCRIBERS ID')
                        SBI = int(input())
                        if check_subid(SBI) == False:
                            print('PLEASE ENTER A VALID SUBSCRIBER ID')
                            continue
                        break
                    except ValueError:
                        print('PLEASE ENTER A VALID SUBSCRIBER ID')
                        continue
                with conn:
                    sql = '''DELETE FROM sub WHERE sub_id = ? '''
                    task = (SBI,)
                    cur = conn.cursor()
                    cur.execute(sql, task)
                    conn.commit()
                    print('SUBSCRIBER REMOVED')
            if option == 5:
                print('ENTER BOOK\'S NAME')
                B = input()
                if not B:
                    print('BOOK\'S NAME IS COMPULSORY')
                    continue
                print('ENTER AUTHOR\'S NAME')
                AU = input()
                with conn:
                    sql = '''INSERT INTO book_id (book,author) values( ?, ? )'''
                    task = (B, AU)
                    cur = conn.cursor()
                    cur.execute(sql, task)
                    conn.commit()
                    print('BOOK ADDED')
                continue
            if option == 6:
                while True:
                    try:
                        print('ENTER BOOK ID')
                        BI = int(input())
                        if check_bookid(BI) == False:
                            print('PLEASE ENTER A VALID BOOK ID')
                            continue
                        break
                    except ValueError:
                        print('PLEASE ENTER A VALID BOOK ID')
                        continue
                with conn:
                    sql = '''DELETE FROM book_id WHERE book_id = ? '''
                    task = (BI,)
                    cur = conn.cursor()
                    cur.execute(sql, task)
                    conn.commit()
                    print('done')



                    print('book removed')
                    continue


            if option == 7:
                print('HERE IS THE SUBSCRIBER LIST')
                with conn:
                    cur = conn.cursor()
                    cur.execute('SELECT * FROM sub')
                    rows = cur.fetchall()
                    for row in rows:
                        print('SUBSCRIBER ID:', row[0])
                        print('NAME:', row[1])
                        print('PHONE NUMBER:', row[2])
                        print('ADDRESS:', row[3])
                        print('______________________________')

            if option == 8:
                print('HERE IS THE BOOK LIST')
                with conn:
                    cur = conn.cursor()
                    cur.execute('SELECT * FROM book_id')
                    rows = cur.fetchall()
                    for row in rows:
                        print('BOOK ID:', row[0] )
                        print('NAME:', row[1])
                        print('AUTHOR:', row[2])
                        print('______________________________')
            if option == 9:
                isd = date.today()
                print('HERE IS THE DEFAULTER LIST AS OF', isd)
                with conn:
                    sql = '''SELECT * FROM issue WHERE due_date < ?'''
                    task = (isd,)
                    cur = conn.cursor()
                    cur.execute(sql, task)
                    rows = cur.fetchall()

                    for row in rows:
                        print(row)

            if option == 10:
                print('HERE IS THE ISSUE LIST')
                with conn:
                    cur = conn.cursor()
                    cur.execute('SELECT * FROM issue')
                    rows = cur.fetchall()
                    for row in rows:
                        print('SUBSCRIBER ID:', row[0] )
                        print('BOOK ID:', row[1])
                        print('ISSUE DATE:', row[2])
                        print('RETURN DATE:', row[3])
                        print('______________________________')
            if option == 11:
                while True:
                    try:
                        BI = int(input('ENTER THE BOOK ID FOR THE BOOK YOU WANT INFO:  '))
                        if check_bookid(BI) == False:
                            print('PLEASE ENTER A VALID BOOK ID')
                            continue
                        break
                    
                    except ValueError:
                        print(' PLEASE ENTER A VALID BOOK ID')
                if check_issue(BI) == True:
                    with conn:
                        sql = '''SELECT sub_id from issue where book_id = ? '''
                        task = (BI,)
                        cur = conn.cursor()
                        cur.execute(sql, task)
                        rows = cur.fetchone()
                        for row in rows:
                            SI = row

                        
                    with conn:
                        sql = '''SELECT sub_name from sub where sub_id = ?'''
                        task = (SI,)
                        cur = conn.cursor()
                        cur.execute(sql, task)
                        rows = cur.fetchone()
                        for row in rows:
                            SN  = row

                    with conn:
                        sql = '''SELECT due_date from issue where book_id = ?'''
                        task = (BI,)
                        cur = conn.cursor()
                        cur.execute(sql, task)
                        rows = cur.fetchone()
                        for row in rows:
                            dud = row
                        td = date.today()

                        if str(td) < dud:
                            statusissue = f'THIS BOOK IS ISSUED TO {SN} AND HAS TO BE RETURNED ON {dud}'
                        else:
                            statusissue = f'THIS BOOK IS ISSUED TO {SN} AND HAD TO BE RETURNED ON {dud} HENCE IT IS OVERDUE'

                else:
                    statusissue = 'BOOK IS NOT ISSUED TO ANYONE'
                with conn:
                    sql = '''SELECT * FROM book_id where book_id = ?'''
                    task = (BI,)
                    cur = conn.cursor()
                    cur.execute(sql, task)
                    rows = cur.fetchall()
                    for row in rows:
                        print('______________________________')
                        print('BOOK ID:', row[0] )
                        print('NAME:', row[1])
                        print('AUTHOR:', row[2])
                        print(statusissue)
                        print('______________________________')
            if option == 12:
                pass

            if option == 0:
                print('THANK YOU FOR USING VG LIBRARY SOFTWARE Copyright (c) 2020 VG08')
                time.sleep(2)
                sys.exit
            