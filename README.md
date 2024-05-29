# database_finalHW
112-2 資料庫期末作業
使用HeisiSQL的資料庫管理工具
## Server Tier 架設說明
1. 先於mariaDB的官網下載並安裝
2. 開啟HeidiSQL或MySQL，於左下角新增一個工作階段，右方參數設定完成後開啟。
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/31e0233e-5c8c-4da1-b2b1-86a8e886f74a)
   ```bash=
   host="0.tcp.jp.ngrok.io",
   port=15305, user="411062002",
   password="411062002",
   database="411062002"
   ```
3.可於HeisiSQL輸入DML (Data Manipulation Language)、DDL (Data Definition Language)操作

## Client Tier 連線說明
1.進入虛擬環境
```bash=
new_env\Scripts\activate
```
離開:
```bash=
deactivate
```
2. 輸入
```bash=
pip3 install mysql.connector mariadb (或pip install mysql.connector mariadb
```
4. 
