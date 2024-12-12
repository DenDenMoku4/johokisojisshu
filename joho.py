import streamlit as st
import pandas as pd
import pydeck as pdk
import math

st.title("最寄りのJリーグクラブ2025")
st.write("このサイトでは緯度と経度を入力すると最寄りのJリーグクラブが表示されます！")

df = pd.DataFrame({
    'latitude': [
        43.0155146624762, 35.99284980340223, 35.90442439057765, 35.84945581637986, 35.66458055978756, 
        35.769660908307586, 35.59326731539242, 35.586435373587854, 35.5108539357046, 35.34410365257245, 
        37.88296634465003, 34.72618967411714, 35.085146102982826, 35.0180199390456, 34.80331956304201, 
        34.616016420673326, 34.65730468128645, 34.40241678134133, 33.586749693632584, 33.37211651577936,

        38.31975970996166, 39.72200206763264, 38.336111948291894, 37.017845109547224, 36.34595472239713, 
        36.515510124071554, 36.412127026342, 35.5777220935923, 35.469888441597064, 35.62323407740334, 
        34.98516642478781, 34.88254090164482, 34.68124250168755, 34.155338807322686, 34.1691761617415, 
        33.76908807491083, 32.83926971305532, 32.83769171562157, 33.201647506286335, 31.565523939286447,

        40.59095126731528, 39.648261061631665, 37.723914450403925, 35.916757101551525, 35.47103433308346, 
        35.52752657999696, 36.18047153597394, 36.580171931331684, 36.62575677932421, 36.596786999340665, 
        35.156383483731936, 35.44186937942266, 34.66976456874177, 34.69805835626216, 35.45881560535673, 
        34.26271817480345, 34.041363790510395, 33.891495436131486, 32.07461777543211, 26.30939994487347,

        34.81176670347749, 35.628328826943786, 35.28302494423647, 40.839441891850875, 
        33.1991659675214, 33.511955410819574, 34.9806456957016, 34.83599023675995, 35.07262272873517, 
        35.66585741741378, 34.81955276982877, 35.71826065074556, 31.945468894044982, 26.33361586283162, 36.33816629815042,34.490148898135914,


],
    'longitude': [
        141.40975715180173, 140.64029658350165, 139.7171498453332, 139.97541742201096, 139.52708830652048, 
        139.70800353729214, 139.4386802604314, 139.65242142973753, 139.60656529846457, 139.3411792369571, 
        139.05922783848288, 137.87520028250927, 137.17117672882034, 135.58462465998127, 135.53860028997886, 
        135.51642773639188, 135.16936534435823, 132.45380672088376, 130.46066178957784, 130.52037983889343,

        140.88139897775488, 140.09589067831755, 140.37847876192092, 140.8641591688742, 140.41282618323706, 
        139.85805378335837, 139.0533686605151, 140.1228946599251, 139.6035182370802, 138.5900022366873, 
        138.48181512832028, 138.23318123617256, 133.91893463603455, 131.43775823567654, 134.6175886515321, 
        132.79759654333986, 130.0392994966869, 130.80005121203195, 131.65758577365526, 130.55975182656195,

        141.45739430918405, 141.13787996291467, 140.3609840080054, 139.63390528293252, 139.60369779350376, 
        139.3863705019673, 137.91719426034996, 138.17000917598193, 137.1955647992835, 136.65782712253198, 
        138.85405308240053, 136.76622389052218, 135.62640977464198, 135.82721392962316, 134.22132965984173,
        133.78608850209577, 132.9585270974845, 130.8893187582683, 131.49072376550046, 127.82123935419278,

        137.722323121278, 139.89234375996026, 136.25505217506526, 140.84157579453307, 
        131.65084447010392, 133.50296622782307, 137.18975323920174, 136.51395015618812, 136.578570036804, 
        139.52337160602514, 135.6840311287064, 139.56776064467732, 131.37788621937986, 127.7889788076674, 139.64558790700102,135.79219192848075,

        

],
    'name': [
        '北海道コンサドーレ札幌(J2)', '鹿島アントラーズ(J1)', '浦和レッズ(J1)', '柏レイソル(J1)', 'FC東京(J1)',
          '東京ヴェルディ(J1)', 'FC町田ゼルビア(J1)', '川崎フロンターレ(J1)', '横浜F・マリノス(J1)', '湘南ベルマーレ(J1)', 
          'アルビレックス新潟(J1)', 'ジュビロ磐田(J2)', '名古屋グランパス(J1)', '京都サンガF.C.(J1)', 'ガンバ大阪(J1)', 
          'セレッソ大阪(J1)', 'ヴィッセル神戸(J1)', 'サンフレッチェ広島(J1)', 'アビスパ福岡(J1)', 'サガン鳥栖(J2)',

          'ベガルタ仙台(J2)', 'ブラウブリッツ秋田(J2)', 'モンテディオ山形(J2)', 'いわきFC(J2)', '水戸ホーリーホック(J2)',
          '栃木SC(J3)', 'ザスパ群馬(J3)', 'ジェフユナイテッド千葉(J2)', '横浜FC(J1)', 'ヴァンフォーレ甲府(J2)', 
          '清水エスパルス(J1)', '藤枝MYFC(J2)', 'ファジアーノ岡山(J1)', 'レノファ山口FC(J2)', '徳島ヴォルティス(J2)', 
          '愛媛FC(J2)', 'V・ファーレン長崎(J2)', 'ロアッソ熊本(J2)', '大分トリニータ(J2)', '鹿児島ユナイテッドFC(J3)',

          'ヴァンラーレ八戸(J3)', 'いわてグルージャ盛岡(JFL)', '福島ユナイテッドFC(J3)', '大宮アルディージャ(J2)', 'Y.S.C.C.横浜(JFL)', 
          'SC相模原(J3)', '松本山雅FC(J3)', 'AC長野パルセイロ(J3)', 'カターレ富山(J2)', 'ツエーゲン金沢(J3)', 
          'アスルクラロ沼津(J3)', 'FC岐阜(J3)', 'FC大阪(J3)', '奈良クラブ(J3)', 'ガイナーレ鳥取(J3)', 
          'カマタマーレ讃岐(J3)', 'FC今治(J2)', 'ギラヴァンツ北九州(J3)', 'テゲバジャーロ宮崎(J3)', 'FC琉球(J3)',

          'Honda FC(JFL)', 'ブリオベッカ浦安(JFL)', 'レイラック滋賀(JFL)', 'ラインメール青森(JFL)', 
          'ヴェルスパ大分(JFL)', '高知ユナイテッドSC(J3)', 'FCマルヤス岡崎(JFL)', 'アトレチコ鈴鹿(JFL)', 'ヴィアティン三重(JFL)', 
          'クリアソン新宿(JFL)', 'FCティアモ枚方(JFL)', '横河武蔵野FC(JFL)', 'ミネベアミツミFC(JFL)', '沖縄SV(JFL)', '栃木シティ(J3)','飛鳥FC(JFL)',



]
})

