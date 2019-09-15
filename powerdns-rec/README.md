# PowerDNS Recursor Ansible Playbook

Work in progress  

This will setup PowerDNS Recursor 4.2. Using PowerDNS-Admin for webinterface. No bootstrapping done yet.  


Copy variables-example.yml to variables.yml before use. Change passwords before use :)  

Using a custom role for PowerDNS Recursor to get 4.2, PR to get this upstream will be created

```
cp variables-example.yml variables.yml
ansible-galaxy install -r requirements.yml
ansible-playbook main.yml -i hosts-example
```