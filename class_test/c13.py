f = None
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except Exception as emsg:
#or except IOError as emsg:
  print("Something went wrong when writing to the file, emsg:",emsg)
finally:
  print "ciwsonc:"
  if f != None:
    f.close()
  print type(f)