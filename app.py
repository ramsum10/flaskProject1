from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence
import psycopg2

app = Flask(__name__)
con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="ramamunagala",
    password="hell")

# cursor
app.debug = True
cur = con.cursor()



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        Last_name = request.form['LastName']
        FirstName = request.form['FirstName']
        Department = request.form['Department']
        JobTitle = request.form['JobTitle']
        '''
        found_staff = Staff.query.filter_by(last_name=Last_name, first_name=FirstName).first()
        '''

        cur.execute("select * from staff where last_name = %s  ", (Last_name,))
        rows = cur.fetchall()

        return render_template('results.html', data=rows)


@app.route('/changes.html')
def changes():
    return render_template('changes.html')

@app.route('/nemployee.html')
def nemp():
    return render_template('nemployee.html')

@app.route('/nshift.html')
def nshift():
    return render_template('nshift.html')


@app.route('/submitne', methods=['POST'])
def submitne():
    if request.method == 'POST':
        Last_name = request.form['LastName']
        FirstName = request.form['FirstName']
        Department = request.form['Department']
        Gender = request.form['Gender']
        JobTitle = request.form['JobTitle']
        middle = request.form['middle']
        tenure = request.form['tenure']
        patient = request.form['patient']
        cur.execute("insert into staff(job_title,first_name,last_name,gender,middle_name,tenure_time) values(%s,%s,%s,%s,%s,%s)",
        (JobTitle, FirstName, Last_name, Gender, middle, tenure))
        con.commit()
        cur.execute("select f_id from facility where facility_name = %s", (Department,))
        fid = cur.fetchone()[0]
        print(fid)
        cur.execute("select staff_id from staff where last_name = %s and first_name = %s", (Last_name, FirstName))
        sid = cur.fetchone()[0]
        print(sid)
        cur.execute("insert into works_within(staff_id,f_id,assignment_name) values(%s,%s,%s)",
               (sid, fid, patient))
        con.commit()
        cur.close()
        return render_template('index.html')


@app.route('/submitns', methods=['POST'])
def submitns():
    if request.method == 'POST':
        Last_name = request.form['LastName']
        FirstName = request.form['FirstName']
        start = request.form['start']
        end = request.form['end']
        dn = request.form['DN']
        ed = request.form['ed']
        sd = request.form['sd']
        cur.execute("select staff_id from staff where last_name = %s and first_name = %s", (Last_name, FirstName))
        sid = cur.fetchone()[0]
        print(sid)
        cur.execute("insert into shifts(end_time,day_or_night,start_time) values(%s,%s,%s)",
               (end, dn, start))
        con.commit()
        cur.execute("select shift_id from shifts where end_time = %s and start_time = %s and day_or_night = %s", (end, start,dn))
        shid = cur.fetchone()[0]
        cur.execute("insert into works(shift_id,staff_id,start_date,end_date) values(%s,%s,%s,%s)",
                    (shid, sid, sd,ed))
        con.commit()
        cur.close()
        return render_template('index.html')


if __name__ == '__main__':

    app.run()
