-- Safe updates-i deaktiv et
SET SQL_SAFE_UPDATES = 0;

-- Row-ları sil
DELETE FROM second_table
WHERE score <= 5;

-- Optional: geri aktiv et
SET SQL_SAFE_UPDATES = 1;