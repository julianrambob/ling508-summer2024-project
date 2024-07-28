CREATE DATABASE russian_nouns;
USE russian_nouns;

CREATE TABLE nouns (
    id INT NOT NULL AUTO_INCREMENT,
    form VARCHAR(100),
    pos VARCHAR(50),
    definition VARCHAR(255),
    case VARCHAR(50),
    gender VARCHAR(50),
    number VARCHAR(50),
    declension VARCHAR(50),
    PRIMARY KEY (id)
);
INSERT INTO nouns (form, pos, definition, case, gender, number, declension)
VALUES
('дом', 'noun', 'house', 'nominative', 'masculine', 'singular', 'first'),
('работу', 'noun', 'worker/laborer', 'accusative', 'feminine', 'singular', 'first')
('собака', 'noun', 'dog', 'nominative', 'feminine', 'singular', 'first'),
('окно', 'noun', 'window', 'nominative', 'neuter', 'singular', 'secone');
