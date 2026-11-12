CREATE TABLE IF NOT EXISTS users (
    id                 INT AUTO_INCREMENT PRIMARY KEY,
    prenom             VARCHAR(50)  NOT NULL,
    nom                VARCHAR(50)  NOT NULL,
    login              VARCHAR(100) NOT NULL UNIQUE,
    password_hash      VARCHAR(255) NOT NULL,
    role               ENUM('super_admin', 'admin', 'user') NOT NULL DEFAULT 'user',
    site               ENUM('Paris', 'Marseille', 'Rennes', 'Grenoble') NOT NULL,
    password_expires_at DATETIME    NOT NULL,
    failed_attempts    INT          NOT NULL DEFAULT 0,
    locked_until       DATETIME     NULL,
    created_at         TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);