# MP3-Splitter
A tool to easily split MP3 compilations from youtube or other sources.

# Installation
1. Run ` pip install -r requirements.txt ` to automagically install all requirements.

# Usage
1. Prepare a tracks.txt file with time of each track within the mp3 in the following format.

   ` HH:MM - TITLE `

   E.g:
   ```
   00:00 - Tears in the Wind
   02:49 - Power of the Saint
   04:41 - City a1
   05:10 - City a2
   07:04 - City b
   08:37 - City c
   09:56 - City d
   13:37 - City e
   15:42 - City f
   18:00 - City g
   ```
2. mp3-splitter.py [-h] -i FILENAME [-ti TRACKLIST_INPUT]

   E.g:
   `python mp3-splitter.py -i "Perfect World - Complete Soundtrack.mp3" `
   
# Sample Output:
  [<img src="https://cloud.githubusercontent.com/assets/7908951/14741201/316f520a-08c7-11e6-800f-2fca410c7fd2.png" width=355 height=240>](Example)
  [<img src="https://cloud.githubusercontent.com/assets/7908951/14741248/8bec2a8c-08c7-11e6-955f-e6afde14b062.png" width=355 height=240>](Example)
