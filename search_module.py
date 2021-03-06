import requests
import re
import os


curr_path = os.path.split(os.path.realpath(__file__))
os.chdir(curr_path[0])

artist = 'rammstein'
song = 'rosenrot'

r1 = requests.get(f'https://www.amalgama-lab.com/songs/{artist[0]}/{artist}/{song}.html')
for_analysis = r1.text.split('\n')
separator = '<div class="string_container"><div class="original">'
ref1 = r'<div class="string_container"><div class="original">'
ref2 = r'<div class="empty_container"><div class="original"><br /></div>'
final_text = ''
for idx in range(len(for_analysis)):
    if re.search(ref1, for_analysis[idx], flags=re.DOTALL):
        if for_analysis[idx] == separator:
            middle = for_analysis[idx+1].split('</div>')[0]
            print(middle)
            final_text += middle+'\n'
        else:
            middle = for_analysis[idx].split(separator)[1].split('</div>\r')[0]
            final_text += middle + '\n'
            print(middle)
    if re.search(ref2, for_analysis[idx]):
        print('\n')
        final_text += '\n'

print(final_text)

with open('new_request.html', 'w+') as f:
    for string in for_analysis:
        f.write(string)
    f.close()

with open(f'{artist}-{song} lyrics.txt', 'w+') as lyrics:
    lyrics.write(final_text)
    lyrics.close()
