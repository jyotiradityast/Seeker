# Seeker

This Python application detects fake news through semantic comparison of user-input headlines with related news from trusted sources stored in a database populated by web feeds. The semantic comparison is powered by OpenAI's GPT 3.5 model. NLTK is used for identifying keywords from user-input headline. These keywords are then used to search for related news headline in a SQLite database with full text search capabilities provided by FTS-5 extension. A verdict is given after semantic comparison.

## Overview
<img src='seeker_overview.png' alt='Overview of the application'>
  
## Screenshot
<img src='screenshot_1.png' alt='Screesnhot'>
