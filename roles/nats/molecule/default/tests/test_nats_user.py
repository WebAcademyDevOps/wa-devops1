import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_nats_user_exists(host):
    assert host.user("nats").exists
    assert host.user("nats").group == "nats"
    assert host.user("nats").shell == "/usr/sbin/nologin"
