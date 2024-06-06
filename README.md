# database_finalHW
請參考以下介紹：
112-2 資料庫期末作業
使用HeisiSQL的資料庫管理工具
## Server Tier 架設說明
1. 先於mariaDB的官網下載並安裝
2. 啟動MySQL server後，開啟HeidiSQL或MySQL，於左下角新增一個工作階段，右方參數設定完成後開啟。
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/af098fa2-4a77-42c9-a13a-1aa6385d37c0)

   ```bash=
   host="0.tcp.jp.ngrok.io",
   port=11051, user="411062002",
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
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/2fb1b17f-d49a-4135-bf43-57dccf6ffe7f)



## Relation Schema
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/2078abcd-8e0d-4de4-97bd-073ab7843741)



## Tables 內容說明
| Vehicle           |                |               |             |            |            |                  |       |                |         |
|:-----------------:|:--------------:|:-------------:|:-----------:|:----------:|:----------:|:----------------:|:-----:|:--------------:|:-------:|
| vin               | model_id       | manufactor_id | import_date | sold_date  | salesprice | engine           | color | transmission   | style   |
| ABC12345678901234 | BZNZ-0302S-1   | 1             | 2023/1/5    | 2023/7/24  | 1000000    | 1.0L TSI         | black | 6-Speed Manual | 4 doors |
| DEF23456789012345 | BZNZ-0303      | 2             | 2022/9/15   | 2023/1/30  | 1200000    | 2.0L Turbo       | white | 9G-TRONIC      | SUV     |
| GHI21367890123456 | MVE-ST72       | 3             | 2023/3/25   | 2024/4/20  | 1100000    | 1.4L TFSI        | gray  | S-Tronic       | 4 doors |
| HIJ56789012345678 | DAF-FT3605DKZ  | 4             | 2023/5/1    | 2023/8/14  | 1200000    | 2.0L Turbo       | black | 9G-TRONIC      | 4 doors |
| GHI34567890123456 | MAN-16.290HOCL | 5             | 2023/4/19   | 2023/12/21 | 1500000    | 3.0L V6 Bi-Turbo | black | 9G-TRONIC      | SUV     |
| IJK67890123456789 | BZNZ-0302S-1   | 6             | 2022/8/13   | 2023/4/15  | 2000000    | 1.0L TSI         | white | S-Tronic       | SUV     |

| Part    |                        |                 |               |            |                   |
|---------|------------------------|-----------------|---------------|------------|-------------------|
| part_id | part_name              | manufactor_date | manufactor_id | factory_id | vin               |
| 1       | Brake line             | 2022/12/30      | 1             | NULL       | ABC12345678901234 |
| 2       | Brake line             | 2023/7/19       | NULL          | 1          | DEF23456789012345 |
| 3       | Air filter             | 2023/8/17       | NULL          | 2          | GHI34567890123456 |
| 4       | spark plug line        | 2022/3/14       | 2             | NULL       | HIJ56789012345678 |
| 5       | transmission           | 2023/2/27       | 3             | NULL       | GHI34567890123456 |
| 6       | transmission           | 2023/1/20       | NULL          | 4          | IJK67890123456789 |

| Salesrecord       |             |            |
|-------------------|-------------|------------|
| vin               | customer_id | sold_date  |
| ABC12345678901234 | 762         | 2023/7/24  |
| HIJ56789012345678 | 504         | 2023/8/14  |
| GHI34567890123456 | 321         | 2023/12/21 |
| IJK67890123456789 | 245         | 2023/4/15  |
| DEF23456789012345 | 777         | 2023/1/30  |
| GHI21367890123456 | 432         | 2024/4/20  |

| Customer    	|        	|        	|              	|                         	|               	|
|-------------	|--------	|--------	|--------------	|-------------------------	|---------------	|
| customer_id 	| name   	| gender 	| phone        	| address                 	| annual_income 	|
| 762         	| 王小明 	| male   	| 0912-345-678 	| 台北市信義區松高路123號 	| 550000        	|
| 504         	| 陳美玲 	| female 	| 0921-234-567 	| 屏東縣屏東市民權路666號 	| 600000        	|
| 321         	| 黃小菁 	| female 	| 0933-456-789 	| 台中市南屯區            	| 740000        	|
| 245         	| 盧婷婷 	| female 	| 0944-567-890 	| 嘉義縣朴子市中華路555號 	| 590000        	|
| 777         	| 周志明 	| male   	| 0911-234-567 	| 花蓮縣花蓮市中山路707號 	| 880000        	|
| 432         	| 陳明志 	| male   	| 0911-111-222 	| 台北市中山區中正路123號 	| 900000        	|

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
| 2          | 光達汽車零件     |
| 3          | 龍騰汽車零件公司 |
| 4          | Getrag          |

| Model          |                  |
|----------------|------------------|
| model_id       | brand_name       |
| BZNZ-0302S-1   | 汽車零件之家     |
| BZNZ-0303      | 訊發零件之家     |
| MVE-ST72       | 龍騰汽車零件公司 |
| DAF-FT3605DKZ  | 光達汽車零件     |
| MAN-16.290HOCL | 輝煌汽車零件公司 |

| Inventory          |            |              |   |
|--------------------|------------|--------------|---|
| vin                | dealer_id  | import_date  |   |
| ABC12345678901234  | 2          | 2023/1/5     |   |
| DEF23456789012345  | 1          | 2022/9/15    |   |
| GHI21367890123456  | 3          | 2023/3/25    |   |
| HIJ56789012345678  | 1          | 2023/5/1     |   |
| GHI34567890123456  | 4          | 2023/4/19    |   |
| IJK67890123456789  | 5          | 2022/8/13    |   |

## Query的SQL語法如下
1. Suppose that it is found that transmissions made by supplier Getrag between two given dates are defective. Find the VIN of each car containing such a transmission and the customer to which it was sold. If your design allows, suppose the defective transmissions all come from only one of Getrag’s plants.

```bash=
```
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/0ec85abc-5178-4b84-8c41-8e3391112131)

2. Find the dealer who has sold the most (by dollar-amount) in the past year.
```bash=
SELECT d.dealer_name, SUM(v.salesprice) AS total_sales
FROM Vehicle v
JOIN Salesrecord s ON v.vin = s.vin
JOIN Inventory i ON v.vin = i.vin
JOIN Dealer d ON i.dealer_id = d.dealer_id
WHERE
    s.sold_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 YEAR) 
    AND CURDATE()
