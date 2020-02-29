import sqlite3
conn = sqlite3.connect('org_count.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fn = input("Enter File name: ")
fh = open(fn)

for line in fh:
    if line.startswith('From: '):
        lines = line.split()
        email = lines[1]
        doms = email.split('@')
        org = doms[1]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()




