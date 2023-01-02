"""
Working with remote servers from Python using the 'paramiko' module.
Paramiko creates an ssh client that connect to the remote server.
We can also use it to transfer files to/from the remote server.
We can establish the connection with a) username + password b) username + cryptographic key
"""

"""
This needs:
	ssh-copy-id krys@to05xl.to.infn.it
so that my pub keys are in the authorized_keys of the remote server.

paramiko seems to have some issues that have not been resolved yet.
The RSA key sometimes is treated as a DSA key if key_filename is supplied instead of loading they key directly
and passing it as pkey. For this reason, avoid supplying the filename in the connect(...) command.
Load the key with paramiko.RSAKey/paramiko.DSSKey/etc and then supply it as pkey.
https://github.com/fabric/fabric/issues/2182
https://github.com/paramiko/paramiko/issues/1839
https://github.com/paramiko/paramiko/pull/1606
https://github.com/paramiko/paramiko/pull/1993
https://github.com/ktbyers/netmiko/issues/2827

Additionally, if using an RSA key on a server that does not support rsa-sha2-256/512, we need to disable them:
	disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']}  <-- add this to connect(...)
because paramiko uses the following algorithms in order of preference:
# ~= PubKeyAcceptedAlgorithms
	_preferred_pubkeys = (
		"ssh-ed25519",
		"ecdsa-sha2-nistp256",
		"ecdsa-sha2-nistp384",
		"ecdsa-sha2-nistp521",
		"rsa-sha2-512",
		"rsa-sha2-256",
		"ssh-rsa",
		"ssh-dss",
	)

Note that this is not in the same order as 'ssh -Q PubkeyAcceptedAlgorithms'.
Otherwise, we'll get an AuthenticationError.
https://www.paramiko.org/changelog.html#2.9.0
https://github.com/paramiko/paramiko/issues/1984
"""

# !/usr/bin/python

import paramiko
import os

# Ideally, we want to use ED25519
# key = paramiko.DSSKey.from_private_key_file(os.path.expanduser('~/.ssh/id_dsa'))  # DSA
key = paramiko.RSAKey.from_private_key_file(os.path.expanduser('~/.ssh/id_rsa'))  # RSA

sshclient = paramiko.SSHClient()
sshclient.load_system_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

sshclient.set_missing_host_key_policy(paramiko.WarningPolicy())  # What to do if connecting to an unknown server

# sshclient.connect(hostname="to05xl.to.infn.it", username="krys", look_for_keys=False, pkey=key)
sshclient.connect(hostname="to05xl.to.infn.it", username="krys", look_for_keys=False, pkey=key,
				  disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']})  # required if RSA

stdin, stdout, stderr = sshclient.exec_command('pwd')
remote_main_dir = stdout.readline().splitlines()[0]

stdin, remote_ls, stderr = sshclient.exec_command('ls')
print(remote_ls.readlines())

# Copy an item from remote server onto local
sftpclient = sshclient.open_sftp()

sftpclient.chdir(remote_main_dir)  # change dir on remote server
print(sftpclient.getcwd())

# copy from/to remote
sftpclient.get('const.m', os.path.expanduser('~/Desktop/const.m'))
# sftpclient.put(os.path.expanduser('~/Desktop/const.m'), 'const.m')

sftpclient.close()
sshclient.close()
