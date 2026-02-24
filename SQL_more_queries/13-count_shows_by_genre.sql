-- Her genre için bağlı show sayısını hesapla

SELECT 
    tv_genres.name AS genre,              -- Genre adını göster
    COUNT(tv_show_genres.show_id) AS number_of_shows  -- Bağlı show sayısını hesapla

FROM tv_genres

-- Genre ile show ilişki tablosunu birleştir
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id

-- Her genre için grupla
GROUP BY tv_genres.id

-- Show sayısına göre azalan sırala
ORDER BY number_of_shows DESC;