import pandas as pd
from svm_model import SVMModel
import joblib
# from sklearn.externals import joblib
import numpy as np
import json
link_data = "./data.csv"

class TextClassificationPredict(object):
    def __init__(self):
        self.clf = None
        self.data=None
    def convert_data_json(self,data_str):
        json_ = json.loads(data_str)
        data={"feature":[],"target":[]}
        for i in json_:
            data["feature"].append(i["input"])
            data["target"].append(i["nhan_data"])
        self.data = pd.DataFrame(data)
    def convert_data_csv(self,rawData): #raw data la mot chuoi a rua
        rawData = rawData.split("\n") 
        data={"feature":[],"target":[]} 
        for line in rawData:
            feature = line.split(",")[0]
            target = line.split(",")[1]
            data["feature"].append(feature)
            data["target"].append(target)
        dataF = pd.DataFrame(data)
        self.data = dataF
    def train_model(self):
        # Tạo train data
        model = SVMModel()
        # df_train = pd.read_csv(link_data)
        df_train = self.data
        self.clf = model.clf.fit(df_train["feature"], df_train["target"])
        # self.clf = joblib.load('./tenfile.sav')
    def tra_loi(self,msg):
        test_data = []
        test_data.append({"feature": u"{}".format(msg)})
        df_test = pd.DataFrame(test_data)
        predict_proba = max(self.clf.predict_proba(df_test["feature"])[0,:])
        if predict_proba > 0.4:
            predicted = self.clf.predict(df_test["feature"])[0]
            test_data.clear
            print("Accuracy :" +str(predict_proba))
            return predicted
        else:
            return "TOI-KHONG-HIEU"