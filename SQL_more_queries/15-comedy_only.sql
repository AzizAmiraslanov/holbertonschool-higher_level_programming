-- Sadece Comedy türüne ait show'ları listele

SELECT tv_shows.title

FROM tv_shows

-- Show ile genre ilişki tablosunu birleştir
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

-- Genre bilgisine ulaşmak için genre tablosu ile birleştir
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id

-- Sadece Comedy türünü filtrele
WHERE tv_genres.name = 'Comedy'

-- Show adını alfabetik sırala
ORDER BY tv_shows.title ASC;