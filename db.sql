

CREATE TABLE Department (
    D_id SERIAL PRIMARY KEY ,
    Department_name TEXT NOT NULL
);
CREATE TABLE Facility (
    F_id SERIAL PRIMARY KEY ,
    Facility_name TEXT NOT NULL,
    Facility_location TEXT NOT NULL,
    Facility_description TEXT NOT NULL
);

CREATE TABLE Staff (
    Staff_id SERIAL PRIMARY KEY ,
    Job_title TEXT NOT NULL ,
    First_name TEXT NOT NULL,
    Last_name TEXT NOT NULL,
    Gender TEXT NOT NULL,
    Middle_name TEXT NOT NULL,
    Tenure_time TEXT NOT NULL

);

CREATE TABLE Works_within(
    Staff_id INT NOT NULL ,
    F_id INT NOT NULL ,
    Assignment_name TEXT NOT NULL ,
    PRIMARY KEY(Staff_id),
    FOREIGN KEY (F_id)
                         REFERENCES Facility(F_id)
);

CREATE TABLE Salary (
    Payment_date TEXT NOT NULL,
    Gross_pay FLOAT NOT NULL ,
    Deductions FLOAT NOT NULL,
    Net_pay FLOAT NOT NULL PRIMARY KEY
);
CREATE TABLE Earns(
    Staff_id INT NOT NULL ,
    Net_pay FLOAT NOT NULL,
    PRIMARY KEY (Staff_id),
    FOREIGN KEY (Net_pay)
                  REFERENCES Salary(Net_pay)
);
CREATE TABLE Shifts (
    Shift_id SERIAL PRIMARY KEY ,
    End_time TEXT NOT NULL ,
    Day_or_Night TEXT NOT NULL,
    Start_time TEXT NOT NULL
);

CREATE TABLE Works (
    Shift_id INT NOT NULL,
    Staff_id INT NOT NULL,
    Start_date TEXT NOT NULL ,
    End_date TEXT NOT NULL ,
    PRIMARY KEY (Staff_id),
    FOREIGN KEY (Shift_id)
                   REFERENCES Shifts(Shift_id)
);

CREATE TABLE Management (
    Staff_id INT NOT NULL,
    PRIMARY KEY (Staff_id),
    FOREIGN KEY (Staff_id)
                   REFERENCES Staff(Staff_id)
);

CREATE TABLE Worker (
    Staff_id INT NOT NULL,
    Job_title TEXT NOT NULL ,
    PRIMARY KEY (Staff_id),
    FOREIGN KEY (Staff_id)
                   REFERENCES Staff(Staff_id)
);
CREATE TABLE Department (
    D_id INT NOT NULL,
    Department_name TEXT NOT NULL ,
    PRIMARY KEY (D_id)
);
CREATE TABLE Manages (
    D_id INT NOT NULL,
    Staff_id INT NOT NULL ,
    PRIMARY KEY (D_id,Staff_id),
    FOREIGN KEY (D_id)
                     REFERENCES Department(D_id),
    FOREIGN KEY (Staff_id)
                     REFERENCES Staff(Staff_id)
);
CREATE TABLE Apart_of (
    D_id INT NOT NULL,
    Staff_id INT NOT NULL ,
    Manger_id INT NOT NULL,
    PRIMARY KEY (Staff_id),
    FOREIGN KEY (D_id)
                     REFERENCES Department(D_id),
    FOREIGN KEY (Manger_id)
                     REFERENCES Management(Staff_id)
);

INSERT INTO Staff (Job_title, First_name, Last_name, Gender, Middle_name, Tenure_time)
VALUES('Nurse', 'Hannah', 'Whitworth', 'F', 'P', '11 months');

INSERT INTO Staff (Job_title, First_name, Last_name, Gender, Middle_name, Tenure_time)
VALUES('Doctor', 'Hook', 'Pawel', 'M', 'S', '10 years');

INSERT INTO Facility (Facility_name, Facility_location, Facility_description) VALUES ('ICU', '2nd Floor', 'Top tier ICU');
INSERT INTO Facility (Facility_name, Facility_location, Facility_description) VALUES ('ER', '1nd Floor', 'Where emergency cases are treated');
INSERT INTO Facility (Facility_name, Facility_location, Facility_description) VALUES ('Neuro Wing', '1nd Floor', 'Where Neuro cases are treated');
INSERT INTO Facility (Facility_name, Facility_location, Facility_description) VALUES ('Cardio Wing', '1nd Floor', 'Where Cardio cases are treated');
INSERT INTO Facility (Facility_name, Facility_location, Facility_description) VALUES ('Pediatric Wing', '1nd Floor', 'Where Pediatric cases are treated');
INSERT INTO Works_within
VALUES (1, 2, 'ER');
INSERT INTO Works_within
VALUES (2, 2, 'ICU');
INSERT INTO Salary
VALUES ('1st', 10000, 2000, 8000);
INSERT INTO Salary
VALUES ('1st', 150000, 40000, 110000);
INSERT INTO Earns VALUES (1, 8000);
INSERT INTO Earns VALUES (2, 110000);
INSERT INTO Shifts
VALUES (1, '8PM', 'DAY', '10AM');
INSERT INTO Shifts
VALUES (2, '2AM', 'NIGHT', '6PM');
INSERT INTO Works
VALUES (1, 1, 'Monday', 'Friday');
INSERT INTO Works
VALUES (2, 2, 'Saturday', 'Wednesday');
INSERT INTO Management VALUES (2);
INSERT INTO Worker VALUES (1);
INSERT INTO Department (Department_name) VALUES ('General');
INSERT INTO Department (Department_name) VALUES ('Cardio');
INSERT INTO Manages VALUES (2, 2);
INSERT INTO Apart_of VALUES (2, 1, 2);
