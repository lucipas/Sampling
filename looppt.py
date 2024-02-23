import wave
import os

for files in os.walk('../Sampling'):
  for filename in files:
      print(filename)
  input()


