import socket
import subprocess
import re
import os
import allure
from log import log_info


def get_local_ip():
    try:
        # 获取本地主机名
        host_name = socket.gethostname()
        # 获取本地 IP 地址
        local_ip = socket.gethostbyname(host_name)
        return local_ip
    except socket.error:
        return None


def find_available_port():
    # 创建一个 TCP 套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 0))  # 绑定到任意可用地址和端口
    # 获取绑定后的套接字信息
    _, port = sock.getsockname()
    # 关闭套接字
    sock.close()
    return port


def generate_report():
    try:
        # 生成Allure报告
        cmd = "allure generate ./allure-results -o ./reports --clean"
        os.popen(cmd)
    except subprocess.CalledProcessError as e:
        log_info("报告生成失败：" + str(e))


def get_report_url():
    report_url = ""
    ip = get_local_ip()
    port = find_available_port()
    log_info("本机ip: ", ip, port)
    open_cmd = "allure open -h " + ip + " -p " + str(port) + " ./reports"
    # open_cmd = "allure open -h 100.111.222.14 -p 4001 ./reports"
    # 使用 subprocess 执行命令并获取输出
    process = subprocess.Popen(open_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # 逐行读取命令的实时输出
    while process.poll() is None:
        output = process.stdout.readline()
        if output:
            log_info(output.decode("utf-8").strip())
            url_pattern = r"<(http://[^/]+)/>"
            match = re.search(url_pattern, output.decode("utf-8").strip())
            if match:
                report_url = match.group(1)
                break
    process.terminate()
    return report_url


def case_name(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with allure.step(name):
                log_info(name)
                return func(*args, **kwargs)

        return wrapper

    return decorator
