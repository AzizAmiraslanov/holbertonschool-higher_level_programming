-- Dexter dizisine ait tüm genre'ları listele

SELECT tv_genres.name

FROM tv_shows

-- Dexter'ın genre bağlantılarını bul
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

-- Genre isimlerini almak için genre tablosu ile birleştir
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id

-- Sadece Dexter dizisini filtrele
WHERE tv_shows.title = 'Dexter'

-- Genre adını alfabetik sırala
ORDER BY tv_genres.name ASC;