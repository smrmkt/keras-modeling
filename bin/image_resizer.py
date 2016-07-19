import os
from PIL import Image

size = 64, 64
data_path = '../data/images'
in_path = os.path.join(data_path, 'original')
out_path = os.path.join(data_path, 'resized')

in_files = os.listdir(in_path)

for in_file in in_files:
    out_file = os.path.join(out_path, in_file)
    if in_file != out_file:
        try:
            im = Image.open(os.path.join(in_path, in_file))
            im = im.resize(size, Image.ANTIALIAS)
            im.save(out_file, 'JPEG', quality=100, optimize=True)
        except IOError:
            print "cannot create thumbnail for '%s'" % in_file

