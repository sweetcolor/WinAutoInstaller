CREATE TABLE hosts (
    id serial PRIMARY KEY,
    hostname varchar(50) NOT NULL CHECK (hostname <> ''),
    ip varchar(15) NOT NULL CHECK (ip <> '')
);

CREATE TABLE scripts (
    id serial PRIMARY KEY,
    program varchar(30) NOT NULL CHECK (program <> ''),
    path_to_script varchar(255) NOT NULL CHECK (path_to_script <> ''),
    script text NOT NULL CHECK (script <> '')
--    installer BLOB,
);