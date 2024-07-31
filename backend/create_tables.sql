CREATE TABLE students_diagnostics (
    id SERIAL PRIMARY KEY,
    emotional_diagnostics BOOLEAN NOT NULL,
    cognitive_diagnostics BOOLEAN NOT NULL,
    professional_self_diagnostics BOOLEAN NOT NULL,
    abilities_diagnostics BOOLEAN NOT NULL,
    monitoring_diagnostics BOOLEAN NOT NULL
);

CREATE TABLE teachers_diagnostics (
    id SERIAL PRIMARY KEY,
    emotional_diagnostics BOOLEAN NOT NULL,
    monitoring_diagnostics BOOLEAN NOT NULL
);

CREATE TABLE parents_diagnostics (
    id SERIAL PRIMARY KEY,
    diagnostics BOOLEAN NOT NULL
);
