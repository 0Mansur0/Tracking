-- NOT READY FOR PRODUCTION

-- types of activities
CREATE TABLE activities(
    id INTEGER PRIMARY KEY AUTOINCREMENT
);

-- consist of activities and people
CREATE TABLE actions(
    activity_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    start_timestamp TEXT,
    duration_seconds INTEGER,
    FOREIGN KEY(activity_id) REFERENCES activities(id),
    FOREIGN KEY(person_id) REFERENCES people(id),
    PRIMARY KEY(activity_id, person_id, start_timestamp)
);

CREATE TABLE people(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sex_id INTEGER NOT NULL,
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    birth_date TEXT,
    -- parents can be biological or legal
    parent_1_id INTEGER,
    parent_2_id INTEGER,
    FOREIGN KEY(sex_id) REFERENCES sex(id)
);

CREATE TABLE sex( -- or gender
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "type" TEXT
);
