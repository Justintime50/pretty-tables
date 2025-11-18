import pytest

import pretty_tables


def test_create_table_with_colors(headers, rows, colors):
    output = pretty_tables.create(
        headers=headers,
        rows=rows,
        empty_cell_placeholder="No data",
        colors=colors,
    )

    # fmt: off
    assert output == (
        '| \x1b[94mID\x1b[0m | \x1b[95mName  \x1b[0m | \x1b[1mOccupation       \x1b[0m | \x1b[92mEmployed\x1b[0m |\n'
        '| -- | ------ | ----------------- | -------- |\n'
        '| \x1b[94m1 \x1b[0m | \x1b[95mJustin\x1b[0m | \x1b[1mSoftware Engineer\x1b[0m | \x1b[92mTrue    \x1b[0m |\n'
        '| \x1b[94m2 \x1b[0m | \x1b[95mMisty \x1b[0m | \x1b[1mReceptionist     \x1b[0m | \x1b[92mFalse   \x1b[0m |\n'
        '| \x1b[94m3 \x1b[0m | \x1b[95mJohn  \x1b[0m | \x1b[1mNo data          \x1b[0m | \x1b[92mFalse   \x1b[0m |'
    )
    # fmt: on


def test_create_table_with_colors_partial(headers, rows, colors_partial):
    """Tests that we can use `Colors.none` inbetween other colors as well as use the default color
    when our colors list doesn't match the length of the data.
    """
    output = pretty_tables.create(
        headers=headers,
        rows=rows,
        empty_cell_placeholder="No data",
        colors=colors_partial,
    )

    # fmt: off
    assert output == (
        '| \x1b[94mID\x1b[0m | \x1b[0mName  \x1b[0m | \x1b[95mOccupation       \x1b[0m | \x1b[0mEmployed\x1b[0m |\n'
        '| -- | ------ | ----------------- | -------- |\n'
        '| \x1b[94m1 \x1b[0m | \x1b[0mJustin\x1b[0m | \x1b[95mSoftware Engineer\x1b[0m | \x1b[0mTrue    \x1b[0m |\n'
        '| \x1b[94m2 \x1b[0m | \x1b[0mMisty \x1b[0m | \x1b[95mReceptionist     \x1b[0m | \x1b[0mFalse   \x1b[0m |\n'
        '| \x1b[94m3 \x1b[0m | \x1b[0mJohn  \x1b[0m | \x1b[95mNo data          \x1b[0m | \x1b[0mFalse   \x1b[0m |'
    )
    # fmt: on


def test_create_table_with_default_truthy(headers, rows):
    output = pretty_tables.create(
        headers=headers,
        rows=rows,
        empty_cell_placeholder="No data",
        truthy=3,
    )

    # fmt: off
    assert output == (
        '| ID\x1b[0m | Name  \x1b[0m | Occupation       \x1b[0m | Employed\x1b[0m |\n'
        '| -- | ------ | ----------------- | -------- |\n'
        '| \x1b[92m1 \x1b[0m | \x1b[92mJustin\x1b[0m | \x1b[92mSoftware Engineer\x1b[0m | \x1b[92mTrue    \x1b[0m |\n'
        '| \x1b[91m2 \x1b[0m | \x1b[91mMisty \x1b[0m | \x1b[91mReceptionist     \x1b[0m | \x1b[91mFalse   \x1b[0m |\n'
        '| \x1b[91m3 \x1b[0m | \x1b[91mJohn  \x1b[0m | \x1b[91mNo data          \x1b[0m | \x1b[91mFalse   \x1b[0m |'
    )
    # fmt: on


def test_create_table_with_custom_truthy_colors(headers, rows):
    output = pretty_tables.create(
        headers=headers,
        rows=rows,
        empty_cell_placeholder="No data",
        colors=[pretty_tables.Colors.cyan, pretty_tables.Colors.purple],
        truthy=3,
    )

    # fmt: off
    assert output == (
        '| ID\x1b[0m | Name  \x1b[0m | Occupation       \x1b[0m | Employed\x1b[0m |\n'
        '| -- | ------ | ----------------- | -------- |\n'
        '| \x1b[96m1 \x1b[0m | \x1b[96mJustin\x1b[0m | \x1b[96mSoftware Engineer\x1b[0m | \x1b[96mTrue    \x1b[0m |\n'
        '| \x1b[95m2 \x1b[0m | \x1b[95mMisty \x1b[0m | \x1b[95mReceptionist     \x1b[0m | \x1b[95mFalse   \x1b[0m |\n'
        '| \x1b[95m3 \x1b[0m | \x1b[95mJohn  \x1b[0m | \x1b[95mNo data          \x1b[0m | \x1b[95mFalse   \x1b[0m |'
    )
    # fmt: on


def test_create_table_with_default_truthy_bad_column_index(headers, rows):
    with pytest.raises(ValueError) as exc:
        _ = pretty_tables.create(
            headers=headers,
            rows=rows,
            empty_cell_placeholder="No data",
            truthy="bad",
        )

    assert "The column specified for truthy values does not exist. Column: bad" in str(exc.value)


def test_create_table_with_default_truthy_out_of_range_column(headers, rows):
    with pytest.raises(ValueError) as exc:
        _ = pretty_tables.create(
            headers=headers,
            rows=rows,
            empty_cell_placeholder="No data",
            truthy=5,
        )

    assert "The column specified for truthy values does not exist. Column: 5" in str(exc.value)
