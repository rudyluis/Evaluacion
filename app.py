from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine,desc
from sqlalchemy.orm import sessionmaker,joinedload
from flask import jsonify
from Entities import  Base, Inscripcion, Curso, Estudiante,Profesor
from sqlalchemy.exc import IntegrityError
from datetime import date
app= Flask(__name__)

app.secret_key='123456'


# Configuración de la base de datos
engine = create_engine('postgresql://postgres:123456@localhost:5432/gestion_academica')


Base.metadata.bind = engine

# Crear sesión de base de datos
DBSession = sessionmaker(bind=engine)

#Ruta Principal
@app.route('/')
def home():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)



