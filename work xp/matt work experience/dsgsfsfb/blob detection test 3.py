import cv2

b = cv2.SimpleBlobDetector()

  #set parameter
if GetValue('Blob_Detection.blob_color') == 0:
    b.setInt('blobColor',0)
else:
    b.setInt('blobColor',255)
    b.setDouble('maxArea',GetValue('Blob_Detection.maxArea'))
    b.setDouble('maxCircularity',GetValue('Blob_Detection.maxCircularity'))
    b.setDouble('maxConvexity',GetValue('Blob_Detection.maxConvexity'))
    b.setDouble('maxInertiaRatio',GetValue('Blob_Detection.maxInertiaRatio'))
    b.setDouble('maxThreshold',GetValue('Blob_Detection.maxThreshold'))
    b.setDouble('minDistBetweenBlobs',GetValue('Blob_Detection.minDistbetweenBlobs'))
    b.setDouble('minRepeatability',GetValue('Blob_Detection.minRepeatability'))
    b.setDouble('minThreshold',GetValue('Blob_Detection.minThreshold'))
    b.setDouble('thresholdStep',GetValue('Blob_Detection.thresholdStep'))
blob = b.detect(img)
