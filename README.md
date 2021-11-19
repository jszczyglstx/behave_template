# behave_template

Run command: For all tests:

behave -D driver=chrome -D base_url=some_url

For single feature file:

behave features/some_feature.feature -D driver=chrome -D base_url=some_url

For single tag add:

--tags=@tag_name

For multiple tags add:

--tags=@tag_name1, @tag_name2

Exclude tag/s:

--tags ~@tag_name
