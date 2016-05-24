ALTER TABLE scripts
    ADD arguments VARCHAR(100) NOT NULL CHECK (arguments <> '') DEFAULT '/S';
