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
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ramamunagala:hell@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Staff(db.Model):
    __tablename = 'Staff'

    staff_id = db.Column(Integer, primary_key=True)
    job_title = db.Column(db.TEXT)
    last_name = db.Column(db.TEXT)
    first_name = db.Column(db.TEXT)
    gender = db.Column(db.TEXT)
    middle_name = db.Column(db.TEXT)
    tenure_time = db.Column(db.TEXT)

    def __init__(self, staff_id, job_title, first_name, last_name, gender, middle_name, tenure_time):
        self.staff_id = staff_id
        self.job_title = job_title
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.middle_name = middle_name
        self.tenure_time = tenure_time

'''


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


if __name__ == '__main__':

    app.run()
