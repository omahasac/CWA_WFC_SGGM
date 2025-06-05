# Style Guide for Griddata Map
根據中心的需求，希望發展地圖繪製公版工具，整理常見的需求並且統整

# 2025/04/15 更新摘要
1. 避免重複讀取shapefile

# 2025/03/06 更新摘要
1. 略增風標的大小跟密度

# 2025/01/20 更新摘要
1. 以savez_compressed進一步壓縮GFE參考檔大小
2. 新增繪製國道的功能，使用方式為`Draw_obj.draw(..., road=True)`，或者填入HEX色碼
3. 新增繪製西濱快速公路的功能，使用方式為`Draw_obj.draw(..., road_ph61=True)`，或者填入HEX色碼

# 2025/01/13 更新摘要(本次更新有動到interface)
1. 為了讓不同版面的地圖能有不同的邊界線粗細，因此將海岸線相關設定從原本的`DrawGriddataMap(...)`，移動到`Draw_obj.draw(...)`
2. 除了draw_zoom_in產出的圖片是預設邊界線粗度0.4之外，其餘則為0.8

# 2025/01/09 更新摘要
1. 在`Draw_obj.draw`類型的方法中新增標註最小值的`draw_min`、`draw_min_tw`、`draw_min_main`三個關鍵字
2. 在`Draw_obj.draw`類型的方法中新增限制標註數量的`mark_limit_num`關鍵字，預設為1
3. 更新能見度色階，邊界改為0.1, 0.2, 0.3, 0.5, 1, 2, 5

# 2025/01/08 更新摘要
1. 色階新增溫度誤差色階，以及能見度色階(單位為公里)
2. 移除shapefile中與海岸線無關的檔案，並將參考檔`GFEGridInfo_1km_Ext_OI.txt`內容重新以`npz`封裝，縮小參考資料夾大小
3. 新增地圖左下角文字功能，可在`set_info`設定

# 2024/01/01-2024/12/25 更新摘要
* 調整子圖框位置與比例，金門與主圖相同，馬祖為3倍大，並右移避免遮蔽烏坵
* 在`set_info`方法新增`lead_time_unit`的關鍵字，預設為h，可以如下操作調整`Draw_obj.set_info(..., lead_time_unit='m')`
* 為了增加方便性，不設定經緯度的情況下預設提供最新版GFE網格點
* 新增雷達迴波所使用之色階`Radar_Composite_Reflectivity`
* 配合雷達迴波新增黑底模式，使用`Draw_obj.draw(..., dark_mode=True)`呼叫
* 圖上最大值四捨五入到整數位
* 新增`draw_wind_barbs`方法，可繪製僅含風標圖的透明背景圖，圖框範圍與`draw`相同
* 新增`put_uwind_vwind`方法，可以僅匯入風標圖所需的uwind與vwind(單位為公尺每秒)  
* 增加`calculate_gfe1km_total_water`方法，若資料是GFE1km網格點，可以用此方法計算total_water
* 預設移除外傘頂洲，可由`DrawGriddataMap(caisancho=True)`補回
* 新增功能，可在圖上標出最大值位置與數值，  
  可使用`Draw_obj.draw(..., draw_max=True)`呼叫，  
  或者`Draw_obj.draw(..., draw_max_tw=True)`只標示台灣陸地最大值，  
  還有`Draw_obj.draw(..., draw_max_main=True)`標示台澎金馬蘭嶼綠島等有一定面積的陸地區域  


## 已測試過之環境版本
### 個人筆電
Python 3.10.9  
cartopy 0.21.1  
matplotlib 3.7.0  
numpy 1.23.5  
### Docker Image  
Python 3.10.12  
cartopy 0.22.0  
matplotlib 3.8.0  
numpy 1.26.1  

## 使用說明
基本上是操作`module`內的`draw_griddata.py`  
操作方式可以參考`module`內的`load_demo.py`  
還有要複製ref裡面需要的參考檔。  
  
