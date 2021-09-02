import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:123456789@localhost:5432/postgres')

connection = engine.connect()

test1 = connection.execute(""" SELECT genres.genre, COUNT(artist_id) c FROM genres
LEFT JOIN artist_tracks_genres atg ON genres.id = atg.genres_id
GROUP BY genres.genre
ORDER BY c DESC;
""").fetchall()


test2 = connection.execute(""" SELECT alboms, COUNT(tracks.id) c FROM alboms
LEFT JOIN tracks ON alboms_id = alboms.id
WHERE alboms.year BETWEEN 2019 and 2020
GROUP BY alboms
ORDER BY c DESC;
""").fetchall()

test3 = connection.execute(""" SELECT alboms, ROUND(AVG(tracks.duration),2) ra FROM alboms
LEFT JOIN tracks ON alboms_id = alboms.id
GROUP BY alboms
ORDER BY ra DESC;
""").fetchall()


test4 = connection.execute(""" SELECT artist.artist, artist.nickname FROM artist
JOIN artist_tracks_genres atg ON artist.id = atg.artist_id
JOIN tracks ON atg.tracks_id = tracks.id
JOIN alboms ON tracks.alboms_id = alboms.id
WHERE alboms.year NOT BETWEEN 2019 and 2021
GROUP BY artist.id
""").fetchall()

test5 = connection.execute(""" SELECT namecollection, col.year_ FROM Сollection col
JOIN tracol ON col.id = tracol.collection_id
JOIN tracks ON tracol.tracks_ids = tracks.id
JOIN artist_tracks_genres atg ON tracks.id = atg.artist_id
JOIN artist ON atg.artist_id = artist.id
WHERE artist.artist = 'wolf'
GROUP BY col.namecollection, col.year_
""").fetchall()

test6 = connection.execute(""" SELECT alboms FROM alboms
JOIN tracks ON alboms.id = tracks.alboms_id
JOIN artist_tracks_genres atg ON tracks.id = atg.artist_id
JOIN genres ON atg.genres_id = genres.id
WHERE (SELECT COUNT(genre) FROM genres) > 1
GROUP BY alboms
""").fetchall()


test7 = connection.execute(""" SELECT tracks FROM tracks
JOIN tracol ON tracks.id = tracol.tracks_ids
JOIN Сollection col ON tracol.collection_id = col.id
WHERE tracks.id is null
GROUP BY tracks
""").fetchall()


test8 = connection.execute(""" SELECT artist.artist, artist.nickname FROM artist
JOIN artist_tracks_genres atg ON artist.id = atg.artist_id
JOIN tracks ON atg.tracks_id = tracks.id
WHERE duration = (SELECT MIN(duration) FROM tracks)
GROUP BY artist.artist, artist.nickname
""").fetchall()

test9 = connection.execute(""" SELECT alboms FROM alboms
JOIN tracks ON tracks.alboms_id = alboms.id 
WHERE tracks.alboms_id in (SELECT alboms_id FROM tracks
GROUP BY alboms_id HAVING COUNT(id) = (SELECT COUNT(id) FROM tracks
GROUP BY alboms_id ORDER BY COUNT
LIMIT 1))
ORDER BY alboms
""").fetchall()

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)
print(test6)
print(test7)
print(test8)
print(test9)

