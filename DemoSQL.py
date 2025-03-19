#sqlite3을 사용하는 데모
import sqlite3

#연결객체를 생성
con = sqlite3.connect('c:\\work\\sample.db')
#커서객체를 생성
cur = con.cursor()
#테이블 생성
cur.execute('CREATE TABLE people (name_last, age)')
#데이터 입력   
cur.execute("INSERT INTO people VALUES ('Smith', 27)")

#여러건
datalist = [('Jones', 34), ('Brown', 23)]
datalist.append(('Green', 45))
cur.executemany('INSERT INTO people VALUES (?, ?)', datalist)

#데이터 조회
cur.execute('SELECT * FROM people')
#선택한 블럭을 주석 처리 : ctrl + /
for row in cur:
    print(row)

#커밋
con.commit()



