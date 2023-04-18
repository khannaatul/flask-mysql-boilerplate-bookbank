-- This file is to bootstrap a database for the CS3200 project. 

-- Create a new database.  You can change the name later.  You'll
-- need this name in the FLASK API file(s),  the AppSmith 
-- data source creation.
create database bookbank_db;

-- Via the Docker Compose file, a special user called webapp will 
-- be created in MySQL. We are going to grant that user 
-- all privilages to the new database we just created. 
-- TODO: If you changed the name of the database above, you need 
-- to change it here too.
grant all privileges on bookbank_db.* to 'webapp'@'%';
flush privileges;

-- Move into the database we just created.
-- TODO: If you changed the name of the database above, you need to
-- change it here too. 
use bookbank_db;

-- Put your DDL 
CREATE DATABASE `BookBank`;

DROP SCHEMA IF EXISTS `BookBank` ;
CREATE SCHEMA IF NOT EXISTS `BookBank` DEFAULT CHARACTER SET latin1 ;
USE `BookBank` ;

CREATE TABLE BookReader
(
    userID   INT PRIMARY KEY,
    first    VARCHAR(50),
    last     VARCHAR(50),
    email    VARCHAR(100),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50) NOT NULL,
    city     VARCHAR(50),
    state    VARCHAR(50),
    zip      INT
);

CREATE TABLE Curator
(
    CuratorID INT PRIMARY KEY,
    first     VARCHAR(50),
    last      VARCHAR(50),
    email     VARCHAR(100),
    username  VARCHAR(100) UNIQUE,
    password  VARCHAR(100) NOT NULL,
    City      VARCHAR(50),
    State     VARCHAR(50),
    Zip       INT
);


CREATE TABLE Author
(
    AuthorID  INT PRIMARY KEY,
    first     VARCHAR(50),
    last      VARCHAR(50),
    email     VARCHAR(100),
    username  VARCHAR(50) UNIQUE,
    password  VARCHAR(50) NOT NULL,
    city      VARCHAR(50),
    state     VARCHAR(50),
    zip       INT,
    CuratorID INT,
    FOREIGN KEY (CuratorID) REFERENCES Curator (CuratorID)
);

CREATE TABLE Books
(
    first           VARCHAR(50),
    last            VARCHAR(50),
    pageCount       INT,
    coverImage      VARCHAR(500),
    genre           VARCHAR(50),
    title           VARCHAR(50),
    link            VARCHAR(50),
    conditionOfBook VARCHAR(50),
    inBank          BOOLEAN,
    isPhysical      BOOLEAN,
    numCopies       INT,
    synopsis        VARCHAR(200),
    isAutographed   BOOLEAN,
    bookID          INT PRIMARY KEY,
    UserID          INT,
    CuratorID       INT,
    AuthorID        INT,
    FOREIGN KEY (UserID) REFERENCES BookReader (UserID),
    FOREIGN KEY (CuratorID) REFERENCES Curator (CuratorID),
    FOREIGN KEY (AuthorID) REFERENCES Author (AuthorID)
);

CREATE TABLE AuthorEmail
(
    AuthorID INT PRIMARY KEY,
    email    VARCHAR(100),
    CONSTRAINT fk_01 FOREIGN KEY (AuthorID) REFERENCES Author (AuthorID)
        ON DELETE CASCADE
);

CREATE TABLE AuthorAddress
(
    AuthorID INT PRIMARY KEY,
    city     VARCHAR(50),
    state    VARCHAR(50),
    zip      INT,
    CONSTRAINT fk_02 FOREIGN KEY (AuthorID) REFERENCES Author (AuthorID) on DELETE CASCADE
);

CREATE TABLE UserEmail
(
    UserID INT PRIMARY KEY,
    email  VARCHAR(100),
    CONSTRAINT fk_03 FOREIGN KEY (UserID) REFERENCES BookReader (UserID) on DELETE CASCADE
);

CREATE TABLE UserAddress
(
    UserID INT PRIMARY KEY,
    city   VARCHAR(50),
    state  VARCHAR(50),
    zip    INT,
    CONSTRAINT fk_04 FOREIGN KEY (UserID) REFERENCES BookReader (UserID) on DELETE CASCADE
);

CREATE TABLE CuratorAddress
(
    CuratorID INT PRIMARY KEY,
    city      VARCHAR(50),
    state     VARCHAR(50),
    zip       INT,
    CONSTRAINT fk_05 FOREIGN KEY (CuratorID) REFERENCES Curator (CuratorID) on DELETE CASCADE
);

CREATE TABLE CuratorEmail
(
    CuratorID INT PRIMARY KEY,
    email     VARCHAR(100),
    CONSTRAINT fk_06 FOREIGN KEY (CuratorID) REFERENCES Curator (CuratorID) on DELETE CASCADE
);

CREATE TABLE CuratorModeration
(
    CuratorID INT,
    UserID    INT,
    PRIMARY KEY (CuratorID, UserID),
    CONSTRAINT fk_07 FOREIGN KEY (CuratorID) REFERENCES Curator (CuratorID) on DELETE CASCADE,
    CONSTRAINT fk_08 FOREIGN KEY (UserID) REFERENCES BookReader (UserID) on DELETE CASCADE
);

CREATE TABLE CuratorEdits
(
    CuratorID INT,
    BookID    INT,
    Primary Key (CuratorID, bookID),
    CONSTRAINT fk_09 FOREIGN KEY (CuratorID) REFERENCES Curator (CuratorID) on DELETE CASCADE,
    CONSTRAINT fk_10 FOREIGN KEY (bookID) REFERENCES Books (bookID) on DELETE CASCADE
);

CREATE TABLE ReaderLibrary
(
    UserID     INT,
    BookID     INT,
    numOfBooks INT,
    PRIMARY KEY (UserID, BookID),
    FOREIGN KEY (UserID) REFERENCES BookReader (UserID),
    FOREIGN KEY (BookID) REFERENCES Books (bookID)
);

-- Add sample data. 
INSERT INTO Curator(curatorid,first,last,email,username,password,city,state,zip) VALUES (3590,'Maressa','Corson','mcorson0@squidoo.com','mcorson0','kZMrYaJZMMQ','Bilalang',NULL,NULL);

INSERT INTO BookReader(userid,first,last,email,username,password,city,state,zip) VALUES (2973,'Sheelagh','Lethardy','slethardy0@so-net.ne.jp','slethardy0','j4UNP0MBb4a','Guzhuyingzi',NULL,NULL);

INSERT INTO Author(authorid,first,last,email,username,password,city,state,zip,curatorid) VALUES (5461,'Jaymie','Deeman','jdeeman0@infoseek.co.jp','jdeeman0','gSiVVgdzCQI8','Foumbot',NULL,NULL,1436);
