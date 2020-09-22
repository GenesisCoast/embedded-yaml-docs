import pytest
from src.helpers.string_helper import StringHelper


@pytest.mark.parametrize(
    'text,prefixes',
    [
        ('HelloWorld!', ['!']),
        ('this_is_my_value', ['value']),
        ('HelloWorld!', ['!Hello'])
    ]
)
def test_startswith_multi_returns_false_when_string_does_not_startswith(text: str, prefixes: str):
    """
    Tests if the `StringHelper.startswith_multi()` method returns false
    when the string does not starts with a value.
    """
    # Arrange
    result = StringHelper.startswith_multi(text, prefixes)

    # Assert
    assert result == False

@pytest.mark.parametrize(
    'text,prefixes',
    [
        ('HelloWorld!', ['H']),
        ('this_is_my_value', ['this']),
        ('!HelloWorld!', ['!Hello'])
    ]
)
def test_startswith_multi_returns_true_when_string_startswith(text: str, prefixes: str):
    """
    Tests if the `StringHelper.startswith_multi()` method returns true
    when the string starts with a value.
    """
    # Arrange
    result = StringHelper.startswith_multi(text, prefixes)

    # Assert
    assert result == True


@pytest.mark.parametrize(
    'text,prefix,expected',
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
    'text,postfix,expected',
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
