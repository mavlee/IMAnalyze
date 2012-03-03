#!/usr/bin/python
import sys
from BeautifulSoup import BeautifulSoup

# Recursively gets all of the information out of the span elements
# Returns a list
def extract_info(item):
  return_list = []
  if hasattr(item, 'contents'):
    items = item.contents[0]
  else:
    return_list.append(item.string)
    return return_list
  while items is not None:
    if hasattr(items, 'name') and items.name is not None and items.name != 'span':
      return_list.append(items.string.strip())
    else:
      return_list += extract_info(items)
    items = items.findNextSibling('span')
  return return_list

#             MAIN                     #
# Read in all log files to combine
for arg in sys.argv[1::]:
  print "!!!------ Combining file " + arg + " ------!!!\n"
  f = open(arg, 'r')

  # this is pretty terrible figure out better way later
  # when there is less alcohol in system
  testfile = BeautifulSoup(''.join(f.readlines()))
  spans = testfile.span
  while spans is not None:
    if spans.name is not None and spans.name == 'span':
      content = extract_info(spans)#extract_info(spans.contents[0])
      for line in content:
        print line
    spans = spans.findNextSibling('span')

  f.close()
