import time
import serial
import clr

clr.AddReference('BrainLinkDualParser')

from BrainLinkDual import BrainLinkDualParser

def onSign(sign, battery):
    print('sign = ' + str(sign))

def onBrain(leftAtt, rightAtt, leftMed, rightMed):
    print('left attention = ' + str(leftAtt) + ' right attention = ' + str(rightAtt) + ' left meditation = ' + str(leftMed) + ' right meditation = ' + str(rightMed))

def onFrequency(left, right):
    print('left frequency = ' + ','.join([str(x) for x in left]) + ' right frequency = ' + ','.join([str(x) for x in right]))

def onEEG(left, right):
    print('left eeg = ' + ','.join([str(x) for x in left]) + ' right eeg = ' + ','.join([str(x) for x in right]))

def onRaw(left, right):
    print('left raw = ' + str(left) + ' right raw = ' + str(right))

parser = BrainLinkDualParser()
parser.mOnSignCallBack += onSign
parser.mOnBrainEventCallBack += onBrain
parser.mOnFrequencyCallBack += onFrequency
parser.mOnEEGEventCallBack += onEEG
parser.mOnRawDataCallBack += onRaw

ser = serial.Serial('com4', 115200)

try:
    while True:

        data = ser.read(512)
        
        for byte in data:
            parser.ParseByte(byte)

        time.sleep(0.1)

finally:
    ser.close()