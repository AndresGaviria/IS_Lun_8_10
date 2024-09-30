CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'user_ptyhon'@'localhost' WITH GRANT OPTION;

CREATE DATABASE db_personas;

CREATE TABLE `db_personas`.`estados` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(50) NOT NULL UNIQUE,
  PRIMARY KEY (`id`)
);

CREATE TABLE `db_personas`.`personas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cedula` VARCHAR(50) NOT NULL ,
  `nombre` VARCHAR(50) NOT NULL,
  `estado` INT NOT NULL,
  `fecha` DATETIME NOT NULL,
  `activo` BIT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_personas__estados` FOREIGN KEY (`estado`) REFERENCES `estados` (`id`)
);

INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Casado-Casada');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Soltero-Soltera');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Viudo-Viuda');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Separado-Separada');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Lo que importa es que Diosito me quiere');

INSERT INTO `db_personas`.`personas` (`cedula`, `nombre`, `estado`, `fecha`, `activo`) 
VALUES ('154287565', 'Pepito Perez', 1, NOW(), 1);

INSERT INTO `db_personas`.`personas` (`cedula`, `nombre`, `estado`, `fecha`, `activo`) 
VALUES ('789546541', 'Susana Martinez', 2, NOW(), 0);

DELIMITER $$
CREATE PROCEDURE `db_personas`.`proc_select_estados`()	
BEGIN 
	SELECT `id`,
        `nombre`
    FROM `db_personas`.`estados`;
END$$ 

DELIMITER $$
CREATE PROCEDURE `db_personas`.`proc_insert_estados` (
	IN `Nombre` VARCHAR(50),
	INOUT `Respuesta` INT
)	
BEGIN 
	INSERT INTO `db_personas`.`estados` (`nombre`) 
	VALUES (`Nombre`);
    
	SET `Respuesta` = 1;
END$$ 

DELIMITER $$
CREATE PROCEDURE `db_personas`.`proc_select_personas`()	
BEGIN 
	SELECT * FROM `db_personas`.`personas`;
END$$ 

DELIMITER $$
CREATE PROCEDURE `db_personas`.`proc_insert_personas` (
	IN `_Cedula` VARCHAR(50),
	IN `_Nombre` VARCHAR(50),
	IN `_Estado` INT,
	IN `_Fecha` DATETIME,
	IN `_Activo` BIT,
	INOUT `Respuesta` INT
)	
BEGIN 
	INSERT INTO `db_personas`.`personas` (`cedula`, `nombre`, `estado`, `fecha`, `activo`) 
	VALUES (`_Cedula`, `_Nombre`, `_Estado`, `_Fecha`, `_Activo`);
    
	SET `Respuesta` = 1;
END$$ 

DELIMITER $$
CREATE PROCEDURE `db_personas`.`proc_update_personas` (
	IN `_Id` INT,
	IN `_Cedula` VARCHAR(50),
	IN `_Nombre` VARCHAR(50),
	IN `_Estado` INT,
	IN `_Fecha` DATETIME,
	IN `_Activo` BIT,
	INOUT `Respuesta` INT
)	
BEGIN 
	UPDATE `db_personas`.`personas`
	SET `cedula` = `_Cedula`, 
		`nombre` = `_Nombre`, 
		`estado` = `_Estado`, 
		`fecha` = `_Fecha`, 
		`activo` = `_Activo`
	WHERE `id` = `_Id`;
    
	SET `Respuesta` = 1;
END$$

DELIMITER $$
CREATE PROCEDURE `db_personas`.`proc_delete_personas` (
	IN `_Id` INT,
	INOUT `Respuesta` INT
)	
BEGIN 
	DELETE FROM `db_personas`.`personas`
	WHERE `id` = `_Id`;
    
	SET `Respuesta` = 1;
END$$ 