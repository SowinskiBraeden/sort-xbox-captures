#!/usr/bin/python
import glob
import os

base_path: str = ""
captures: [str] = glob.glob(glob.escape(base_path) + "/*.mp4")

for capture in captures:
  filename: str = capture.split(base_path)[1] # get filename
  game: str = filename.split('202')[0][1:] # get game name from filename
  while game.endswith(' '): game = game[:-1] # clear excess spaces from end of game name
  if not os.path.exists(f'{base_path}/{game}'): os.mkdir(f'{base_path}/{game}') # create game dir if not exists
  os.rename(f'{base_path}/{filename}', f'{base_path}/{game}/{filename}') # move file to game dir
