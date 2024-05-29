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
## Tables 內容說明
| Vehicle           |           |               |           |             |            |      |
|-------------------|-----------|---------------|-----------|-------------|------------|------|
| vin               | option_id | manufactor_id | dealer_id | import_date | salesprice | sold |
| ABC12345678901234 | 1         | 1             | 1         | 2023/1/5    | 1000000    | yes  |
| DEF23456789012345 | 1         | 2             | 2         | 2022/9/15   | 1200000    | no   |
| GHI34567890123456 | 2         | 3             | 3         | 2023/3/25   | 1100000    | no   |
| HIJ56789012345678 | 3         | 4             | 4         | 2023/5/1    | 1200000    | yes  |
| GHI34567890123456 | 4         | 5             | 5         | 2024/4/19   | 1500000    | yes  |
| IJK67890123456789 | 5         | 6             | 6         | 2024/8/13   | 2000000    | yes  |

| Information       |               |         |       |                  |                |      |
|-------------------|---------------|---------|-------|------------------|----------------|------|
| option_id         | brand_name    | style   | color | engine           | transmiscion   | sold |
| 1                 | Volkswagen    | 4 doors | black | 1.0L TSI         | 6-Speed Manual | yes  |
| 2                 | Mercedes-Benz | SUV     | white | 2.0L Turbo       | 9G-TRONIC      | no   |
| 3                 | Audi          | 4 doors | gray  | 1.4L TFSI        | S-Tronic       | no   |
| 4                 | Mercedes-Benz | 4 doors | black | 2.0L Turbo       | 9G-TRONIC      | yes  |
| 5                 | Mercedes-Benz | SUV     | black | 3.0L V6 Bi-Turbo | 9G-TRONIC      | yes  |
| IJK67890123456789 | 5             | 6       | 6     | 2024/8/13        | 2000000        | yes  |

| Part              |                        |                 |               |            |                   |      |
|-------------------|------------------------|-----------------|---------------|------------|-------------------|------|
| part_id           | part_name              | manufactor_date | manufactor_id | factory_id | vin               | sold |
| 1                 | Brake line             | 2022/12/30      | 1             | 1          | ABC12345678901234 | yes  |
| 2                 | Brake line             | 2023/7/19       | 2             | 1          | DEF23456789012345 | no   |
| 3                 | Air filter             | 2023/8/17       | 3             | 2          | GHI34567890123456 | no   |
| 4                 | spark plug line        | 2022/3/14       | 4             | 3          | HIJ56789012345678 | yes  |
| 5                 | air conditioner switch | 2023/2/27       | 5             | 4          | GHI34567890123456 | yes  |
| IJK67890123456789 | 5                      | 6               | 6             | 2024/8/13  | 2000000           | yes  |
