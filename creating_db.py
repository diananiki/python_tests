import sqlite3

base = sqlite3.connect('student.db')
cur = base.cursor()
base.execute('CREATE TABLE list(student, task1, task2, task3, task4, task5, automate)')
cur.execute('ALTER TABLE list ADD sum AS(task1 + task2 + task3 + task4 + task5)')
cur.execute('ALTER TABLE list ADD mark AS(IIF(sum>=90 or automate == 1,"A",(IIF(sum>=80,"B",(IIF(sum>=70,"C",IIF(sum>=60,"D",IIF(sum>=50,"E","F"))))))))')
base.commit()