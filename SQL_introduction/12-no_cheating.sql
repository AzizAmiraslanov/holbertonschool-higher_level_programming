-- deactivate safe updates
SET SQL_SAFE_UPDATES = 0;

-- sonra update-i run et
UPDATE second_table
SET score = 10
WHERE name = 'Bob';

-- optional: geri aktiv et
SET SQL_SAFE_UPDATES = 1;