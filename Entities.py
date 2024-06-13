from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Estudiante(Base):
    __tablename__ = 'estudiante'
    id_estudiante = Column(Integer, primary_key=True)
    nombre = Column(String)
    fecha_nacimiento= Column(Date)
    direccion = Column(String)
    carrera = Column(String)

    @staticmethod
    def adicionar(session, nombre, fecha_nacimiento, direccion, carrera):
        nuevo_estudiante = Estudiante(nombre=nombre, fecha_nacimiento=fecha_nacimiento, direccion=direccion, carrera=carrera)
        session.add(nuevo_estudiante)
        session.commit()

    @staticmethod
    def modificar(session, id_estudiante, nombre=None, fecha_nacimiento=None, direccion=None, carrera=None):
        estudiante= session.query(Estudiante).filter_by(id_estudiante=id_estudiante).first()
        if estudiante:        
            if nombre:
                estudiante.nombre = nombre
            if fecha_nacimiento:
                estudiante.fecha_nacimiento = fecha_nacimiento
            if direccion:
                estudiante.direccion = direccion
            if carrera:
                estudiante.carrera = carrera
            session.commit()

    @staticmethod
    def eliminar(session, id_estudiante):
        estudiante= session.query(Estudiante).filter_by(id_estudiante=id_estudiante).first()

        if estudiante:
            session.delete(estudiante)
            session.commit()

class Profesor(Base):
    __tablename__ = 'profesor'
    id_profesor = Column(Integer, primary_key=True)
    nombre = Column(String)
    departamento = Column(String)
    salario = Column(Numeric)

    @staticmethod
    def adicionar(session, nombre, departamento, salario):
        nuevo_profesor = Profesor(nombre=nombre, departamento=departamento, salario=salario)
        session.add(nuevo_profesor)
        session.commit()

    @staticmethod
    def modificar(session, id_profesor, nombre=None, departamento=None, salario=None):
        profesor= session.query(Profesor).filter_by(id_profesor=id_profesor).first()
        if profesor:
            if nombre:
                profesor.nombre = nombre
            if departamento:
                profesor.departamento = departamento
            if salario:
                profesor.salario = salario
            session.commit()

    @staticmethod
    def eliminar(session, id_profesor):
        profesor= session.query(Profesor).filter_by(id_profesor=id_profesor).first()

        if profesor:
            session.delete(profesor)
            session.commit()

class Curso(Base):
    __tablename__ = 'curso'
    id_curso = Column(Integer, primary_key=True)
    nombre = Column(String)
    id_profesor = Column(Integer, ForeignKey('profesor.id_profesor'))
    semestre = Column(String)
    profesor = relationship("Profesor")

    @staticmethod
    def adicionar(session, nombre, id_profesor, semestre):
        nuevo_curso = Curso(nombre=nombre, id_profesor=id_profesor, semestre=semestre)
        session.add(nuevo_curso)
        session.commit()

    @staticmethod
    def modificar(session, id_curso, nombre=None, id_profesor=None, semestre=None):
        curso= session.query(Curso).filter_by(id_curso=id_curso).first()
        if curso:
            if nombre:
                curso.nombre = nombre
            if id_profesor:
                curso.id_profesor = id_profesor
            if semestre:
                curso.semestre = semestre
            session.commit()

    @staticmethod
    def eliminar(session, id_curso):
        curso= session.query(Curso).filter_by(id_curso=id_curso).first()

        if curso:
            session.delete(curso)
            session.commit()

class Inscripcion(Base):
    __tablename__ = 'inscripcion'
    id_inscripcion = Column(Integer, primary_key=True)
    id_estudiante = Column(Integer, ForeignKey('estudiante.id_estudiante'))
    id_curso = Column(Integer, ForeignKey('curso.id_curso'))
    nota = Column(Numeric)
    estudiante = relationship("Estudiante")
    curso = relationship("Curso")

    @staticmethod
    def adicionar(session, id_estudiante, id_curso, nota):
        nueva_inscripcion = Inscripcion(id_estudiante=id_estudiante, id_curso=id_curso, nota=nota)
        session.add(nueva_inscripcion)
        session.commit()

    @staticmethod
    def modificar(session, id_inscripcion, id_estudiante=None, id_curso=None, nota=None):
        inscripcion= session.query(Inscripcion).filter_by(id_inscripcion=id_inscripcion).first()

        if inscripcion:
            if id_estudiante:
                inscripcion.id_estudiante = id_estudiante
            if id_curso:
                inscripcion.id_curso = id_curso
            if nota:
                inscripcion.nota = nota
            session.commit()

    @staticmethod
    def eliminar(session, id_inscripcion):
        inscripcion= session.query(Inscripcion).filter_by(id_inscripcion=id_inscripcion).first()

        if inscripcion:
            session.delete(inscripcion)
            session.commit()

