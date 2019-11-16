# purple and white by Pasha

Purple is my favourite color <br>



<br><b>Please explore and even read carefully ALL the configuration files.</b>

<h2>Features</h2>
<h4>Gmail checker</h4>
You need to enter your login and password in the `pygmail.py` and modify gmail.conf file to see number of income emails

<h4>System monitoring</h4>
You will know everything about your computer without any commands - all information will bo on your desktop
(My main disk is /dev/sdb8, if you want to see write/read of disk, change /dev/sdb8 in disk_graph.conf)

<h4>Development and integration</h4>
You can change and add everything you want, scripts on any languages and it will be very easy

<h2>Installation</h2>

1) install conky-cairo<br>
in ArchLinux from AUR via a command:<br>
~~~~
yaourt -S conky-cairo
~~~~
2) clone this repo from git:
~~~~
git clone https://github.com/Myralllka/blood-and-milk.git ~/blood-and-milk
~~~~
3) move into the directory and make app executable:
~~~~
cd ~/blood-and-milk; sudo chmod +x Application.sh
~~~~
and than you need only to start the app
~~~~
./Application.sh
~~~~

<h2>Contribution</h2>
If you want to modify this files:<br>
1) fork it<br>
2) create new directory inside<br>
3) modify that directory as you want<br>
4) make pull request<br>
<hr>
if you want to understand in which way each file works, you can do:

~~~~
conky -c /file_to_start
~~~~

<b>I recommend to do this with every file and modify them one by one</b>

[Here](http://conky.sourceforge.net/variables.html) you can find information about conky objects and how to work with them

![screenshot](https://github.com/Myralllka/blood-and-milk/blob/master/Screenshot%20from%202019-02-27%2013-10-52.png)
