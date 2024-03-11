import paramiko


def ssh_connect(url, user, password):
    # 创建 SSHClient 对象
    ssh = paramiko.SSHClient()
    # 允许连接到没有知名主机密钥的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接到设备
    ssh.connect(url, user, password)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('ls')
    # 获取命令输出
    output = stdout.read().decode('utf-8')
    # 打印输出
    print(output)
    # 关闭 SSH 连接
    ssh.close()
