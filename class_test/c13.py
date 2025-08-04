# File handling with exception handling
f = None
try:
    f = open("demofile.txt", "w")
    f.write("Lorum Ipsum")
except Exception as emsg:
    # or except IOError as emsg:
    print("Something went wrong when writing to the file, emsg:", emsg)
finally:
    print("Closing file:")
    if f is not None:
        print("File is open, now closing...")
        f.close()
    print(f is not None, type(f))
