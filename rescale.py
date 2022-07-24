import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img )

def rescaleFrame(frame, scale=0.75):
    # scale the frame down to 80%
    width = int(frame.shape[1] * scale)    # width = frame.shape[1] * 0.75 (or 0.8)
    height = int(frame.shape[0] * scale)  # height = frame.shape[0] * 0.75 (or 0.8)
    dim = (width, height) 
    # resize the frame
    resizedFrame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)    # INTER_AREA is the default
    return resizedFrame

# # Reading Videos
# capture = cv.VideoCapture('Videos/dog.mp4')

resized_image = rescaleFrame(img, 0.5)
cv.imshow() = ('image', resized_image)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.75)
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        cv.imshow('Video Resized', frame_resized)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()

cv.waitkey