#coding:utf-8
import cv2
import numpy as np
 

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,320)

flag = 1;

def video_capture0():
  return cap
