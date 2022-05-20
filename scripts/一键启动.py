from distutils.command.config import config
import subprocess
import time

# coins = [
#     "MASKUSDT",
#     "PEOPLEUSDT",
#     "ZILUSDT",
#     "HBARUSDT",
#     "1000SHIBUSDT",
#     "ZECUSDT",
#     "LRCUSDT",
#     "MATICUSDT",
#     "CTKUSDT",
#     "TRBUSDT",
#     "NKNUSDT",
#     "C98USDT",
#     "FLMUSDT",
#     "ZRXUSDT",
#     "CHZUSDT",
#     "LINAUSDT",
#     "HNTUSDT",
#     "GRTUSDT",
#     "BANDUSDT",
#     "SCUSDT"
#     ]

coins = ['MASKUSDT', 'PEOPLEUSDT', 'ZILUSDT', 'HBARUSDT', '1000SHIBUSDT', 'ZECUSDT', 'LRCUSDT', 'MATICUSDT', 'CTKUSDT', 'TRBUSDT', 'NKNUSDT', 'C98USDT', 'FLMUSDT', 'ZRXUSDT', 'CHZUSDT', 'LINAUSDT', 'HNTUSDT', 'GRTUSDT', 'BANDUSDT', 'SCUSDT', 'SXPUSDT', 'MANAUSDT', 'CHRUSDT', 'NEARUSDT', 'ANKRUSDT', 'CELRUSDT', 'DOGEUSDT', 'KNCUSDT', 'CRVUSDT', 'KAVAUSDT', 'ONEUSDT', 'COTIUSDT', 'STORJUSDT', 'CVCUSDT', 'ALICEUSDT', 'DENTUSDT', 'RVNUSDT', 'GTCUSDT']

config = "configs/live/recursive_grid_mode_auto_unstuck_enabled.example.json"#自动解套
# config = "configs\live\static_grid_mode_auto_unstuck_disabled.example.json"
acount = "binance_01"

for coin in coins:
    subprocess.Popen(
        rf'C:/py3810/python.exe passivbot.py {acount} {coin} {config}', 
        creationflags=subprocess.CREATE_NEW_CONSOLE,
        cwd=r"C:\\Users\\Administrator\\Desktop\\passivbot",
        shell= False
    )
    print(f"{coin} started...")
    # time.sleep(1)

print('Complete! All {} coins'.format(len(coins)))






