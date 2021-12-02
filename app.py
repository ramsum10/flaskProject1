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


@app.route('/uemployee.html')
def uemployee():
    return render_template('uemployee.html')


@app.route('/usalary.html')
def usalary():
    return render_template('usalary.html')


@app.route('/ushift.html')
def ushift():
    return render_template('ushift.html')


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
        cur.execute(
            "insert into staff(job_title,first_name,last_name,gender,middle_name,tenure_time) values(%s,%s,%s,%s,%s,%s)",
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
        cur.execute("select shift_id from shifts where end_time = %s and start_time = %s and day_or_night = %s",
                    (end, start, dn))
        shid = cur.fetchone()[0]
        cur.execute("insert into works(shift_id,staff_id,start_date,end_date) values(%s,%s,%s,%s)",
                    (shid, sid, sd, ed))
        con.commit()
        cur.close()
        return render_template('index.html')


@app.route('/submitue', methods=['POST'])
def submitue():
    if request.method == 'POST':
        sid = request.form['sid']
        Last_name = request.form['LastName']
        FirstName = request.form['FirstName']
        Gender = request.form['Gender']
        JobTitle = request.form['JobTitle']
        middle = request.form['middle']
        tenure = request.form['tenure']

        if (Last_name):
            cur.execute("update staff set last_name =%s where staff_id=%s ", (Last_name, sid))
            con.commit()
        if (FirstName):
            cur.execute("update staff set first_name =%s where staff_id=%s ", (FirstName, sid))
            con.commit()
        if (Gender):
            cur.execute("update staff set gender =%s where staff_id=%s ", (Gender, sid))
            con.commit()
        if (JobTitle):
            cur.execute("update staff set job_title =%s where staff_id=%s ", (JobTitle, sid))
            con.commit()
        if (middle):
            cur.execute("update staff set middle_name =%s where staff_id=%s ", (middle, sid))
            con.commit()
        if (tenure):
            cur.execute("update staff set tenure_time =%s where staff_id=%s ", (tenure, sid))
            con.commit()
        cur.close()
        return render_template('index.html')


@app.route('/submitus', methods=['POST'])
def submitus():
    if request.method == 'POST':
        sid = request.form['sid']
        salary = request.form['salary']
        cur.execute("select net_pay from earns where staff_id = %s", (sid,))
        netp = cur.fetchone()[0]
        grossp = str(float(salary)*1.3)
        deduct = str(float(salary)*0.3)
        date = "1st"
        cur.execute("insert into salary(payment_date, gross_pay, deductions,net_pay) values( %s, %s, %s,%s)",(date,grossp,deduct,salary))
        con.commit()
        cur.execute("update earns set net_pay =%s where staff_id=%s ", (salary, sid))
        con.commit()
        cur.close()
        return render_template('index.html')

@app.route('/submitush', methods=['POST'])
def submitush():
    if request.method == 'POST':
        shid = request.form['shid']
        sid = request.form['sid']
        start = request.form['st']
        end = request.form['et']

        if (sid):
            cur.execute("delete from works where staff_id =%s ",(sid,))
            cur.execute("update works set staff_id =%s where shift_id=%s ", (sid, shid))
            con.commit()
        if (start):
            cur.execute("update shifts set start_time =%s where shift_id=%s ", (start, sid))
            con.commit()
        if (end):
            cur.execute("update shifts set end_time =%s where shift_id=%s", (end, sid))
            con.commit()
        cur.close()
        return render_template('index.html')
if __name__ == '__main__':
    app.run()
