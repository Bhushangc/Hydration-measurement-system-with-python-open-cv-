import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def stop_program():
        exit()

def main():
        intro.quit()

        root = tk.Tk()
        root.withdraw()  

        file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg *.png *.bmp *.jpeg")])

        # Check if the user selected a file
        if file_path:
        # Read the selected image using OpenCV
                image = cv2.imread(file_path)

        # Check if the image was successfully loaded
                if image is not None:

                        dimensions = image.shape 
                        h, w=dimensions[0], dimensions[1]  
                        cx = int(w/2)
                        cy = int(h/2)

                        #applying thresholding
                        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        _, thresholded_image = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY)
                        bgr_image = cv2.cvtColor(thresholded_image, cv2.COLOR_GRAY2BGR)

                        #convert image to hsv format and get h value of image
                        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
                        pixel_centre = hsv[cx,cy]
                        h_value = int(pixel_centre[0] *360/180)
                        s_value = int(pixel_centre[1] *100/256)


                        #detect the color of image and give hydration level based on the color

                        if 58<h_value<80:
                                hydration = 'good'
                                suggestion = 'You are properly hydrated.'
                                print (hydration)
                        elif 51<h_value<59:
                                hydration = 'fair'
                                suggestion = 'Start drinking a bit more water.'
                                print (hydration)
                        elif 34<h_value<52:
                                hydration = 'dehydrated'
                                suggestion = 'Drink more water.'
                                print (hydration)
                        elif 24<h_value<35:
                                hydration = 'very dehydrated'
                                suggestion = 'You nned to drink lot more water and consider taking rehydration sachets.'
                                print (hydration)
                        elif 7<h_value<25:
                                hydration = 'severely dehydrated'
                                suggestion = 'You should take rehydration sachets and seek professional help.'
                                print (hydration)
                        else:
                                hydration = "error"
                                suggestion = 'Please take another picture and try again.'
                        print (hydration)
                        
                        result = tk.Tk()
                        result.title('Result')
                        result.geometry("500x150")
                        final = tk.Label(result,text="Your hydration level is:" + hydration)
                        final.pack()
                        suggest = tk.Label(result,text="Suggestion:" + suggestion)
                        suggest.pack()
                        test_again = tk.Button(result,text='Test again',command=main)
                        test_again.pack(padx=10,pady=10)
                        exit = tk.Button(result,text='Exit',command=stop_program)
                        exit.pack(padx=10,pady=10)
                        result.mainloop()

                else:
                        print("Error: Unable to read the selected image.")
        else:
                print("No file selected.")

        
        root.quit()

intro = tk.Tk()
intro.title('Welcome')
title = tk.Label(intro,text="Hydration Level Detection System",font=('Helvatical bold',30))
title.pack(padx=10,pady=10)
content = tk.Label(intro,text="Welcome to Hydration Lable Detection System. Please take a good picture of your urine and insert your image to see the reasults.",)
content.pack(padx=10,pady=10)
intro.geometry("800x200")
button = tk.Button(intro,text='Insert Image',command= main)
button.pack(padx=10,pady=10)
intro.mainloop()



        

        
       


