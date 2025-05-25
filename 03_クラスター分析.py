import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance


# ルート設定 ##########
Root_Dir = "C:/Users/fuu_m/OneDrive/NRIコンペ2021/"

# データ読込 ##########
df_View = pd.read_csv(Root_Dir + "01_raw/テレビ番組視聴状況_2021.csv", engine='python', na_values=' ', header=0)
df_TV = pd.read_csv(Root_Dir + "01_raw/TV番組一覧.csv", engine='python', na_values=' ', header=0, encoding='utf-8_sig')
df_Main = pd.read_csv(Root_Dir + "01_raw/メインデータ_2021.csv", engine='python', na_values=' ', header=0)
Rating_all = pd.read_pickle(Root_Dir + '03_data/target_rating')
Flg_attribute = pd.read_pickle(Root_Dir + '03_data/Flg_attribute')


"""""""""""""""""""""""""""""""""""""""""""""
# 費用対効果上位番組の抽出
"""""""""""""""""""""""""""""""""""""""""""""
# 属性フラグ+視聴履歴データ
View = pd.merge(Flg_attribute, df_View, on='SampleID')

# 連ドラ除去
Rating_all = Rating_all[~Rating_all.title_name.str.contains(
                'めざましテレビ（７時まで）|韓流プレミア|天国と地獄|リカ|その女|書けない|モコミ|レッドアイズ|監察医|火曜ドラマ|青のＳＰ|アノニマス|ＮＮＮ　未来へのチカラ')]

# ターゲット毎の対象番組を確認 ##########
def Get_TopTitle(target):

    # 費用対効果の作成
    target_rate = Rating_all[['title_code_variable','title_name','tv_day_text',
                          'start_hour','Ratio_All','Ratio_'+str(target)]]
    target_rate['cospa'] = target_rate['Ratio_'+str(target)] / target_rate.Ratio_All # ターゲット費用対効果

    # 上位番組抽出：ターゲット視聴率5%以上かつ費用対効果1以上
    Top_title = target_rate[(target_rate['Ratio_'+str(target)]>=0.05)&(target_rate.cospa>1)]
    Top_title = Top_title.sort_values('cospa', ascending=False).head(50).reset_index(drop=True)

    return Top_title

TopTitle_SI = Get_TopTitle('Single_IncomeL')
TopTitle_MU = Get_TopTitle('Male_Under30s')
TopTitle_MM = Get_TopTitle('Male_Married')
TopTitle_FS = Get_TopTitle('Female_Single')
TopTitle_FC = Get_TopTitle('Female_Child')
TopTitle_FM = Get_TopTitle('Female_Married')


titles_Single_IncomeL = [
        "めざましテレビ（７時から）",
        "めざましテレビ（７時まで）",
        "クイズ！オンリー１",
        "サンドウィッチマン＆芦田愛菜の博士ちゃん",
        "ジョブチューン",
        "炎の体育会ＴＶ",
        ]

titles_Male_Under30s = [
        "オールスター後夜祭",
        "カンブリア宮殿",
        "クイズ！ＴＨＥ違和感",
        "クレヨンしんちゃん",
        "サッカー日本代表・国際強化試合",
        "ダウンタウンのガキの使いやあらへんで",
        "テレビ千鳥",
        "ワンピース",
        "乃木坂工事中",
        "全力！脱力タイムズ",
        "千鳥のクセがスゴいネタＧＰ",
        "千鳥ＶＳかまいたち",
        "日向坂で会いましょう",
        "幸せ！ボンビーガール",
        "有吉ぃぃｅｅｅｅｅ",
        "林先生の初耳学",
        "水曜日のダウンタウン",
        "激レアさんを連れてきた。",
        "ＤＲＡＭＡＴＩＣ　ＢＡＳＥＢＡＬＬ",
        "ＦＩＦＡワールドカップ"
        ]

titles_Male_Married = [
        "みんなのＫＥＩＢＡ",
        "ウェークアップ",
        "ウェークアップ！ぷらす",
        "グッド！モーニング",
        "サタデーステーション",
        "サンデーモーニング",
        "サンデーＬＩＶＥ！！",
        "ジャンクＳＰＯＲＴＳ",        
        "ワンピース",
        "噂の！東京マガジン",
        "報道ステーション",
        "週刊ニュースリーダー",
        "ＤＲＡＭＡＴＩＣ　ＢＡＳＥＢＡＬＬ",
        "ＮＥＷＳ２３",
        "ＷＢＳ"
        ]

titles_Female_Single = [
        "めざましテレビ（７時から）",
        "クイズ！オンリー１",
        "ジョブチューン",
        "炎の体育会ＴＶ",
        "ポツンと一軒家",
        "動物スクープ１００連発",
        "坂上＆指原のつぶれない店",
        "１億３０００万人のＳＨＯＷチャンネル"
        ]

