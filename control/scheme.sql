-- NOT READY FOR PRODUCTION

CREATE TABLE activities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    person_id INTEGER,
    start_second INTEGER,
    end_time_min INTEGER,
    FOREIGN KEY(person_id) REFERENCES people(id)
);

CREATE TABLE people(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sex_id INTEGER NOT NULL,
    first_name TEXT,
    middle_name TEXT, -- for russian
    last_name TEXT,
    birth_date TEXT,
    -- parents can be biological or legal
    parent_1_id INTEGER,
    parent_2_id INTEGER
);

CREATE TABLE sex( -- or gender
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "type" TEXT
);