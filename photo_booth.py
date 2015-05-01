import time, os, subprocess

x = lambda z: subprocess.call(z, shell=True)
while True:
  choice = raw_input("> Press 'b' and enter")
  if choice == 'b':
    snap = 0
    while snap < 4:
      gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename /home/pi/photobooth_images/photobooth%d%H%M%S.jpg", stderr=subprocess.STDOUT, shell=True)
      print(gpout)
      if "ERROR" not in gpout: 
        snap += 1
      time.sleep(0.5)
    x("mogrify -resize 968x648 /home/pi/photobooth_images/*.jpg")
    x("montage /home/pi/photobooth_images/*.jpg -tile 2x2 -geometry +10+10 /home/pi/temp_montage2.jpg")
    x("montage /home/pi/temp_montage2.jpg /home/pi/photobooth_label.jpg -tile 2x1 -geometry +5+5 /home/pi/temp_montage3.jpg")
    #x("lp -d Canon_CP900 /home/pi/temp_montage3.jpg")
    x("cp /home/pi/temp_montage3.jpg /home/pi/PB_archive/PB_%d%H%M%S.jpg")
    #x("rm /home/pi/photobooth_images/*.jpg")
    x("rm /home/pi/temp*")
