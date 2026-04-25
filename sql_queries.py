SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS fornecedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cnpj VARCHAR(18)
);

CREATE TABLE IF NOT EXISTS notas_fiscais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_nota INT,
    valor_total DECIMAL(10,2),
    data_emissao DATE,
    fornecedor_id INT,
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
);
"""

QUERY_DASHBOARD = """
SELECT f.nome AS fornecedor, n.numero_nota, n.valor_total, n.data_emissao 
FROM notas_fiscais n 
JOIN fornecedores f ON n.fornecedor_id = f.id
"""
