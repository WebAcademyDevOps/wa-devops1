import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_nats_service_is_masked(host):
    assert host.service("nats-server").is_masked == False

def test_nats_service_is_enabled(host):
    assert host.service("nats-server.service").is_enabled

def test_nats_service_is_running(host):
    assert host.service("nats-server").is_running
