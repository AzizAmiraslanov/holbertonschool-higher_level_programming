-- Tüm show'ları al
-- Genre bağlantısı olmayanları bulmak için LEFT JOIN kullan

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
-- Show ID'leri üzerinden eşleştir
ON tv_shows.id = tv_show_genres.show_id

-- Sadece genre'ı olmayanları filtrele
WHERE tv_show_genres.genre_id IS NULL

-- Sonuçları alfabetik sırala
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;