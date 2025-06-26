USE matheus;

DROP TABLE usuarios;

CREATE TABLE usuarios (
	CPF VARCHAR(14),
	NOME VARCHAR(100),
    EMAIL VARCHAR(100),
    SENHA VARCHAR(50),
    
    PRIMARY KEY(CPF)
    
);

-- Inserindo Dados Necessarios

INSERT INTO usuarios (NOME, CPF, EMAIL, SENHA)
VALUES
	('Matheus Henrique', '032.588.976-61', 'matheus.privadotvsmart@gmail.com', '2007matheus2022'),
	('Francielle', '134.566.787-91', 'francielle.especialistaemp@gmail.com', 'FrancielleEspec2000'),
	('Ederson', '985.432.199-31', 'ederson.programasenior@hotmail.com', 'EdersonSenior20Program'),
    ('Antonio José', '987.443.235-81', 'alpharei.frifras@gmail.com', 'alpharei2028frifas2007A'),
    ('Luiz Otavio', '055.698.766-32', 'luiz.otaviopassaorodo@gmail.com', 'LuizPassaORodoMenores'),
    ('Meiry Nascimento', '324.987.544-01', 'meirynascimento.2000@hotmail.com', 'MeiryNascimento2000Programadora');
    
SELECT * FROM usuarios;
    