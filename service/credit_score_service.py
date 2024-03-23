import json
import pickle
import pandas as pd
from model.credit_score_request import CreditScoreRequest

class CreditScoreService():
    def __init__(self):
        self.dfCol = ['Month','Age','Occupation','Annual_Income','Monthly_Inhand_Salary', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate','Num_of_Loan', 'Credit_History_Age']
    def prediction(self, creditScoreRequest: CreditScoreRequest):
        data = {
            'Month': creditScoreRequest['month'],
            'Age': creditScoreRequest['age'],
            'Occupation': creditScoreRequest['occupation'],
            'Annual_Income': creditScoreRequest['annualIncome'],
            'Monthly_Inhand_Salary': creditScoreRequest['monthlyInhandSalary'],
            'Num_Bank_Accounts': creditScoreRequest['numBankAccount'],
            'Num_Credit_Card': creditScoreRequest['numCreditCard'],
            'Interest_Rate': creditScoreRequest['interestRate'],
            'Num_of_Loan': creditScoreRequest['numOfLoan'],
            'Credit_History_Age': creditScoreRequest['creditHistoryAge']
        }
        dataFrame = pd.DataFrame(data, index=[0])
        import os
        filepath = '\ml-model\credit_score.pkl'
        path = os.getcwd() + filepath
        print('DataFrame', dataFrame)
        if not dataFrame.empty:
            if os.path.exists(path):
                file = open(path, 'rb')
                model = pickle.load(file)
                predition = model.predict(dataFrame)
                file.close()
            else:
                print("File not present at desired location")
                return "Machine Learning Model error"
            return json.dumps({
                "status": 200,
                "result": {
                    "Credit_Score": predition[0],
                    "Percentage": 0.5
                }
            })
        else:
            return json.encoder({
                "status": 404,
                "message": "Data for prediction not correct"
            })
