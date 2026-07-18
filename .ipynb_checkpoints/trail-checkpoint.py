import cv2

# 1. Load your image or video frame
image = cv2.imread(r'C:\Users\DELL\Documents\Programming\Face mask detection\Howard LinkedIn post.jpg')

# 2. This command creates and launches the separate window application
cv2.imshow('Computer Vision Output', image)

# 3. CRITICAL: Keeps the separate window open until you press any key
cv2.waitKey(0) 

# 4. Cleans up and closes the window properlyd
cv2.destroyAllWindows()
