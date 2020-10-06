import pdfkit
import connect as co
import voice_to_text as voice_data
from pdf2image import convert_from_path as cvt
from matplotlib import pyplot as plt
import cv2
import urllib.request
i = 1
txt = co.searching("power")


def change_to_jpeg(data):
    pdfkit.from_url(data, 'webimages/generated%0i.pdf' % i)


"""
 images = cvt("generated.pdf")
    images[0].save("output.jpeg", "JPEG")
    frame, ig = cv2.imread("output.jpeg")
    if frame:
        cv2.imwrite("output" + str(count) + "jpeg", ig)
    return frame
#    cv2.waitKey(0)
    # image_contor()


# def image_contor():
    #    ig = cv2.imread("output.jpeg")

#    cv2.imshow("output", ig)
#    cv2.waitKey(0)


# t hresh = cv2.adaptiveThreshold(ig, 255, cv2.
#                               ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# print(list)
"""
print(txt)
for data in txt:
    print(data)
    change_to_jpeg(data)
    i = i + 1
