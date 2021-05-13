import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_nats_conf_is_file(host):
    assert host.file("/etc/nats/nats-server.conf").is_file
