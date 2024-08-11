DROP DATABASE IF EXISTS russian_nouns;
CREATE DATABASE russian_nouns;
ALTER DATABASE russian_nouns CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE russian_nouns;

CREATE TABLE IF NOT EXISTS nouns (
    id INT NOT NULL AUTO_INCREMENT,
    form VARCHAR(100),
    pos VARCHAR(50),
    definition VARCHAR(255),
    base_form VARCHAR(100),
    nounCase VARCHAR(50),
    gender VARCHAR(50),
    number VARCHAR(50),
    declension VARCHAR(50),
    PRIMARY KEY (id)
);
ALTER TABLE nouns
MODIFY form VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
/*INSERT INTO nouns (form, pos, definition, nounCase, gender, number, declension)
VALUES
('дом', 'noun', 'house', 'nominative', 'masculine', 'singular', 'first'),
('работа', 'noun', 'worker/laborer', 'nominative', 'feminine', 'singular', 'first'),
('работу', 'noun', 'worker/laborer', 'accusative', 'feminine', 'singular', 'first'),
('собака', 'noun', 'dog', 'nominative', 'feminine', 'singular', 'first'),
('окно', 'noun', 'window', 'nominative', 'neuter', 'singular', 'second');*/