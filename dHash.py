from PIL import Image, ImageTk
import cv2
import numpy as np
import os
import PySimpleGUI as sg

location = ""

def compImg(img1, img2):
    image = Image.open(img1)
    image = image.resize((9, 8))
    file1 = 'tempImg1.png'
    image.save(file1)
    grImg = cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
    hash1 = hashImg(grImg)
    
    image2 = Image.open(img2)
    image2 = image2.resize((9, 8))
    file2 = 'tempImg2.png'
    image2.save(file2)
    grImg2 = cv2.imread(file2, cv2.IMREAD_GRAYSCALE)
    hash2 = hashImg(grImg2)
    
    diff = hammingDist(hash1, hash2)
    
    location = os.getcwd()
    
    os.remove(os.path.join(location, file1))
    os.remove(os.path.join(location, file2))
    
    return "The images are {}% different".format((100/64) * diff)
    
def binToHex(binNum):
    hashHex = ''
    for i in range(16):
        sum = 0
        subStr = binNum[(4*i):((4*i)+4)]
        count = 3
        for j in subStr:
            sum += int(j) * (2 ** count)
            count -= 1
            
        if (sum < 10):
            hashHex += chr(sum + 48)
        else:
            hashHex += chr(sum + 55)
            
    return hashHex

def hashImg(imag):
    hash1 = ''
    hashHex = ''

    for i in range(8):
        for j in range(8):
            if (imag[i][j] < imag[i][j + 1]):
                hash1 += '1'
            else:
                hash1 += '0'
                
    #hashHex = binToHex(hash1)
    return hash1

def hammingDist(num1, num2):
    count = 0
    for i in range(64):
        if (num1[i] != num2[i]):
            count += 1
        else:
            continue
    
    return count


sg.theme('DarkPurple1')

filesColumn = [
    [
        sg.Text('Image file: '),
        sg.In(size=(25, 1), enable_events = True, key = "-FILE1-"),
        sg.FileBrowse()
    ],
    [
        sg.Text('Image file: '),
        sg.In(size = (25, 1), enable_events = True, key = "-FILE2-"),
        sg.FileBrowse()
    ],
    [
        sg.Button("Compare", size = (10, 1), key = "_BUTT_")
    ]
]

imageColumn = [
    [
        sg.Image(size = (300, 500), key = "-IMAGE1-"),
        sg.Image(size = (300, 500), key = "-IMAGE2-"),
    ],
    [
        sg.Text(font = ("Helvetica", 16),key = "-OUTPUT-") 
    ]
]

layout = [
    [
        sg.Column(filesColumn, element_justification='center'),
        sg.VSeperator(), 
        sg.Column(imageColumn, element_justification='center')
    ]    
]

window = sg.Window("dHash", layout)

img1 = ''
img2 = ''

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    
    if event == "-FILE1-":
        img1 = values["-FILE1-"]
        temp1 = Image.open(img1)
        temp1 = temp1.resize((360, 640))
        imaegeee = ImageTk.PhotoImage(image = temp1)
        window["-IMAGE1-"].update(data = imaegeee)
    elif event == "-FILE2-":
        img2 = values["-FILE2-"]
        temp = Image.open(img2)
        temp = temp.resize((360, 640))
        outImg2 = ImageTk.PhotoImage(image = temp)
        window["-IMAGE2-"].update(data = outImg2)
    elif event == "_BUTT_":
        txt = compImg(img1, img2)
        window["-OUTPUT-"].update(txt)
        
window.close()
#os.remove(os.path.join(location, "imageeee1.png"))
    
#image = Image.open("D:\doonloods\insto\pung.png").convert('L')
#image = image.resize((9, 8))
#image.save('testPung.png')

#img1 = "D:\doonloods\insto\pung.png"
#img2 = "D:\doonloods\insto\IMG_6680.jpg"
#image = Image.open(img1)
#image = image.resize((9, 8))
#image.save('res.png')
#grImg = cv2.imread('res.png', cv2.IMREAD_GRAYSCALE)
#image.save('testPung.png')

#hash1 = ''
#hashHex = ''

#for i in range(8):
#    for j in range(8):
#        if (grImg[i][j] < grImg[i][j + 1]):
#            hash1 += '1'
#        else:
#            hash1 += '0'
            
#hashHex = binToHex(hash1)

#img1 = input("Enter absolute path of first image: ")
#img2 = input("Enter absolute path of second image: ")

#compImg(img1, img2)
