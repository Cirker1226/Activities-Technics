USE matheus;

DROP TABLE agendamentos;

CREATE TABLE agendamentos(
	AGENDAMENTO INT PRIMARY KEY AUTO_INCREMENT,
	CPF VARCHAR(14),
    SERVIÇO VARCHAR(100),
    DATA_AGENDAMENTO DATE,
	HORA_AGENDADA TIME,
    OBSERVAÇÕES TEXT
);

INSERT INTO agendamentos(CPF, SERVIÇO, DATA_AGENDAMENTO, HORA_AGENDADA, OBSERVAÇÕES)
VALUES
	('027.793.626-85', 'Manutenção em Computador', '2025-10-08', '13:00:00', 'Computador lento e upgrade em hardware'),
    ('726.996.156-50', 'Troca de Pasta Termica', '2025-05-10', '15:30:00', 'Temperatura elevada, troca de pasta termica'),
    ('939.093.766-30', 'Instalação de Hardware', '2025-08-22', '14:00:00', 'Troca de placa de video, RTX 3060 TI --> RTX 5060'),
    ('081.655.796-90', 'Formatação de Notebook', '2025-07-23', '14:30:00', 'Computador lento, travando, salvar dados em um HD externo e formata-lo'),
    ('642.324.996-28', 'Limpeza de Hardware', '2025-07-12', '13:30:00', 'Computador sujo, poeira e fazendo barulhos estranhos'),
    ('836.742.446-83', 'Fonte de Alimentação', '2025-09-20', '17:00:00', 'Fonte de alimentação desligando'),
    ('192.618.946-90', 'Instalação de Linux', '2025-11-12', '16:00:00', 'Substituir o Windows e instalar um Linux, Zion OS'),
	('132.121.620-31', 'Instalação de Watter Coller', '2025-08-08', '10:00:00', 'Instalação na parte superior do gabinete'),
	('376.509.950-38', 'Reset de BIOS', '2025-01-10', '12:00:00', 'Reset de BIOS e atualização da BIOS para Processador de quinta geração'),
	('943.821.940-40', 'Upgrade de Memoria RAM', '2025-03-18', '15:40:00', 'Troca de Memoria Ram, 2667Mhz --> 3200Mhz!'),
	('558.253.780-57', 'Troca de Processador', '2025-07-04', '16:30:00', 'Troca de Processador de terceira para quinta geração Ryzen!');

SELECT * FROM agendamentos;