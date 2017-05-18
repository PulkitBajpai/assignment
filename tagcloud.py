__author__ = 'pulkit-bajpai'


from wordfreq import general_function

def main():
  data,taglist = general_function()
  # find max and min frequency
  ranges = getRanges(taglist)
  writeCloud(taglist, ranges, 'tags.html')

def getRanges(taglist):
  taglist = sorted(taglist)[::-1]
  mincount = taglist[0][1]
  maxcount = taglist[len(taglist) - 1][1]
  distrib = (maxcount - mincount) / 4;
  index = mincount
  ranges = []
  while (index <= maxcount):
    range = (index, index + distrib)
    index = index + distrib
    ranges.append(range)
  return ranges

def writeCloud(taglist, ranges, outputfile):
  new_list = []
  taglist = list(set(taglist))
  outputf = open(outputfile, 'w')
  outputf.write("<style type=\"text/css\">\n")
  outputf.write(".smallestTag {font-size: xx-small;}\n")
  outputf.write(".smallTag {font-size: small;}\n")
  outputf.write(".mediumTag {font-size: medium;}\n")
  outputf.write(".largeTag {font-size: large;}\n")
  outputf.write(".largestTag {font-size: xx-large;}\n")
  outputf.write("a:hover { background-color: yellow;}\n")
  outputf.write("</style>\n")
  rangeStyle = ["smallestTag", "smallTag", "mediumTag", "largeTag", "largestTag"]
  # resort the tags alphabetically
  taglist.sort(lambda x, y: cmp(x[0], y[0]))
  for tag in taglist:
    rangeIndex = 0
    for range in ranges:
      url = tag[0].replace(' ', '+')
      # if url not in new_list:
      #     new_list.append(url)
      if (tag[1] >= range[0] and tag[1] <= range[1]):
        outputf.write("<span class=\"" + rangeStyle[rangeIndex] + "\"><a href=\"" + url + "\">" + tag[0] + "</a></span></br> ")
        break
      rangeIndex = rangeIndex + 1
  outputf.close()

if __name__ == "__main__":
  main()
