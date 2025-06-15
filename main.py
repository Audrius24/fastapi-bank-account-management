from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from uuid import uuid4

app = FastAPI()

class Account(BaseModel):
    id: str
    type: Literal['business', 'personal']
    person_name: str
    address: str

accounts: list[Account] = []

@app.post("/accounts/")
def create_account(account: Account):
    account.id = str(uuid4())
    accounts.append(account)
    return {"message": "Account created", "account": account}

@app.get("/accounts/")
def get_all_accounts():
    return accounts

@app.get("/accounts/{account_id}")
def get_account(account_id: str):
    for acc in accounts:
        if acc.id == account_id:
            return acc
    return {"message": "Account not found"}

@app.delete("/accounts/{account_id}")
def delete_account(account_id: str):
    global accounts
    accounts = [acc for acc in accounts if acc.id != account_id]
    return {"message": "Account deleted"}

@app.get("/")
def read_root():
    return {"Hello": "World"}
