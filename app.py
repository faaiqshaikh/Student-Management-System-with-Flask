#Group 4
#Mohammed Faiq Shaikh - 100905727
#Favour Eseagwu - 100892897

from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'student.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            dob TEXT NOT NULL,
            amount_due REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def landing_page():
    return render_template('home.html')

# Create UI
@app.route('/ui/create', methods=['GET'])
def create_ui():
    return render_template('create.html')

# Read UI
@app.route('/ui/read', methods=['GET'])
def read_ui():
    return render_template('read.html')

# Update UI
@app.route('/ui/update', methods=['GET'])
def update_ui():
    return render_template('update.html')

# Delete UI
@app.route('/ui/delete', methods=['GET'])
def delete_ui():
    return render_template('delete.html')

# Show All UI
@app.route('/ui/show_all', methods=['GET'])
def show_all_ui():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return render_template('show_all.html', students=students)

# Create
@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = request.json
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (first_name, last_name, dob, amount_due)
                VALUES (?, ?, ?, ?)
            ''', (data['first_name'], data['last_name'], data['dob'], data['amount_due']))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Student created successfully'})
        elif request.content_type == 'application/x-www-form-urlencoded':
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            dob = request.form.get('dob')
            amount_due = request.form.get('amount_due')
            
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (first_name, last_name, dob, amount_due)
                VALUES (?, ?, ?, ?)
            ''', (first_name, last_name, dob, amount_due))
            conn.commit()
            conn.close()
            
            return redirect(url_for('show_all_ui'))

# Read
@app.route('/read/<int:student_id>', methods=['GET'])
def read(student_id):
    if 'application/json' in request.headers.get('Accept'):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
        student = cursor.fetchone()
        conn.close()
        if student:
            return jsonify({
                'student_id': student[0],
                'first_name': student[1],
                'last_name': student[2],
                'dob': student[3],
                'amount_due': student[4]
            })
        return jsonify({'message': 'Student not found'})
    elif 'text/html' in request.headers.get('Accept'):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
        student = cursor.fetchone()
        conn.close()
        if student:
            return render_template('read.html', student=student)
        return jsonify({'message': 'Student not found'})

# Update
@app.route('/update/<int:student_id>', methods=['PUT'])
def update(student_id):
    if request.form.get('_method') == 'PUT':
        if request.content_type == 'application/json':
            data = request.json
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE students
                SET first_name=?, last_name=?, dob=?, amount_due=?
                WHERE student_id=?
            ''', (data['first_name'], data['last_name'], data['dob'], data['amount_due'], student_id))
            conn.commit()
            conn.close()
            if student:
                return render_template('update.html', student=student)
            return jsonify({'message': 'Student updated successfully'})
        
        else:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            dob = request.form.get('dob')
            amount_due = request.form.get('amount_due')
            
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE students
                SET first_name=?, last_name=?, dob=?, amount_due=?
                WHERE student_id=?
            ''', (first_name, last_name, dob, amount_due, student_id))
            conn.commit()
            conn.close()
            
            return redirect(url_for('show_all_ui'))
        

# Delete
@app.route('/delete/<int:student_id>', methods=['DELETE'])
def delete(student_id):
    if request.method == 'DELETE':
        if 'application/json' in request.headers.get('Accept'):
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
            conn.commit()
            conn.close()
            return jsonify({'message': 'Student deleted successfully'})
        elif 'text/html' in request.headers.get('Accept'):
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE student_id = ?', (student_id,))
            student = cursor.fetchone()
            conn.close()
            if student:
                return render_template('delete.html', student=student)
            return jsonify({'message': 'Student not found'})

# Show All
@app.route('/show_all', methods=['GET'])
def show_all():
    if 'application/json' in request.headers.get('Accept'):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        conn.close()
        student_list = []
        for student in students:
            student_list.append({
                'student_id': student[0],
                'first_name': student[1],
                'last_name': student[2],
                'dob': student[3],
                'amount_due': student[4]
            })
        return jsonify(student_list)
    elif 'text/html' in request.headers.get('Accept'):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        conn.close()
        return render_template('show_all.html', students=students)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