titles_Female_Child = [
        "それいけ！アンパンマン",
        "とくダネ！",
        "トロピカル～ジュ！プリキュア",
        "ドラえもん",
        "ヒーリングっどプリキュア",
        "ボクらの時代",
        "ポケットモンスター",
        "仮面ライダーセイバー",
        "機界戦隊ゼンカイジャー",
        "魔進戦隊キラメイジャー",
        "ｎｅｗｓ　ｅｖｅｒｙ"
        ]

titles_Female_Married = [
        "ドラえもん",
        "バイキングＭＯＲＥ",
        "ミヤネ屋",
        "Ｎスタ",
        "ｎｅｗｓ　ｅｖｅｒｙ",
        #"ＮＮＮ　未来へのチカラ"
        ]


"""""""""""""""""""""""""""""""""""""""""""""
# 因子得点算出
"""""""""""""""""""""""""""""""""""""""""""""
factors = {
    'Active'   :['HOB_21_MA', 'HOB_26_MA', 'HOB_27_MA', 'HOB_29_MA'], 
    'Indoor'   :['HOB_07_MA', 'HOB_08_MA', 'HOB_16_MA'], 
    'Outdoor'  :['HOB_02_MA', 'HOB_03_MA', 'HOB_04_MA', 'HOB_05_MA'], 
    'Machining':['HOB_12_MA', 'HOB_11_MA', 'HOB_13_MA', 'HOB_14_MA', 'HOB_15_MA'],
    'Gamble'   :['HOB_23_MA', 'HOB_24_MA', 'HOB_25_MA'],
    'Quality'  :['SEN_03_MA', 'SEN_09_MA', 'SEN_13_MA', 'SEN_15_MA', 'SEN_28_MA'], 
    'Value'    :['SEN_01_MA', 'SEN_02_MA', 'SEN_22_MA', 'SEN_24_MA', 'SEN_29_MA'],
    'Reference':['SEN_11_MA', 'SEN_26_MA','SEN_30_MA'], 
    'Design'   :['SEN_04_MA', 'SEN_08_MA'],
    'Safety'   :['SEN_17_MA', 'SEN_18_MA'],
    'Negative' :['NC_Scale_04_MX', 'NC_Scale_06_MX', 'NC_Scale_07_MX', 'NC_Scale_08_MX', 'NC_Scale_09_MX', 'NC_Scale_10_MX', 'NC_Scale_11_MX', 'NC_Scale_15_MX'],
    'Logical'  :['NC_Scale_01_MX', 'NC_Scale_02_MX', 'NC_Scale_05_MX', 'NC_Scale_12_MX', 'NC_Scale_14_MX'],
    'Cautious' :['NC_Scale_03_MX', 'NC_Scale_13_MX', 'RF_Scale_01_MX', 'RF_Scale_07_MX', 'RF_Scale_08_MX', 'RF_Scale_09_MX'],
    'Curious'  :['RF_Scale_02_MX', 'RF_Scale_03_MX', 'RF_Scale_04_MX', 'RF_Scale_05_MX', 'RF_Scale_10_MX']
    }

# 全サンプルの因子得点算出
score_all = pd.DataFrame()
for factor, quest in factors.items():
    quest.insert(0,'SampleID')
    df_fact = df_Main[quest]
    score = pd.DataFrame(df_fact.iloc[:,1:].sum(axis=1,skipna=False), columns=[factor])
    scaler = StandardScaler()

    if factor in ('Logical','Curious'):
        score[factor+'_dev'] = 50 + scaler.fit_transform(score)*-10            
    else:
        score[factor+'_dev'] = 50 + scaler.fit_transform(score)*10
    
    score_all = pd.concat([score_all, score], axis=1)

# 偏差値のスコアのみ保持する
score_all.drop(factors.keys(), axis=1, inplace=True)


