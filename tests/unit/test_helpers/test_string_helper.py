import pytest
from src.helpers.string_helper import StringHelper


@pytest.mark.parametrize(
    'value,prefix,expected',
    [
        ('HelloWorld!', 'H', 'elloWorld!'),
        ('this_is_my_value', 'this_', 'is_my_value'),
        ('!HelloWorld!', '!', 'HelloWorld!')
    ]
)
def test_remove_prefix_works_as_intended(text: str, prefix: str, expected: str):
    """
    Tests if the `StringHelper.remove_prefix()` method removes the prefix from
    the string.
    """
    # Act
    actual = StringHelper.remove_prefix(text, prefix)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(
    'value,postfix,expected',
    [
        ('HelloWorld!', '!', 'HelloWorld'),
        ('this_is_my_value', '_value', 'this_is_my'),
        ('!HelloWorld!', '!', '!HelloWorld')
    ]
)
def test_remove_postfix_works_as_intended(text: str, postfix: str, expected: str):
    """
    Tests if the `StringHelper.remove_postfix()` method removes the postfix from
    the string.
    """
    # Act
    actual = StringHelper.remove_postfix(text, postfix)

    # Assert
    assert actual == expected