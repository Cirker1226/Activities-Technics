USE matheus;

DROP TABLE medicos;

CREATE TABLE medicos (
	NOME VARCHAR(100),
    RG INT,
	CPF VARCHAR(14),
    ESPECIALIZAÇÃO VARCHAR(100),
    ENTRADA DATE
);

-- Inserção de dados na tabela

INSERT INTO medicos (NOME, RG, CPF, ESPECIALIZAÇÃO, ENTRADA)
VALUES
	('Dr. Matheus Henrique', 2208, '032.588.976-61', 'Paramedico', '2025-08-22'),
	('Dr(a). Francielle', 2354, '134.566.787-91', 'Nutricionista', '2019-03-08'),
	('Dr(a). Paloma', 2007, '985.432.199-31', 'Dentista', '2024-10-12'),
    ('Dr. Antonio José', 1106, '987.443.235-81', 'Cirurgião', '2022-09-13'),
    ('Dr. Luiz Otavio', 2001, '055.698.766-32', 'Clínico Geral', '2032-01-20'),
    ('Dr(a). Meiry Nascimento', 4895, '324.987.544-01', 'Pediatra', '2017-12-17');