prt_dict = {
    'yes': 'aye',
    'English': 'Pirate',
    'sir': 'matey',
    'hotel': 'fleabag inn',
    'student': 'swabbie',
    'boy': 'matey',
    'madam': 'proud beauty',
    'professor': 'foul blaggart',
    'restaurant': 'galley',
    'your': 'yer',
    'excuse': 'arr',
    'students': 'swabbies',
    'are': 'be',
    'lawyer': 'foul blaggart',
    'the': "th'",
    'restroom': 'head',
    'my': 'me',
    'hello': 'avast',
    'is': 'be',
    'man': 'matey',
}
s = str(input("Enter an English sentence: "))
def translate(sent):
    '''
    translate a sentence using pirate dict
    :param sent:
    :return:
    '''
    new_sent = []
    eng_words = list(prt_dict.keys())
    prt_words = list(prt_dict.values())
    lst = sent.split() #split sentence
    for str in lst:
        if str in eng_words: #if word is available in dict
            new_sent.append(prt_dict[str])
        else:
            new_sent.append(str)
    new_sent = ' '.join(new_sent)
    return new_sent

print(translate(s))