# ユーザーから緯度と経度を入力
latitude_input = st.number_input('緯度を入力', -90.0, 90.0, 36.65)
longitude_input = st.number_input('経度を入力', -180.0, 180.0, 138.18)

def get_team_color(name):
    if "(J1)" in name:
        return [230, 0, 18] 
    if "(J2)" in name:
        return [1,126,64]
    if "(J3)" in name:
        return [2,98,178] 
    else:
        return [255,255,255]
    
df['color'] = df['name'].apply(get_team_color)


def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    radius = 6371.0
    return radius * c

def filter_by_league(df, league):
    return df[df['name'].str.contains(f"\\({league}\\)")]

def find_closest_by_league(lat, lon, df, league):
    league_df = filter_by_league(df, league)
    if league_df.empty:
        return f"{league}に該当するクラブがありません"
    distances = []
    for _, row in league_df.iterrows():
        dist = haversine(lat, lon, row['latitude'], row['longitude'])
        distances.append((row['name'], dist))
    sorted_distances = sorted(distances, key=lambda x: x[1])
    closest = sorted_distances[0]  
    return closest

closest_j1 = find_closest_by_league(latitude_input, longitude_input, df, "J1")
closest_j2 = find_closest_by_league(latitude_input, longitude_input, df, "J2")
closest_j3 = find_closest_by_league(latitude_input, longitude_input, df, "J3")
closest_jfl = find_closest_by_league(latitude_input, longitude_input, df, "JFL")

st.write("最寄りのクラブ（各リーグごと）:")
st.write(f"J1クラブ: {closest_j1[0]} - 距離: {closest_j1[1]:.2f} km" if isinstance(closest_j1, tuple) else closest_j1)
st.write(f"J2クラブ: {closest_j2[0]} - 距離: {closest_j2[1]:.2f} km" if isinstance(closest_j2, tuple) else closest_j2)
st.write(f"J3クラブ: {closest_j3[0]} - 距離: {closest_j3[1]:.2f} km" if isinstance(closest_j3, tuple) else closest_j3)
st.write(f"JFLクラブ: {closest_jfl[0]} - 距離: {closest_jfl[1]:.2f} km" if isinstance(closest_jfl, tuple) else closest_jfl)

layer = pdk.Layer(
    'ScatterplotLayer',
    data=df,
    get_position='[longitude, latitude]',
    get_radius=7000,
    get_color='color',
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=latitude_input, 
    longitude=longitude_input, 
    zoom=7.2 
)

deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state
)

st.pydeck_chart(deck)
st.write("赤丸はJ1,青丸はJ2,緑丸はJ3,白丸はJFLに所属しているクラブです(2025年)")