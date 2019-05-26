
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']
version = '0.4.0'


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_install_dir(host):
    f = host.file('/opt/alertmanager_bot')

    assert f.exists
    assert f.is_directory


def test_release_dir(host):
    f = host.file('/opt/alertmanager_bot/releases/' + version)

    assert f.exists
    assert f.is_directory


def test_release_symlink_dir(host):
    f = host.file('/opt/alertmanager_bot/current')

    assert f.exists
    assert f.is_symlink
    assert f.linked_to == '/opt/alertmanager_bot/releases/' + version


def test_service(host):
    s = host.service('alertmanager_bot')

    assert s.is_enabled
    # assert s.is_running


def test_user(host):
    u = host.user('am-bot')

    assert u.shell == '/usr/sbin/nologin'


def test_group(host):
    g = host.user('am-bot')

    assert g.exists
