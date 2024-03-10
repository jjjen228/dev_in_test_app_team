import subprocess

def get_device_udid():
    result = subprocess.run(["adb", "devices"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    
    if len(lines) >= 2:
        first_device_line = lines[1]
        device_udid = first_device_line.split('\t')[0]
        return device_udid
    else:
        print("Нет подключенных устройств.")
        return None
    
def adb_command(command):
    result = subprocess.run(["adb", "shell"] + command.split(), stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def android_get_desired_capabilities():
    udid = get_device_udid()
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '14',
        'deviceName': udid if udid else 'error',
        # 'deviceName': '25311JEGR01509',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
