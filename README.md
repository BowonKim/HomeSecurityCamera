# HomeSecurityCamera

## Getting Started
This project is a home security camera that used raspberry pi zero.
It constantly record videos and the files will be stored in a flash drive. When the file is stored, it sends email notification.
It procides web live streaming and photographic function. You can find files with BST.py. 

### Prerequisites
* [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) - The OS for Raspberry pi
* [mjpg-streamer](https://github.com/jacksonliam/mjpg-streamer) - It create HTML pages to stream the video over your browser.


### Installing
Install mjpg streamer 
Excute sh mjpg.sh for live streaming. 
Edit the record.py to change the time how long you are going to record the video and change the email.
If you want to find a file excute the BST.py 


#### Installing_mjpg-streamer
download Raspbian to use Raspberry pi
To set up the camera type 

```
sudo apt-get update
sudo apt-get upgrade
sudo raspi-config
```
interfacing options > camera enable > select
Restart 
Type
```
git clone https://github.com/jacksonliam/mjpg-streamer.git
```
installing the mjpg-streamer package 
type
```
cd mjpg-streamer
ls  # check the current directory
cd mjpg-streamer-exprimental/

sudo apt-get install cmake
sudp apt-get libjpeg-dev

make-CMAKE-BUILD_TYPE=Debug
sudo make install


sudo nano mjpg.sh

export STREMAER_PATH-$HOME/jmpg/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRART_PATH=$STREAMER_PATH
$STERAMER_PATH/mjpg_streamer -i "input_raspicam.so" -o "output_http.so -p 8091 -w $STREAMER_PATH/www"

sh mjpg.sh
```
