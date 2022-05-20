import json
import subprocess
from time import time,sleep
import hjson

#基础信息
not_visialable = False
config = r'configs\live\recursive_grid_mode_auto_unstuck_enabled.example.json'
coins = [
    # "MASKUSDT",
    # "ZILUSDT",
    # "HBARUSDT",
    # "CTKUSDT",
    # "ETRBUSDT",
    # "NKNUSDT",
    "C98USDT",
    # "EOSUSDT"
    ]
start_date = '2022-04-01'
end_date =  '2022-04-30'
running_cwd = r"C:\Users\Administrator\Desktop\passivbot"
default_hjson_path = r'C:\Users\Administrator\Desktop\passivbot\configs\backtest\default.hjson'

#更新default.hjson信息
def update_file(coin):
    try:
        dict={}
        def get_hjson_data(default_hjson_path):
            with open(default_hjson_path,'rb') as f:
                backtest_hjson = hjson.load(f)
                backtest_hjson['symbol'] = coin
                backtest_hjson['start_date'] = start_date
                backtest_hjson['end_date'] =  end_date
                dict = backtest_hjson
            f.close()
            return dict
        def write_hjson_data(dict):
            with open(default_hjson_path,'w') as r:
                hjson.dump(dict,r)  
            r.close()

        the_revised_dict = get_hjson_data(default_hjson_path)
        write_hjson_data(the_revised_dict)

        print("update file successfully")
    except:
        print("something wrong with update file")

# 用default.hjson执行回测
def one_click_run_backtestting():
    try:
        subprocess.Popen(
            rf'C:\py3810\python.exe backtest.py {config}', 
            creationflags=subprocess.CREATE_NEW_CONSOLE,
            cwd = running_cwd,
            shell=False
            )
        print("running backtest seccessfully ")
    except:
        print("fail to run One Click Backtest")
    
    
if __name__ == "__main__":
    for sequance in range(len(coins)):
        update_file(coin=coins[sequance])
        one_click_run_backtestting()
        # sleep(10)

