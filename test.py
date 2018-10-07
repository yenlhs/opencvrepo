import cv2
import boto3
import time

bucketname = 'yenlhs'

client = boto3.client('s3')
# client.put_object(Body=more_binary_data, Bucket=yenlhs)

vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()
count = 0
success = True
while success:
  time.sleep(10)
  cv2.imwrite("frame/frame%d.jpg" % count, image)     # save frame as JPEG file
  
  # client.put_object(Body=x, Bucket=bucketname, Key=None)
#   client.put_object(Body=, Bucket=yenlhs)
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1



