# CHANGELOG

## v2.0.0 (TODO)

* Refactored the entire app to create instances of a table and perform actions on them such as `generate` (see README for info)
* Added missing white and black colors, changed how to invoke the colors (see README for info)
* Validate `color` parameter which was previously skipped
* Various quality of life improvements both for the user and for maintainers of this package
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
