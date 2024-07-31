from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:nadira@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class StudentDiagnostics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emotional_diagnostics = db.Column(db.Boolean, nullable=False)
    cognitive_diagnostics = db.Column(db.Boolean, nullable=False)
    professional_self_diagnostics = db.Column(db.Boolean, nullable=False)
    abilities_diagnostics = db.Column(db.Boolean, nullable=False)
    monitoring_diagnostics = db.Column(db.Boolean, nullable=False)
    
    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class TeacherDiagnostics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emotional_diagnostics = db.Column(db.Boolean, nullable=False)
    monitoring_diagnostics = db.Column(db.Boolean, nullable=False)
    
    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

class ParentDiagnostics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diagnostics = db.Column(db.Boolean, nullable=False)
    
    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

@app.route('/api/diagnostics/students', methods=['POST'])
def add_student_diagnostics():
    data = request.json
    new_entry = StudentDiagnostics(**data)
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Student diagnostics data added"}), 201

@app.route('/api/diagnostics/teachers', methods=['POST'])
def add_teacher_diagnostics():
    data = request.json
    new_entry = TeacherDiagnostics(**data)
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Teacher diagnostics data added"}), 201

@app.route('/api/diagnostics/parents', methods=['POST'])
def add_parent_diagnostics():
    data = request.json
    new_entry = ParentDiagnostics(**data)
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Parent diagnostics data added"}), 201

@app.route('/api/diagnostics/students', methods=['GET'])
def get_student_diagnostics():
    diagnostics = StudentDiagnostics.query.all()
    return jsonify([diag.to_dict() for diag in diagnostics])

@app.route('/api/diagnostics/teachers', methods=['GET'])
def get_teacher_diagnostics():
    diagnostics = TeacherDiagnostics.query.all()
    return jsonify([diag.to_dict() for diag in diagnostics])

@app.route('/api/diagnostics/parents', methods=['GET'])
def get_parent_diagnostics():
    diagnostics = ParentDiagnostics.query.all()
    return jsonify([diag.to_dict() for diag in diagnostics])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)