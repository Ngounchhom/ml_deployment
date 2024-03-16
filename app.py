from flask import Flask, request, jsonify
import json
app = Flask(__name__)
from flask_expects_json import expects_json
from service.credit_score_service import CreditScoreService
@app.route('/')
def hello_world():  # put application's code here
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

schema = {
  "type": "object",
  "properties": {
    "month": { "type": "double"},
    "age": { "type": "integer" },
    "occupation": { "type": "string" },
    "annualIncome": { "type": "string" },
    "monthlyInhandSalary": { "type": "string" },
    "numBankAccount": { "type": "string" },
    "interestRate": { "type": "string" },
    "numOfLoan": { "type": "string" },
    "creditHistoryAge": { "type": "string" }
  },
  "required": [
      "month",
      "age",
      "occupation",
      "annualIncome",
      "monthlyInhandSalary",
      "numBankAccount",
      "interestRate",
      "numOfLoan",
      "creditHistoryAge"]
}
@app.route('/credit-score', methods=['POST'])
# @expects_json(schema)
def preditCreditScore():
    creditScoreService = CreditScoreService()
    creditScoreRequest = json.loads(request.data)
    # return creditScoreRequest
    print('Kingdom', type(creditScoreRequest))
    print('Kingdom', creditScoreRequest)
    print('Kingdom', creditScoreRequest['month'])
    return creditScoreService.prediction(creditScoreRequest)
if __name__ == '__main__':
    app.run()

#%%
