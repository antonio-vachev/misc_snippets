import os

# Set the _source in between the " " characters
_source = r" "

# Set the file extension to be searched for
_extension = ".JPG"
_extension_lowercase = ".jpg"

for i, filename in enumerate(os.listdir(_source)):
    if filename.endswith(_extension) or filename.endswith(_extension_lowercase):

        # Set the naming convention input between the " " characters
        os.rename(_source + filename, _source + r" " + str(i+1).zfill(4) + _extension)