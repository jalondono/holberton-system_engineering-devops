exec { 'killmenow':
provider => 'shell',
command  => 'pkill killmenow'
}