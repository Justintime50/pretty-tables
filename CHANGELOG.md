# CHANGELOG

## v2.0.2 (2021-11-30)

* Adds `mypy` to run type checking and publishes types with new `py.typed` file

## v2.0.1 (2021-11-25)

* Adds missing `__all__` variable for imports

## v2.0.0 (2021-11-22)

* Refactored the entire app to be more straightforward to use. Create a new table by calling `pretty_tables.create()` and pass in your arguments
* Added missing white and black colors, changed how to invoke the colors (now `pretty_tables.Colors.blue` instead of `pretty_tables.TableColors.OKBLUE`)
* Validate `color` parameter which was previously skipped
* Overhauls documentation providing all customization options (closes #2)

## v1.3.0 (2021-09-10)

* Re-adds the horizontal break between header and table content that was accidentally removed in `v1.2.0`
* Bumps minimum Python version to 3.7

## v1.2.0 (2021-07-26)

* Adds the ability to change column colors statically (index) or dynamically based on truthyness (closes #1, thanks @gagelarsen)

## v1.1.0 (2021-04-20)

* Adds horizontal break between header and table content
* Small refactor of stringify Python `True/False` when inserting to a table

## v1.0.0 (2020-11-07)

* Initial release
* Pass headers and rows to generate a uniformly dispersed pretty table
* Added input validation to ensure headers/rows were set and valid lists and correct length
