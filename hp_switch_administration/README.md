This folder contains a script to set password/reset configuration on HP ProCurve switches over SSH.

The script requires the following arguments.

todo: Either set or reset, depending on if you want to set or reset the password 
switch_name: Name of the switch, as it appears in the CLI on your switch.
switch_ip: Managment IP of your switch.
switch_password: The password you want to set, or the one you have set previously.

example: python3 set_passwd_switches.py set Switch1 10.13.37.11 Awesomesauce

