# PowerDNS Ansible playbook

Work in progress  
Change variables-example.yml to variables.yml before use. Also change passwords :)

Currently using a custom hacked role for pdns (https://github.com/PowerDNS/pdns-ansible/pull/61)  

```
cp variables-example.yml variables.yml
ansible-galaxy install -r requirements.yml
ansible-playbook main.yml -i hosts
```