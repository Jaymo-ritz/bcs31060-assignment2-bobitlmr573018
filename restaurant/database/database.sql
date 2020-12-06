CREATE TABLE IF NOT EXISTS meal_types
(
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS serving_unit
(
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS recipes
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS meals
(
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    name   TEXT    NOT NULL,
    unit   INTEGER NOT NULL,
    type   INTEGER NOT NULL,
    recipe INTEGER NOT NULL,
    FOREIGN KEY (type) REFERENCES meal_types (id),
    FOREIGN KEY (unit) REFERENCES serving_unit (id),
    FOREIGN KEY (recipe) REFERENCES recipes (id)
);

CREATE TABLE IF NOT EXISTS menu
(
    item               INTEGER NOT NULL PRIMARY KEY ,
    price              INTEGER NOT NULL,
    available_servings INTEGER NOT NULL,
    FOREIGN KEY (item) REFERENCES meals (id)
);
CREATE INDEX IX_Menu_Item ON menu (item);

CREATE TABLE IF NOT EXISTS patron
(
    service_number INTEGER PRIMARY KEY AUTOINCREMENT,
    name           TEXT    NOT NULL,
    table_number   INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS orders
(
    service_number INTEGER NOT NULL,
    meal           INTEGER NOT NULL,
    servings       INTEGER NOT NULL,
    FOREIGN KEY (service_number) REFERENCES patron (service_number),
    FOREIGN KEY (meal) REFERENCES meals (id)
);

CREATE TABLE IF NOT EXISTS bills
(
    service_number INTEGER PRIMARY KEY NULL,
    charge  TEXT    NOT NULL,
    paid   INTEGER NOT NULL,
    balance INTEGER NOT NULL,
    date   TEXT    NOT NULL,
    FOREIGN KEY (service_number) REFERENCES patron (service_number)
);
CREATE INDEX IX_Bills_Patron ON bills (service_number);


CREATE TRIGGER Update_Menu
    AFTER INSERT ON orders
BEGIN
    UPDATE menu
    SET available_servings = (available_servings - new.servings)
    WHERE item = new.meal;
END;
