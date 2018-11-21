
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_binary(host):
    f = host.file('/opt/alertmanager_bot/current/alertmanager_bot')

    assert f.exists


def test_socket(host):
    s = host.socket('tcp://127.0.0.1:8080')
    print(host.socket.get_listening_sockets())

    assert s.is_listening


def test_serice(host):
    s = host.service('alertmanager_bot')

    assert s.is_enabled
    assert s.is_running
