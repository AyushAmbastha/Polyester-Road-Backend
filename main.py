import pymysql
import os
import urllib.request
import auth
import subprocess
from jwt import InvalidTokenError
from app import app
from email.message import EmailMessage
from config import mysql
from flask import jsonify
from flask import flash, request
from datetime import datetime
from flask import Flask, request, redirect, jsonify, send_from_directory
from werkzeug.utils import secure_filename
Transer_Successful = False

@app.route('/inserTransaction', methods=['POST'])
def transactionlog():
	try:
		_json = request.json
		_itemID = int(_json['itemID'])
		_email = int(_json['email'])
		_transactionID = int(_json['transactionID'])
		
		sqlQuery_transactions = "INSERT INTO TRANSACTIONS(TRANSACTION_ID, EMAIL, ITEM_ID) VALUES(%s , %s , %s);"
		bindData1 = (_transactionID, _email, _itemID)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sqlQuery_transactions,bindData1)
		conn.commit()
		respone = jsonify('Transaction logs updated successfully!')
		respone.status_code = 200
		return respone
        
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()



if __name__ == "__main__":
    app.run(port = 5000)
    #For Running on server please specify the host machine IP address
    #app.run(debug=True, host="IP", port=8080)