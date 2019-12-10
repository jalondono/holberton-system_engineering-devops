# added lines to ssh confif
file_line { 'addLines':
  ensure => present,
  path   => 'etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  line   => 'IdentityFile ~/.ssh/holberton'
}
