
testStr = "this is test string for a file write"

# ---------------------------------------------------------------------------- #
#                                WRITING A FILE                                #
# ---------------------------------------------------------------------------- #

# With context manager way of writing in the file as we don't need to close the file
# Write mode (w) removes all the content and then adds new content
# Append mode (a) adds new content on old content
with open("testFile", "w") as f:
    f.write(testStr)

# Without context manager way of writing in the file
fp = open("testFile", "w")
fp.write(testStr)
fp.close()

# ---------------------------------------------------------------------------- #
#                                Reading a file                                #
# ---------------------------------------------------------------------------- #
with open("testFile", "r") as f:
    s = f.read()
    print(s)
