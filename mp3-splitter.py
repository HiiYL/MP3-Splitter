from pydub import AudioSegment
from pytimeparse.timeparse import timeparse
import os
import argparse

parser = argparse.ArgumentParser(description='split MP3 files for you.')
parser.add_argument('-i','--input',dest="filename", help='input MP3 file', required=True)
parser.add_argument('-ti','--track_input',dest="tracklist_input", help='input track list file', default="track.txt")

args = parser.parse_args()


print "Loading Music File ... " + args.filename
song = AudioSegment.from_mp3(args.filename)
tracks_list = []
print "Slicing ... "

with open(args.tracklist_input) as tracks:
	for row in tracks:
		time = row.split(' - ')[0]
		name = row.split(' - ')[1].rstrip('\n')
		time_in_millis = timeparse(time) * 1000
		tracks_list.append((time_in_millis, name))

dir = os.getcwd()
save_directory = os.path.join(dir, args.filename + " - Split")
if not os.path.exists(save_directory):
	os.makedirs(save_directory)
track_list_length = len(tracks_list)
for idx, track in enumerate(tracks_list):
	print "Working On ... " + track[1] + ".mp3 ( " + str(idx + 1) + " / " + str(track_list_length) + " )"
	begin = track[0]
	try:
	  end = tracks_list[idx + 1][0]
	except IndexError:
	  end = len(song)
	current_slice = song[begin:end]
	filename = os.path.join(save_directory, track[1] + ".mp3")

	current_slice.export(filename, format="mp3")

