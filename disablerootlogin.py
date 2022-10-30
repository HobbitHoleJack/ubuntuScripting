def disablerootlogin():
  # Read file in read mode 'r'
  with open('/etc/ssh/sshd_config', 'r') as file:
    content = file.read()
  # Replace string
  content = content.replace('PermitRootLogin yes', 'PermitRootLogin no')
  # Write new content in write mode 'w'
  with open('/etc/ssh/sshd_config', 'w') as file:
    file.write(content)
