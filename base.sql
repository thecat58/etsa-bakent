-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema etsa
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `etsa` ;

-- -----------------------------------------------------
-- Schema etsa
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `etsa` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `etsa` ;

-- -----------------------------------------------------
-- Table `etsa`.`departamento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`departamento` ;

CREATE TABLE IF NOT EXISTS `etsa`.`departamento` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `codigo` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etsa`.`municipio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`municipio` ;

CREATE TABLE IF NOT EXISTS `etsa`.`municipio` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `departamento_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `municipio_departamento_id_66f217c1_fk_departamento_id`
    FOREIGN KEY (`departamento_id`)
    REFERENCES `etsa`.`departamento` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `municipio_departamento_id_66f217c1_fk_departamento_id` ON `etsa`.`municipio` (`departamento_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`tdocumento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`tdocumento` ;

CREATE TABLE IF NOT EXISTS `etsa`.`tdocumento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `etsa`.`usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`usuario` ;

CREATE TABLE IF NOT EXISTS `etsa`.`usuario` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `telefono` INT NULL DEFAULT NULL,
  `correo` VARCHAR(45) NULL DEFAULT NULL,
  `genero` VARCHAR(45) NULL DEFAULT NULL,
  `fechaNacimiento` DATE NULL DEFAULT NULL,
  `foto` VARCHAR(45) NULL DEFAULT NULL,
  `tipoDocumento` VARCHAR(45) NULL DEFAULT NULL,
  `municipio_id` BIGINT NOT NULL,
  `tdocumento_id` INT NOT NULL,
  `numerocc` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `usuario_municipio_id_c87e17a6_fk_municipio_id`
    FOREIGN KEY (`municipio_id`)
    REFERENCES `etsa`.`municipio` (`id`),
  CONSTRAINT `fk_usuario_tdocumento1`
    FOREIGN KEY (`tdocumento_id`)
    REFERENCES `etsa`.`tdocumento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `usuario_municipio_id_c87e17a6_fk_municipio_id` ON `etsa`.`usuario` (`municipio_id` ASC) VISIBLE;

CREATE INDEX `fk_usuario_tdocumento1_idx` ON `etsa`.`usuario` (`tdocumento_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`taller`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`taller` ;

CREATE TABLE IF NOT EXISTS `etsa`.`taller` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `ubicacion` VARCHAR(160) NULL DEFAULT NULL,
  `usuario_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `taller_usuario_id_9582fedd_fk_usuario_id`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `etsa`.`usuario` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `taller_usuario_id_9582fedd_fk_usuario_id` ON `etsa`.`taller` (`usuario_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`materiales`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`materiales` ;

CREATE TABLE IF NOT EXISTS `etsa`.`materiales` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  `fechaCarga` DATE NULL DEFAULT NULL,
  `taller_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `materiales_taller_id_2b17c28f_fk_taller_id`
    FOREIGN KEY (`taller_id`)
    REFERENCES `etsa`.`taller` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `materiales_taller_id_2b17c28f_fk_taller_id` ON `etsa`.`materiales` (`taller_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`archivosadjuntos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`archivosadjuntos` ;

CREATE TABLE IF NOT EXISTS `etsa`.`archivosadjuntos` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nombreArchivo` VARCHAR(145) NOT NULL,
  `rutaArchivo` VARCHAR(145) NULL DEFAULT NULL,
  `materiales_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `archivosadjuntos_materiales_id_e8c6fc76_fk_materiales_id`
    FOREIGN KEY (`materiales_id`)
    REFERENCES `etsa`.`materiales` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `archivosadjuntos_materiales_id_e8c6fc76_fk_materiales_id` ON `etsa`.`archivosadjuntos` (`materiales_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`auth_group`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`auth_group` ;

CREATE TABLE IF NOT EXISTS `etsa`.`auth_group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `name` ON `etsa`.`auth_group` (`name` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`django_content_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`django_content_type` ;

CREATE TABLE IF NOT EXISTS `etsa`.`django_content_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 20
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` ON `etsa`.`django_content_type` (`app_label` ASC, `model` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`auth_permission`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`auth_permission` ;

CREATE TABLE IF NOT EXISTS `etsa`.`auth_permission` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `content_type_id` INT NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `etsa`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 77
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` ON `etsa`.`auth_permission` (`content_type_id` ASC, `codename` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`auth_group_permissions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`auth_group_permissions` ;

CREATE TABLE IF NOT EXISTS `etsa`.`auth_group_permissions` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `etsa`.`auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `etsa`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` ON `etsa`.`auth_group_permissions` (`group_id` ASC, `permission_id` ASC) VISIBLE;

CREATE INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` ON `etsa`.`auth_group_permissions` (`permission_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`auth_user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`auth_user` ;

CREATE TABLE IF NOT EXISTS `etsa`.`auth_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME(6) NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(150) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `username` ON `etsa`.`auth_user` (`username` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`auth_user_groups`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`auth_user_groups` ;

CREATE TABLE IF NOT EXISTS `etsa`.`auth_user_groups` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `etsa`.`auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `etsa`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq` ON `etsa`.`auth_user_groups` (`user_id` ASC, `group_id` ASC) VISIBLE;

CREATE INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id` ON `etsa`.`auth_user_groups` (`group_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`auth_user_user_permissions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`auth_user_user_permissions` ;

CREATE TABLE IF NOT EXISTS `etsa`.`auth_user_user_permissions` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `etsa`.`auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `etsa`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` ON `etsa`.`auth_user_user_permissions` (`user_id` ASC, `permission_id` ASC) VISIBLE;

CREATE INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` ON `etsa`.`auth_user_user_permissions` (`permission_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`categoriaservicio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`categoriaservicio` ;

CREATE TABLE IF NOT EXISTS `etsa`.`categoriaservicio` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NULL DEFAULT NULL,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etsa`.`citas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`citas` ;

CREATE TABLE IF NOT EXISTS `etsa`.`citas` (
  `id` INT NOT NULL,
  `lugar` VARCHAR(45) NULL DEFAULT NULL,
  `hora` TIME NULL DEFAULT NULL,
  `asunto` VARCHAR(160) NULL DEFAULT NULL,
  `taller_id` BIGINT NOT NULL,
  `usuario_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `citas_taller_id_0e6bd55e_fk_taller_id`
    FOREIGN KEY (`taller_id`)
    REFERENCES `etsa`.`taller` (`id`),
  CONSTRAINT `citas_usuario_id_ed66d0fb_fk_usuario_id`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `etsa`.`usuario` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `citas_taller_id_0e6bd55e_fk_taller_id` ON `etsa`.`citas` (`taller_id` ASC) VISIBLE;

CREATE INDEX `citas_usuario_id_ed66d0fb_fk_usuario_id` ON `etsa`.`citas` (`usuario_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`comentarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`comentarios` ;

CREATE TABLE IF NOT EXISTS `etsa`.`comentarios` (
  `id` INT NOT NULL,
  `descripcion` VARCHAR(160) NOT NULL,
  `puntuacion` DECIMAL(10,0) NOT NULL,
  `taller_id` BIGINT NOT NULL,
  `usuario_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `comentarios_taller_id_52b6fe55_fk_taller_id`
    FOREIGN KEY (`taller_id`)
    REFERENCES `etsa`.`taller` (`id`),
  CONSTRAINT `comentarios_usuario_id_8f914ad8_fk_usuario_id`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `etsa`.`usuario` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `comentarios_taller_id_52b6fe55_fk_taller_id` ON `etsa`.`comentarios` (`taller_id` ASC) VISIBLE;

CREATE INDEX `comentarios_usuario_id_8f914ad8_fk_usuario_id` ON `etsa`.`comentarios` (`usuario_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`django_admin_log`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`django_admin_log` ;

CREATE TABLE IF NOT EXISTS `etsa`.`django_admin_log` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME(6) NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `etsa`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `etsa`.`auth_user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co` ON `etsa`.`django_admin_log` (`content_type_id` ASC) VISIBLE;

CREATE INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id` ON `etsa`.`django_admin_log` (`user_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`django_migrations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`django_migrations` ;

CREATE TABLE IF NOT EXISTS `etsa`.`django_migrations` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 22
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `etsa`.`django_session`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`django_session` ;

CREATE TABLE IF NOT EXISTS `etsa`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME(6) NOT NULL,
  PRIMARY KEY (`session_key`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `django_session_expire_date_a5c62663` ON `etsa`.`django_session` (`expire_date` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`pagosuscripcion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`pagosuscripcion` ;

CREATE TABLE IF NOT EXISTS `etsa`.`pagosuscripcion` (
  `id` INT NOT NULL,
  `tipoPago` VARCHAR(45) NULL DEFAULT NULL,
  `usuario_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `pagosuscripcion_usuario_id_fb378f9e_fk_usuario_id`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `etsa`.`usuario` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `pagosuscripcion_usuario_id_fb378f9e_fk_usuario_id` ON `etsa`.`pagosuscripcion` (`usuario_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`principal_post`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`principal_post` ;

CREATE TABLE IF NOT EXISTS `etsa`.`principal_post` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(145) NOT NULL,
  `body` VARCHAR(145) NOT NULL,
  `author_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `Post_author_id_10aa1ba7_fk_auth_user_id`
    FOREIGN KEY (`author_id`)
    REFERENCES `etsa`.`auth_user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `Post_author_id_10aa1ba7_fk_auth_user_id` ON `etsa`.`principal_post` (`author_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`principal_post_descripcion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`principal_post_descripcion` ;

CREATE TABLE IF NOT EXISTS `etsa`.`principal_post_descripcion` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `post_id` BIGINT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `Post_descripcion_post_id_c2f7c15a_fk_Post_id`
    FOREIGN KEY (`post_id`)
    REFERENCES `etsa`.`principal_post` (`id`),
  CONSTRAINT `Post_descripcion_user_id_3ba6787f_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `etsa`.`auth_user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `Post_descripcion_post_id_user_id_1997ee12_uniq` ON `etsa`.`principal_post_descripcion` (`post_id` ASC, `user_id` ASC) VISIBLE;

CREATE INDEX `Post_descripcion_user_id_3ba6787f_fk_auth_user_id` ON `etsa`.`principal_post_descripcion` (`user_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`redessociales`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`redessociales` ;

CREATE TABLE IF NOT EXISTS `etsa`.`redessociales` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `tipoRedSocial` VARCHAR(100) NOT NULL,
  `enlaceRedSocial` VARCHAR(45) NOT NULL,
  `taller_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `redessociales_taller_id_03b6d36c_fk_taller_id`
    FOREIGN KEY (`taller_id`)
    REFERENCES `etsa`.`taller` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `redessociales_taller_id_03b6d36c_fk_taller_id` ON `etsa`.`redessociales` (`taller_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `etsa`.`servicio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `etsa`.`servicio` ;

CREATE TABLE IF NOT EXISTS `etsa`.`servicio` (
  `id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  `precio` VARCHAR(45) NOT NULL,
  `categoriaservicio_id` BIGINT NOT NULL,
  `taller_id` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `servicio_categoriaservicio_id_3484420b_fk_categoriaservicio_id`
    FOREIGN KEY (`categoriaservicio_id`)
    REFERENCES `etsa`.`categoriaservicio` (`id`),
  CONSTRAINT `servicio_taller_id_e65b84c4_fk_taller_id`
    FOREIGN KEY (`taller_id`)
    REFERENCES `etsa`.`taller` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `servicio_categoriaservicio_id_3484420b_fk_categoriaservicio_id` ON `etsa`.`servicio` (`categoriaservicio_id` ASC) VISIBLE;

CREATE INDEX `servicio_taller_id_e65b84c4_fk_taller_id` ON `etsa`.`servicio` (`taller_id` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
