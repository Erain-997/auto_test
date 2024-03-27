from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.settings import Settings


def connect_devices_ip(name, ip):
    import datetime
    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + "/log/report_" + name + f"_{current_time}"
    if not cli_setup():
        auto_setup(__file__, compress=False, logdir=path,
                   devices=["Android://127.0.0.1:5037/" + ip + ":5555", ])

    poco = AndroidUiautomationPoco()
    wake()
    home()

    Settings.LOG_FILE = False

    # 设置日志级别为 WARNING
    # set_log_level(logging.WARNING)
    return path, poco


# if __name__ == '__main__':
#     name="设备语言"
#     report_dir, poco = connect_devices_ip(name, "192.168.57.199")
#     pos = poco(text="呼叫")
#     snapshot(filename=report_dir + "/{}.png".format(name), quality=99)
