import os
from .filetypes import FILETYPES

RESERVED = ['__HOTDIR__.md']
def watch_for_changes(directory):
  for raw_doc in os.listdir(directory):
    if os.path.isdir(f"{directory}/{raw_doc}") or raw_doc in RESERVED: continue

    filename, fileext = os.path.splitext(raw_doc)
    if filename in ['.DS_Store'] or fileext == '': continue

    if fileext not in FILETYPES.keys():
      print(f"{fileext} not a supported file type for conversion. Please remove from hot directory.")
      continue

    FILETYPES[fileext](
      directory=directory,
      filename=filename,
      ext=fileext,
    )