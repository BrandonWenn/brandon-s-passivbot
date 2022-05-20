# -*- coding: UTF-8 -*-
import subprocess

from sklearn.preprocessing import OneHotEncoder

config_path = r"configs\live\recursive_grid_mode_auto_unstuck_enabled.example.json"
# config_path = r"configs\live\static_grid_mode_auto_unstuck_enabled.example.json"
coins = r"-s C98USDT"
user = r"--user binance_01"
startdate_and_enddate = r"--start_date 2022-04-14 --end_date 2022-05-14"
oh = ""

running_cwd = r"C:\Users\Administrator\Desktop\passivbot"


with open("回测.bat","w+") as bk:
    bk.writelines(rf"C:\py3810\python.exe backtest.py {coins} {user} {startdate_and_enddate} {config_path}"+'\n'+'pause')

def excute_bat_file():
    subprocess.Popen(
        rf"C:\Users\Administrator\Desktop\passivbot\回测.bat",
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        cwd = running_cwd,
        )

if __name__ == "__main__":
    excute_bat_file()

