# first script to setup hosts
# uncomment inventory to create the vm
ansible-playbook -i inventories/seapath_cluster_definition_example_matias.yml playbooks/deploy_vms_cluster.yaml -vvv
