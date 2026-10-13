SET NAMES utf8mb4;
CREATE TABLE IF NOT EXISTS animales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    color VARCHAR(50) NOT NULL,
    especie VARCHAR(50) NOT NULL
);

INSERT INTO animales (nombre, color, especie) VALUES
    ('León', 'Dorado', 'Felino'),
    ('Tigre', 'Naranja', 'Felino'),
    ('Pantera', 'Negro', 'Felino');
