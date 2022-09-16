# write a SQL query to find the name of all reviewers and movies together in a single list #
SELECT reviewer.rev_name
FROM reviewer
UNION
(SELECT movie.mov_title
FROM movie);

