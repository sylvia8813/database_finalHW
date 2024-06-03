# database_finalHW
112-2 資料庫期末作業
使用HeisiSQL的資料庫管理工具
## Server Tier 架設說明
1. 先於mariaDB的官網下載並安裝
2. 啟動MySQL server後，開啟HeidiSQL或MySQL，於左下角新增一個工作階段，右方參數設定完成後開啟。
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
2.輸入
```bash=
pip3 install mysql.connector mariadb (或pip install mysql.connector mariadb
```
## ER-Model
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/251c6042-d76c-4aaf-8bf0-60d0867030e5)

## Relation Schema
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/e6c83339-4d2f-4f79-aa7a-bc2a2c52b34b)


## Tables 內容說明
| Vehicle           |           |               |           |             |            |      |
|-------------------|-----------|---------------|-----------|-------------|------------|------|
| vin               | information_id | manufactor_id | dealer_id | import_date | salesprice | sold |
| ABC12345678901234 | 1         | 1             | 1         | 2023/1/5    | 1000000    | yes  |
| DEF23456789012345 | 1         | 2             | 2         | 2022/9/15   | 1200000    | no   |
| GHI21367890123456 | 2         | 3             | 3         | 2023/3/25   | 1100000    | no   |
| HIJ56789012345678 | 3         | 4             | 4         | 2023/5/1    | 1200000    | yes  |
| GHI34567890123456 | 4         | 5             | 5         | 2024/4/19   | 1500000    | yes  |
| IJK67890123456789 | 5         | 6             | 6         | 2024/8/13   | 2000000    | yes  |

| Information       |               |         |       |                  |                |      |
|-------------------|---------------|---------|-------|------------------|----------------|------|
| information_id         | model_id    | style   | color | engine           | transmiscion   | sold |
| 1                 | BZNZ-0302S-1    | 4 doors | black | 1.0L TSI         | 6-Speed Manual | yes  |
| 2                 | BZNZ-0303 | SUV     | white | 2.0L Turbo       | 9G-TRONIC      | no   |
| 3                 | MVE-ST72          | 4 doors | gray  | 1.4L TFSI        | S-Tronic       | no   |
| 4                 | DAF-FT3605DKZ | 4 doors | black | 2.0L Turbo       | 9G-TRONIC      | yes  |
| 5                 | MAN-11.190HOCL-1 | SUV     | black | 3.0L V6 Bi-Turbo | 9G-TRONIC      | yes  |

| Part    |                        |                 |               |            |                   |
|---------|------------------------|-----------------|---------------|------------|-------------------|
| part_id | part_name              | manufactor_date | manufactor_id | factory_id | vin               |
| 1       | Brake line             | 2022/12/30      | 1             | NULL       | ABC12345678901234 |
| 2       | Brake line             | 2023/7/19       | NULL          | 1          | DEF23456789012345 |
| 3       | Air filter             | 2023/8/17       | NULL          | 2          | GHI34567890123456 |
| 4       | spark plug line        | 2022/3/14       | 2             | NULL       | HIJ56789012345678 |
| 5       | transmission | 2023/2/27       | 3             | NULL       | GHI34567890123456 |

| Sales             |             |            |
|-------------------|-------------|------------|
| vin               | customer_id | sold_date  |
| ABC12345678901234 | 762         | 2023/7/24  |
| HIJ56789012345678 | 504         | 2023/8/14  |
| GHI34567890123456 | 321         | 2023/12/21 |
| IJK67890123456789 | 245         | 2023/4/15  |

| Customer    	|        	|        	|              	|                         	|               	|
|-------------	|--------	|--------	|--------------	|-------------------------	|---------------	|
| customer_id 	| name   	| gender 	| phone        	| address                 	| annual_income 	|
| 762         	| 王小明 	| male   	| 0912-345-678 	| 台北市信義區松高路123號 	| 550000        	|
| 504         	| 陳美玲 	| female 	| 0921-234-567 	| 屏東縣屏東市民權路666號 	| 600000        	|
| 321         	| 黃小菁 	| female 	| 0933-456-789 	| 台中市南屯區            	| 740000        	|
| 245         	| 盧婷婷 	| female 	| 0944-567-890 	| 嘉義縣朴子市中華路555號 	| 590000        	|
| 777         	| 周志明 	| male   	| 0911-234-567 	| 花蓮縣花蓮市中山路707號 	| 880000        	|

| Dealer    	|                    	|              	|
|-----------	|--------------------	|--------------	|
| dealer_id 	| dealer_name        	| phone        	|
| 1         	| 台灣汽車經銷商     	| 02-1234-5678 	|
| 2         	| 台北汽車經銷商     	| 02-2345-6789 	|
| 3         	| 台中汽車製造經銷商 	| 02-0123-4567 	|
| 4         	| 桃園車業經銷商     	| 02-4567-8901 	|
| 5         	| 新北汽車工業經銷商 	| 02-9012-3456 	|

| Manufactor    	|                  	|                     	|            	|
|---------------	|------------------	|---------------------	|------------	|
| manufactor_id 	| manufactor_name  	| manufactor_lacation 	| activities 	|
| 1             	| 台灣汽車零件公司 	| 台北市              	| 提供零部件 	|
| 2             	| 台北車業         	| 台北市              	| 提供零部件 	|
| 3             	| 南台汽車         	| 高雄市              	| 提供零部件 	|
| 4             	| 台南汽車製造     	| 台南市              	| 製造汽車   	|
| 5             	| 彰化汽車工廠     	| 彰化縣              	| 製造汽車   	|
| 6             	| 高雄汽車生產     	| 高雄市              	| 製造汽車   	|

| Factory   |                  |
|------------|------------------|
| factory_id | supplier_name    |
| 1          | 汽車零件之家     |
| 2          | 訊發零件之家     |
| 3          | 龍騰汽車零件公司 |
| 4          | 光達汽車零件     |

| Model          |                  |
|----------------|------------------|
| model_id       | brand_name       |
| BZNZ-0302S-1   | 汽車零件之家     |
| BZNZ-0303      | 訊發零件之家     |
| MVE-ST72       | 龍騰汽車零件公司 |
| DAF-FT3605DKZ  | 光達汽車零件     |
| MAN-16.290HOCL | 輝煌汽車零件公司 |
