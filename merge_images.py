# First install PIL
# c:\python27\scripts> pip install Pillow

# Usage:
# merge_images.py input1.jpg input2.jpy input3.jpy output.jpg

import sys
from PIL import Image

input_files = sys.argv[1:-1]
output_file = sys.argv[-1]
print 'Merging files %s into output file %s' % (','.join(input_files), output_file)

# Width of new image is max of the input widths, while height is the sum of the heights.
input_images = [Image.open(x) for x in input_files]
new_image = Image.new("RGB", (max([x.size[0] for x in input_images]), sum([x.size[1] for x in input_images])))

yy = 0
for input_image in input_images:
    new_image.paste(input_image, (0, yy))
    yy = yy + input_image.size[1]

new_image.save(output_file)
