# PowerDNS Ansible Playbook

Work in progress  

This will setup MariaDB and PowerDNS 4.2. Using PowerDNS-Admin for webinterface. No bootstrapping done yet.  
First user created in PowerDNS-Admin is full admin.

Copy variables-example.yml to variables.yml before use. Change passwords before use :)  

Using this PR https://github.com/PowerDNS/pdns-ansible/pull/61 to get PDNS 4.2

```
cp variables-example.yml variables.yml
ansible-galaxy install -r requirements.yml
ansible-playbook main.yml -i hosts-example
```