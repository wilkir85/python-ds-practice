def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    vowel_indices = [i for i, char in enumerate(s) if char in vowels]
    vowels_to_reverse = [s[i] for i in vowel_indices]
    reversed_vowels = vowels_to_reverse[::-1]
    result = ''
    for i, char in enumerate(s):
        if char in vowels:
            result += reversed_vowels.pop(0)
        else:
            result += char
    return result