bq query --max_rows=600 'SELECT repository_language, repository_name, count(repository_name) as watches, repository_description, repository_url
FROM [githubarchive:github.timeline]
WHERE type="WatchEvent" AND repository_language="Java"
GROUP BY repository_language,repository_name, repository_description, repository_url
ORDER BY watches DESC LIMIT 600'