GROUP BY d.dealer_name
ORDER BY total_sales DESC
LIMIT 1;
```
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/7459397f-8767-43b4-a68f-a544a61f98e8)

3. Find the top 2 brands by unit sales in the past year
```bash=
SELECT m.brand_name, COUNT(v.vin) AS unit_sales
FROM Vehicle v
JOIN Model m ON v.model_id = m.model_id
JOIN Salesrecord s ON v.vin = s.vin
WHERE s.sold_date BETWEEN DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
     AND CURDATE()
GROUP BY m.brand_name
ORDER BY unit_sales DESC
LIMIT 2;
```
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/5b280f0e-95b8-44be-b327-6fcc00887324)

4. In what month(s) do SUVs sell best?
```bash=
SELECT MONTH(s.sold_date) AS sale_month, COUNT(v.vin) AS suv_sales
FROM Vehicle v
JOIN Salesrecord s ON v.vin = s.vin
WHERE v.style = 'SUV'
GROUP BY MONTH(s.sold_date)
ORDER BY suv_sales DESC
LIMIT 1;
```
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/4ed3a285-3ede-4fc9-ae63-d1aad7037546)

5. Find those dealers who keep a vehicle in inventory for the longest average time. 
```bash=
SELECT d.dealer_name,
       AVG(DATEDIFF(CURDATE(), i.import_date)) AS average_inventory_time
FROM Vehicle v
JOIN Inventory i ON v.vin = i.vin
JOIN Dealer d ON i.dealer_id = d.dealer_id
GROUP BY d.dealer_id, d.dealer_name
ORDER BY average_inventory_time DESC
LIMIT 1;
```
![image](https://github.com/sylvia8813/database_finalHW/assets/145385712/2f3b7e28-545d-4ff3-b4be-eeca7dfc02e7)
