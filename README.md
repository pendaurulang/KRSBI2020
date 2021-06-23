# KRSBI2020
## duino/colorconf/colorconf.ino (for Arduino)
## main.py (for Raspi)


gunakan perintah `screen /dev/ttyACM0 9600` , untuk ganti serial monitor `ctrl+a lalu k untuk keluar screen`

01/09/2020 11:44 ---
memodulkan perintah kondisi1 🗹

01/09/2020 12:50 ---
memodulkan perintah test(kendalipwm) 🗹

## Final Version ---

### Requirement 
#### Raspberry pi

### Clone Repository and Enter directory
```
git clone https://github.com/pendaurulang/KRSBI2020.git
cd KRSBI2020/
pip install -r requirement.txt
```
### Upload Arduino Sketch
open `duino/test_modul_r1` directory and open `test_modul_r1.ino` with arduino IDE and upload it

### run python script
open terminal/shell on current folder an run this
```
python3 main.py
```
run monitoring arduino with
```
screen /dev/ttyACM0 9600
```
or
```
screen /dev/ttyACM1 9600
```