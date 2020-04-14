--this is a comment
/*
Select PlaylistId, Name as playlistName

*/





--for all customers who live in the US
--what are their email adresses

/*
Select
-- 	CustomerId, FirstName, LastName, Country, Email 
count(CustomerId) as CustomerCount
from customers
where Country in ("USA", "Brazil")
*/

-- select Country, count(distinct CustomerId) as CustomerCount 
-- from customers
-- group by Country
-- order by CustomerCount DESC
-- limit 5



-- what are all the playlists like classical (classical-related playlist)
		-- SELECT 
		--   PlaylistId
		--   , Name as playlistName
		--   -- ,otherCol
		-- FROM playlists
		-- WHERE playlistName LIKE "%Classical%"


-- for each track, what is the name of that track's genre
-- row per track (3,503)
-- 		SELECT 
-- 		  tracks.TrackId
-- 		  ,tracks.Name as TrackName
-- 		  ,tracks.GenreId
-- 		  ,genres.Name as GenreName
-- 		FROM tracks
-- 		JOIN genres ON tracks.GenreId = genres.GenreId
-- WHERE GenreId IS NULL -- there are no rows with null genres


--for each artist, how many albums?
-- 		Select * 
-- 		from artists
-- 		join albums on artists.ArtistId =albums.ArtistId
-- 		order by ArtistId


-- for each artist, how many albums?
-- rows per artist (275 rows)
-- columns for artist id, artist name, count of album
-- FYI: some artists don't have any albums
​
SELECT 
  r.ArtistId
  ,r."Name" as ArtistName
  ,l.Title as AlbumTitle
FROM artists r
LEFT JOIN albums l ON r.ArtistId = l.ArtistId
ORDER BY 1
