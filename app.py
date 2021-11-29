"""
The script receives a path to a directory and can list the 
name of all the people after reading the JSON files.

Created on Mon Nov 15 00:29:56 2021

@author: danieldeitch1
"""
from os import listdir
import json
from os.path import isfile, join
from flask import Flask, render_template, request

# define the directory of the course
students_path = r'C:\Users\user\Desktop\flask\course\wis-advanced-python-2021-2022\students'

students_dicts = []
ind = 0;
for file_name in listdir(students_path):
    file_path = join(students_path, file_name)
    if isfile(file_path):
        # returns JSON object as a dictionary
        student_file = open(file_path)
        student_data = json.load(student_file)
        student_data['index'] = ind
        ind+=1
        students_dicts.append(student_data)
        


app = Flask(__name__)

@app.route("/", methods=['GET'])
def word_get():
    return render_template('main.html')

@app.route('/student_list', methods=['POST'])
def word_post():
    word = request.form.get('word', '')
    if word == '':
        return render_template('student_list.html',students_dicts=students_dicts)
    else:
        valid_students = [];
        for student in students_dicts:
            for info in student:       
                if (info != 'index') and student[info] != None and (word in student[info]):
                    valid_students.append(student)
                    break
        return render_template('student_list.html',students_dicts=valid_students)


@app.route('/student')
def students_info():
    student_info = students_dicts[int(request.args.get('student_info', None))]
    return render_template('students_info.html',student_info=student_info)