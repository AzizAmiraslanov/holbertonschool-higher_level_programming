-- Tüm show'ları ve bağlı oldukları genre'ları listele
-- Genre yoksa NULL görünsün

SELECT 
    tv_shows.title,       -- Show adı
    tv_genres.name        -- Genre adı

FROM tv_shows

-- Önce show ile ilişki tablosunu LEFT JOIN yap
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

-- Sonra genre tablosuna bağlan
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id

-- Önce show adına göre alfabetik sırala
-- Sonra genre adına göre alfabetik sırala
ORDER BY tv_shows.title ASC, tv_genres.name ASC;