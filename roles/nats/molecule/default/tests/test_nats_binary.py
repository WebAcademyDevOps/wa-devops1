import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_nats_binary_exists(host):
    assert host.file("/usr/local/bin/nats-server").exists

def test_nats_binary_exec(host):
    assert host.file("/usr/local/bin/nats-server").mode == 0o775

def test_nats_binary_version(host):
    cmd = host.run("nats-server --version")
    assert 'v2.2.2' in cmd.stdout

def test_nats_package_is_installed(host):
    assert host.package("nats-server").is_installed
