CREATE TABLE layouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    speed REAL NOT NULL,
    accuracy REAL NOT NULL,
    layout_id INTEGER,
    -- make sure data is valid
    CONSTRAINT layout_id_fkey FOREIGN KEY(layout_id) REFERENCES layout(id),
    CONSTRAINT speed_range CHECK (speed BETWEEN 1 AND 10000),
    CONSTRAINT accuracy_range CHECK (accuracy BETWEEN 0 AND 100)
);