from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

im = Image.save("moon.tif")
# im.show()
print(im.size)
# im = im.filter(ImageFilter.DETAIL)

edge_detect = np.array([[0,-1,0],
                          [-1, 4,-1],
                          [0,-1,0]])

kernel_moon = im.filter(ImageFilter.Kernel(size=(3,3), kernel=edge_detect.flatten(),scale=0.2))
# kernel_moon.show()
kernel_moon.save("kernel_moon.tif")

# kernel_moon = kernel_moon / 255

im1 = np.array(Image.open("moon.tif"))
im2 = np.array(Image.open("kernel_moon.tif").resize(im1.shape[1::-1], Image.BILINEAR))

fig = plt.figure()
a = fig.add_subplot(1, 2, 1)
#imgplot = plt.imshow(im1)
a.set
plt.imshow(im1, 'gray')
plt.savefig('im0.png')
plt.hist(im1)
plt.savefig('im1Hist.png')
plt.imshow(im2, 'gray')
plt.savefig('im2.png')
plt.hist(im2)
plt.savefig('im2Hist.png')


print(im1.dtype)

dst = im1 * 0.5 + im2 * 0.5
plt.imshow(dst, 'gray')
plt.savefig('dst.png')
plt.hist(dst)
plt.savefig('dstHist.png')
print(dst.dtype)
# float64

# Image.fromarray(dst.astype(np.uint8)).show()

