-- ============================================================
-- SaborTech Alimentos | Script de Configuração do Banco
-- Execute este arquivo no MySQL Workbench ou MySQL CLI
-- ============================================================

CREATE DATABASE IF NOT EXISTS logistica_alimentar;
USE logistica_alimentar;

-- Tabela de Fornecedores
CREATE TABLE IF NOT EXISTS fornecedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cnpj VARCHAR(18)
);

-- Tabela de Notas Fiscais
CREATE TABLE IF NOT EXISTS notas_fiscais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_nota INT NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    data_emissao DATE NOT NULL,
    fornecedor_id INT,
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
);

-- ============================================================
-- Dados de Exemplo (fictícios)
-- ============================================================

INSERT INTO fornecedores (nome, cnpj) VALUES
('Distribuidora Alvorada',  '12.345.678/0001-90'),
('Frigorífico São Jorge',   '98.765.432/0001-10'),
('Laticínios Bela Vista',   '11.222.333/0001-44'),
('Cerealista Central',      '55.666.777/0001-88'),
('Hortifruti Norte',        '33.444.555/0001-22');

INSERT INTO notas_fiscais (numero_nota, valor_total, data_emissao, fornecedor_id) VALUES
(1001, 15200.00, '2024-01-05', 1),
(1002,  8750.50, '2024-01-08', 2),
(1003, 12300.00, '2024-01-10', 3),
(1004,  4500.75, '2024-01-12', 4),
(1005,  9800.00, '2024-01-15', 5),
(1006, 21000.00, '2024-01-18', 1),
(1007,  6340.00, '2024-01-20', 2),
(1008, 17500.00, '2024-01-22', 3),
(1009,  3200.00, '2024-01-25', 4),
(1010, 11000.00, '2024-01-28', 5);
