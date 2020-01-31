#!/usr/bin/python3
import pexpect
import time
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('set', type=str)
parser.add_argument('switch_name', type=str)
parser.add_argument('switch_ip', type=str)
parser.add_argument('switch_password', type=str)
args = parser.parse_args()


if args.set == "set":
    try:
        child = pexpect.spawn('ssh -o GlobalKnownHostsFile=/dev/null -o UserKnownHostsFile=/dev/null -c 3des-cbc %s' % args.switch_ip)
        #child.logfile = sys.stdout.buffer  # uncomment to debug
        input = child.expect(['Are you sure you want to continue connecting (yes/no)?', 'Press any key to continue'])


        if input == 0:
            child.sendline('yes')
            child.sendline()
        elif input == 1:
            child.sendline()

        child.expect(args.switch_name)
        child.sendline('en')
        child.expect(args.switch_name)
        child.sendline('conf t')
        child.expect(args.switch_name)
        child.sendline('password all')
        child.expect('New password for operator:')
        child.sendline(args.switch_password)
        child.expect('Please retype new password for operator:')
        child.sendline(args.switch_password)
        child.expect('New password for manager:')
        child.sendline(args.switch_password)
        child.expect('Please retype new password for manager:')
        child.sendline(args.switch_password)
        child.expect(args.switch_name)
        child.sendline('write mem')
        child.expect(args.switch_name)
        child.sendline('exit')
        child.expect(args.switch_name)
        child.sendline('exit')
        child.expect(args.switch_name)
        child.sendline('exit')
        child.expect('Do you want to log out [y/n]?')
        child.sendline('Y')
        print('success')
    except Exception as e:
        msg = "Exception is:\n %s \n" % e
        print(msg)

elif args.set == "reset":
    try:
        child = pexpect.spawn('ssh -l manager -o GlobalKnownHostsFile=/dev/null -o UserKnownHostsFile=/dev/null -c 3des-cbc %s' % args.switch_ip)
        child.logfile = sys.stdout.buffer  # uncomment to debug
        input = child.expect(['Are you sure you want to continue connecting (yes/no)?'])

        if input == 0:
            child.sendline('yes')
        
        child.expect('password:')
        child.sendline(args.switch_password)
        child.sendline()
        child.expect(args.switch_name)
        child.sendline('en')
        child.expect(args.switch_name)
        child.sendline('conf t')
        child.expect(args.switch_name)
        child.sendline('no password all')
        child.expect('Password protection will be deleted, do you want to continue [y/n]?')
        child.sendline('y')
        child.expect(args.switch_name)
        child.sendline('exit')
        child.expect(args.switch_name)
        child.sendline('erase startup-config')
        child.expect("Configuration will be deleted and device rebooted, continue [y/n]?")
        child.sendline('y')
        child.expect('')
        child.close(force=True)
        time.sleep(5)
        print('success')
    except Exception as e:
        msg = "Exception is:\n %s \n" % e
        print(msg)

