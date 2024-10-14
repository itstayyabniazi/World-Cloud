# World-Cloud

You've likely seen word-clouds before, in order to create word clouds, the software finds the most frequently occurring words in a text file. This mini-programme will ask you to do just that. We'll use the text of the famous novel by Charles Dickens, A Tale of Two Cities, in our programme. <br>

## Badges
![GitHub watchers](https://img.shields.io/github/watchers/itstayyabniazi/World-Cloud)
![GitHub Created At](https://img.shields.io/github/created-at/itstayyabniazi/World-Cloud)
![GitHub last commit](https://img.shields.io/github/last-commit/itstayyabniazi/World-Cloud) <br>
![MIT License](https://img.shields.io/badge/Version-1.0-blue) 
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)


## Included files are:
- word_cloud.py <-- main python file.
- 98-0.txt <-- Tale of Two Cities, by Charles Dickens. Credit to [Project Gutenberg](https://www.gutenberg.org/).
- stopwords <-- common words to exclude. Credit to [Andreas Mueller](https://github.com/amueller/word_cloud/). <br>
You can also use nltk stopwords instead of those provided. Feel free to do so if you wish

## Proccesing: <br>
Here the programme will read and clean the input, then count the frequencies of each word. The data science process involves some pre-processing, then consists of some analysis itself. Optionally, you can also filter out common words (“the”, “this”, “and”, etc.) by excluding words which appear in the stopwords file. <br>
Overall, your approach will be:
- Create a data structure to store the words and the number of occurrences of the word.
- Read in each word from the file, making it lower case and removing punctuation. (Optionally, skip common words).
- For each remaining word, add the word to the data structure or update your count for the word
- Extract the top ten most frequently occurring words from your data structure and print them, along with their frequencies.

## 🚀 About Me
I'm a beginner developer...