"""""""""""""""""""""""""""""""""""""""""""""
# クラスター分析
"""""""""""""""""""""""""""""""""""""""""""""
def Clustering(target, target_titles):

    # ターゲット費用対効果の算出
    target_rate = Rating_all[['title_code_variable','title_name','tv_day_text',
                          'start_hour','Ratio_All','Ratio_'+str(target)]]
    target_rate['cospa'] = target_rate['Ratio_'+str(target)] / target_rate.Ratio_All

    # 上位番組の全放送回を抽出
    Top_all = target_rate.copy()
    for i, title in enumerate(target_titles):
        Top_all.loc[Top_all.title_name.str.startswith(title), 'title_no'] = i+1
    Top_all = Top_all[Top_all.title_no>0]
    Top_all.sort_values(['title_no','title_code_variable'], ascending=[True,True], inplace=True)
    Top_all = Top_all.reset_index(drop=True)
    
    """
    クラスタリング実施
    """
    # 分析用データ
    titles = Top_all.title_code_variable.to_list()
    features = View[View['Flg_'+str(target)]==1][titles].T
    
    # 階層型クラスタリング(ウォード法, ユークリッド距離)
    linkage_result = linkage(features, method='ward', metric='euclidean') #0:クラスター番号1, 1:クラスター番号2, 2:クラスタリングに伴う距離の変化, 3:新しいクラスターに属するデータ数
    threshold = 0.8*np.max(linkage_result[:,2]) #閾値設定

    # クラスタリング結果を取得
    clustered = fcluster(linkage_result, threshold, criterion='distance')
    result_clus = pd.DataFrame([features.index, clustered]).T
    result_clus.columns = ['title_code_variable','ClusterID']

    # 整形
    result_clus = pd.merge(Top_all, result_clus, on='title_code_variable') #番組名付与
    result_clus.sort_values(['ClusterID','title_no','title_code_variable'],
                           ascending=[True,True,True],inplace=True)
    
    """
    クラスター毎の因子得点を算出
    """
    # 分析用データの作成
    View_score = pd.concat([score_all, View], axis=1)
    View_score = View_score[View_score['Flg_'+target]==1] #ターゲットに限定

    # 番組単位で平均値算出
    Avg_all = pd.DataFrame()
    for code in Top_all.title_code_variable:
        tar_score = View_score[View_score[code]==1]
        Avg_byTitle = pd.DataFrame(tar_score.iloc[:,:14].mean(), columns=[code]).T
        Avg_all = Avg_all.append(Avg_byTitle)
            
    # 番組単位で平均値算出
    Avg_all = pd.merge(result_clus, Avg_all, left_on='title_code_variable', right_index=True)
    
    #Avg_byCtg = Avg_all.groupby('ClusterID').mean().drop(['start_hour','title_no'],axis=1)
    Avg_byTno = Avg_all.groupby('title_no').mean().drop('start_hour',axis=1)
    Avg_byTno.index = target_titles

    return result_clus, Avg_byTno

# 実施
Clus_SI, Fact_SI  = Clustering('Single_IncomeL', titles_Single_IncomeL)
Clus_MU, Fact_MU  = Clustering('Male_Under30s', titles_Male_Under30s)
Clus_MM, Fact_MM  = Clustering('Male_Married', titles_Male_Married)
Clus_FS, Fact_FS = Clustering('Female_Single', titles_Female_Single)
Clus_FC, Fact_FC = Clustering('Female_Child', titles_Female_Child)
Clus_FM, Fact_FM  = Clustering('Female_Married', titles_Female_Married)


"""""""""""""""""""""""""""""""""""""""""""""
# 番組間ユークリッド距離の算出
"""""""""""""""""""""""""""""""""""""""""""""
def Calc_dist(target, titles_list):
    
    # ターゲット視聴率と費用対効果を保持・作成
    Rating = Rating_all[['title_code_variable','title_name','tv_day_text',
                         'start_hour','Ratio_All','Ratio_'+str(target)]]
    Rating['cospa'] = Rating['Ratio_'+str(target)] / Rating.Ratio_All

    # 同一番組をカテゴライズ
    for i, title in enumerate(titles_list):
        Rating.loc[Rating.title_name.str.startswith(title), 'title_no'] = i+1
    
    # 分析対象番組を抽出
    Rating = Rating[Rating.title_no>0]
    Rating.sort_values(['title_no','title_code_variable'],ascending=[True,True],inplace=True)
    titles = Rating.title_code_variable.to_list()
    
    # 個別番組単位で距離を算出
    V_result = pd.DataFrame()
    for title1 in titles:
        spot1 = df_View[title1].values
        
        H_result = pd.DataFrame()
        for title2 in titles:
            spot2 = df_View[title2].values
            dist = distance.euclidean(spot1, spot2)
            dist = np.where(dist==0, np.nan, dist)
            df_dist = pd.DataFrame([dist],columns=[title2],index=[title1])
            H_result = pd.concat([H_result, df_dist], axis=1) # 結果の横結合
        
        # 結果の縦結合
        V_result = pd.concat([V_result, H_result], axis=0)

    # 番組カテゴリ毎の距離算出    
    All_result = pd.merge(Rating[['title_code_variable','title_no']], V_result,
                          left_on='title_code_variable', right_index=True)
    All_result1 = All_result.groupby('title_no').mean().T
    All_result1 = pd.merge(Rating[['title_code_variable','title_no']], All_result1,
                           left_on='title_code_variable', right_index=True)
    Output2 = All_result1.groupby('title_no').mean()
    
    
    # 結果整形
    V_result.columns = Rating.title_name.to_list()
    Output1 = pd.merge(Rating, V_result, left_on='title_code_variable', right_index=True)    
    Output2.columns, Output2.index = titles_list, titles_list
    
    return Output1, Output2

# 実行
dist1_SI, dist2_SI = Calc_dist('Single_IncomeL', titles_Single_IncomeL)
dist1_MU, dist2_MU = Calc_dist('Male_Under30s', titles_Male_Under30s)
dist1_MM, dist2_MM = Calc_dist('Male_Married', titles_Male_Married)
dist1_FS, dist2_FS = Calc_dist('Female_Single', titles_Female_Single)
dist1_FC, dist2_FC = Calc_dist('Female_Child', titles_Female_Child)
dist1_FM, dist2_FM = Calc_dist('Female_Married', titles_Female_Married)
