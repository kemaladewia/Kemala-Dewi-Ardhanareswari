favorite_languages = {
    'jen' : 'python',
    'mala' : 'c',
    'cila' : 'rust',
    'phil' : 'pyhton',
}

poll_takers = ['jen', 'mala', 'lila', 'phil', 'aiai']

for name in poll_takers:
    if name in favorite_languages:
        print(f"Thank you for responding, {name.title()}!")

    else:
        print(f"{name.title()}, please take our favorite language poll.")