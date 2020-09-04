import cv2


img = cv2.imread('image.jpg')
# convert image to grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert the grayscale image to binary image
ret,thresh = cv2.threshold(gray_image,42, 255, cv2.THRESH_BINARY_INV)

# cv2.imshow("Image_1", thresh)

# calculate moments of binary image
M = cv2.moments(thresh)

print('M   ',M)

for x in M:
	print(x,':',M.get(x))

# calculate x,y coordinate of center
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

print(cX,cY)

# put text and highlight the center
cv2.circle(thresh, (cX, cY), 5, (50, 255, 250), -1)
# cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# out_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# display the image
cv2.imshow("Image", thresh)
cv2.waitKey(0)