0. 增加色階設定
下方的例子中，共有50個色階，最低跟最高的色碼設定在`color_under`與`color_over`，  
其餘的48個色階設定在`hex_list`，然後48個色階會有49個邊界設定在`boundary`，  
以及這49個邊界的文字標籤設定在`ticklabels`。  
接著是單位的文字描述`unit`，以及文字坐落的位子，座標是以colorbar左下為基準，  
範例中的`unit_xloc:1.05`、`unit_yloc:1.03`會約略在colorbar的正上方，略偏右  
```json
{
    "temperature":{
        "color_under":"#000080",
        "color_over":"#9c68ad",
        "boundary":[
            -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
            10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
            30, 31, 32, 33, 34, 35, 36, 37, 38
        ],
        "hex_list":[
            "#0000cd", "#0000ff", "#0040ff", "#006aff", "#0095ff", "#00bfff", "#00eaff", "#00ffea", "#80fff4", "#117388", 
            "#207e92", "#2e899c", "#3d93a6", "#4c9eb0", "#5ba9ba", "#69b4c4", "#78bfce" ,"#87cad8", "#96d4e2", "#a4dfec",
            "#b3eaf6", "#0c924b", "#1d9a51", "#2fa257", "#40a95e", "#51b164", "#62b96a", "#74c170", "#85c876", "#96d07c", 
            "#a7d883", "#b9e089", "#cae78f", "#dbef95", "#f4f4c3", "#f7e78a", "#f4d576", "#f1c362", "#eeb14e", "#ea9e3a", 
            "#e78c26", "#e07b03", "#ed5138", "#ed1759", "#ad053a", "#780101", "#c3a4cd", "#af86bd"
        ],
        "ticklabels":[
            -10, "", -8, "", -6, "", -4, "", -2, "", 
            0, "",  2, "",  4, "",  6, "",  8, "", 
            10, "", 12, "", 14, "", 16, "", 18, "", 
            20, "", 22, "", 24, "", 26, "", 28, "", 
            30, "", 32, "", 34, "", 36, "", 38
        ],
        "unit":"$degree$C",
        "unit_xloc":1.05,
        "unit_yloc":1.03
    }

}
```
1. 初始化繪圖工具  
從模組中匯入`DrawGriddataMap`，再將其初始化，初始化欄位有一個變數`ref_dir`，是參考資料夾的路徑，  
預設為`ref_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ref')`，  
```python
from module.draw_griddata import DrawGriddataMap
Draw_obj = DrawGriddataMap()
```
2. 輸入網格點ARRAY  
這裡的`lat`與`lon`都是二維的numpy array，單精度雙精度都可以使用，  
預設會以新版1公里GFE初始化(117~124, 21.2~27)，資料符合該範圍可以跳過此步驟。  
```python
Draw_obj.put_latlon(lat, lon)
```
3. 輸入資料  
除了第一個欄位values之外，後方還有幾個欄位可以使用`values, **kwargs`，  
當名稱是total_water的時候，會將數值寫在圖上totoal water的顯示位置，  
當名稱是uwind跟vwind的時候，才能繪製風標圖
```python
Draw_obj.put_data(tmax)
```
若只要繪製透明背景風標圖，可以使用以下方式只匯入風場資訊  
```python
Draw_obj.put_uwind_vwind(uwind, vwind)
```
4. 設定標題  
第一個欄位是生產的單位名稱或是產線名稱或是生產方式，  
第二個欄位是場量的名稱，第三個欄位是python的datetime物件，用來標示資料生產的時間，  
第四第五個欄位是Lead Time的起點跟終點，單位是小時，整點預報就填寫1個，有時間段的統計就填寫2個，  
第四個欄位不填寫或是填寫-999的時候就不會顯示
```python
Draw_obj.set_info('ECDCA', 'max-T', init_date, 24, 36)
```
5. 運行繪圖  
有draw, draw_zoom_in, draw_zoom_out三個方法可使用，繪製的範圍不同，  
上述方法的第一個欄位是圖片輸出路徑與名稱，第二個欄位是色階在設定檔裡面的名稱，  
第三個欄位是`draw_barbs`預設是False，改成True可以疊上風標圖(步驟3要匯入風速)，  
若使用draw_zoom_in方法，則無風標圖可使用
```python
Draw_obj.mask_sea_gfe1km() # 用以遮蔽圖資外的範圍，自行選擇是否使用
Draw_obj.draw('tmax_demo.png', 'temperature')
Draw_obj.draw_zoom_in('tmax_demo.png', 'temperature')
Draw_obj.draw_zoom_out('tmax_demo.png', 'temperature')
```
若僅要繪製透明背景的風標圖，可以使用，繪圖範圍與`draw`相同  
```python
Draw_obj.draw_wind_barbs('wind_barbs_demo.png')
```