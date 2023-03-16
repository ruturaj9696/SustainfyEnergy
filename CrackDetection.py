import cv2


# img = cv2.imread('crack3.png')
img = cv2.imread('processed.jpg')
# img = cv2.imread('panel.jpg')

# Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Applying blur to remove the noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny to detect the edges
edges = cv2.Canny(blur, 50, 150)
cv2.imwrite("canny.jpg",edges)

# Apply the dilation and erosion to the image to fill the gaps
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("Closed",closed)
cv2.imwrite('closed.jpg',closed)

# Finding the contors
contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw rectangles around detected cracks
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # cv2.line(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Display the result
cv2.imwrite('Result.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
