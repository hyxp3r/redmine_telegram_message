import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv
load_dotenv("/home/e.n.ermakov@university.local/Documents/VS_Code/Python/Redmine/.env")

def telegram_bot_sendtext(bot_message):

    bot_token = os.environ.get("bot_token")
    bot_chatID = os.environ.get("bot_chatID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + bot_message

    response = requests.get(send_text)

    # return response.json()

base_url = os.environ.get("base_url")
api_key = os.environ.get("api_key")

limit = 50
offset = 0
i = 0
j = 0
x3 = 0
list_r3 = list()
all_issues = []

# Ne soglasovano nikem
r_1 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%21*&f%5B%5D=cf_43&op%5Bcf_43%5D=%21*&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_2 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%3D&v%5Bcf_26%5D%5B%5D=%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%BE%D0%B2%D0%B0%D0%BD%D0%BE&f%5B%5D=cf_43&op%5Bcf_43%5D=%21*&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_3 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit={limit}&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%3D&v%5Bcf_26%5D%5B%5D=%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%BE%D0%B2%D0%B0%D0%BD%D0%BE&f%5B%5D=cf_43&op%5Bcf_43%5D=%21*&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_4 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%3D&v%5Bcf_26%5D%5B%5D=%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%BE%D0%B2%D0%B0%D0%BD%D0%BE&f%5B%5D=cf_43&op%5Bcf_43%5D=%21*&f%5B%5D=cf_27&op%5Bcf_27%5D=%3D&v%5Bcf_27%5D%5B%5D=%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%BE%D0%B2%D0%B0%D0%BD%D0%BE&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()

r_6 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_7 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%21*&f%5B%5D=cf_2&op%5Bcf_2%5D=%3D&v%5Bcf_2%5D%5B%5D=%D0%98%D0%AF+%28%D0%A4%D0%91%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%9C%D0%B8%D0%95%D0%9D+%28%D0%A4%D0%91%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%A4%D0%92%D0%B8%D0%A1+%28%D0%A4%D0%91%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%A4%D0%B8%D0%93%D0%9D+%28%D0%A4%D0%91%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%AD%D0%A2+%28%D0%A4%D0%91%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%94%D0%B5%D0%BA%D0%B0%D0%BD%D0%B0%D1%82+%D0%A4%D0%91%D0%9F&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_8 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%21*&f%5B%5D=cf_2&op%5Bcf_2%5D=%3D&v%5Bcf_2%5D%5B%5D=%D0%98%D0%A2+%28%D0%A4%D0%93%D0%A1%29&v%5Bcf_2%5D%5B%5D=%D0%9C%D0%AD%D0%9C%D0%9E%D0%B8%D0%9F+%28%D0%A4%D0%93%D0%A1%29&v%5Bcf_2%5D%5B%5D=%D0%9E%D0%A4+%28%D0%A4%D0%93%D0%A1%29&v%5Bcf_2%5D%5B%5D=%D0%9F%D0%98+%28%D0%A4%D0%93%D0%A1%29&v%5Bcf_2%5D%5B%5D=%D0%9F%D0%9F%D0%9F+%28%D0%A4%D0%93%D0%A1%29&v%5Bcf_2%5D%5B%5D=%D0%A0%D0%AD%D0%B8%D0%A3+%28%D0%A4%D0%93%D0%A1%29&v%5Bcf_2%5D%5B%5D=%D0%A1%D0%BE%D1%86+%28%D0%A4%D0%93%D0%A1%29&v%5Bcf_2%5D%5B%5D=%D0%A1%D1%82%D0%B0%D1%82+%28%D0%A4%D0%93%D0%A1%29&v%5Bcf_2%5D%5B%5D=%D0%AD%D0%91%D0%B8%D0%A3%D0%9F+%28%D0%A4%D0%93%D0%A1%29&v%5Bcf_2%5D%5B%5D=%D0%94%D0%B5%D0%BA%D0%B0%D0%BD%D0%B0%D1%82+%D0%A4%D0%93%D0%A1&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_9 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%21*&f%5B%5D=cf_2&op%5Bcf_2%5D=%3D&v%5Bcf_2%5D%5B%5D=%D0%91%D0%B2%D0%A1%D0%A3+%28%D0%A4%D0%9A%D0%AD%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%98%D0%90%D0%9E%D0%B8%D0%91%D0%A3+%28%D0%A4%D0%9A%D0%AD%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%98%D0%B8%D0%9F+%28%D0%A4%D0%9A%D0%AD%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%9A%D0%A3%D0%B8%D0%A4+%28%D0%A4%D0%9A%D0%AD%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%9C%D0%A0%D0%B8%D0%A1%D0%9E+%28%D0%A4%D0%9A%D0%AD%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%A4%D0%A0%D0%B8%D0%A4%D0%98+%28%D0%A4%D0%9A%D0%AD%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%AD%D0%A2%D0%B8%D0%A3%D0%9F+%28%D0%A4%D0%9A%D0%AD%D0%9F%29&v%5Bcf_2%5D%5B%5D=%D0%94%D0%B5%D0%BA%D0%B0%D0%BD%D0%B0%D1%82+%D0%A4%D0%9A%D0%AD%D0%9F&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_10 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%21*&f%5B%5D=cf_2&op%5Bcf_2%5D=%3D&v%5Bcf_2%5D%5B%5D=%D0%90%D0%A4%D0%B8%D0%9A%D0%9F+%28%D0%AE%D0%A4%29&v%5Bcf_2%5D%5B%5D=%D0%93%D0%B8%D0%9F%D0%9F+%28%D0%AE%D0%A4%29&v%5Bcf_2%5D%5B%5D=%D0%A2%D0%B8%D0%98%D0%93%D0%B8%D0%9F+%28%D0%AE%D0%A4%29&v%5Bcf_2%5D%5B%5D=%D0%A3%D0%9F%D0%B8%D0%9D%D0%91+%28%D0%AE%D0%A4%29&v%5Bcf_2%5D%5B%5D=%D0%94%D0%B5%D0%BA%D0%B0%D0%BD%D0%B0%D1%82+%D0%AE%D0%A4&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_11 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=cf_3&op%5Bcf_3%5D=%3D&v%5Bcf_3%5D%5B%5D=1%09%D0%9F%D1%80%D0%B8%D0%B5%D0%BC%D0%BD%D0%B0%D1%8F+%D0%BA%D0%B0%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F+%D0%B8+%D0%BF%D1%80%D0%BE%D1%84%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0+%D1%81+%D0%B0%D0%B1%D0%B8%D1%82%D1%83%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B0%D0%BC%D0%B8&v%5Bcf_3%5D%5B%5D=7%09%D0%92%D0%BD%D0%B5%D1%88%D0%BD%D0%B8%D0%B5+%D1%81%D0%B2%D1%8F%D0%B7%D0%B8&v%5Bcf_3%5D%5B%5D=8%09%D0%9C%D0%B0%D1%80%D0%BA%D0%B5%D1%82%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B4%D0%B5%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C&f%5B%5D=tracker_id&op%5Btracker_id%5D=%21&v%5Btracker_id%5D%5B%5D=11&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&c%5B%5D=cf_27&group_by=tracker&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_12 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=cf_3&op%5Bcf_3%5D=%3D&v%5Bcf_3%5D%5B%5D=3%09%D0%9E%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F+%D0%B8+%D1%80%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5+%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE+%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F&f%5B%5D=tracker_id&op%5Btracker_id%5D=%21&v%5Btracker_id%5D%5B%5D=11&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&c%5B%5D=cf_27&group_by=tracker&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_13 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=cf_3&op%5Bcf_3%5D=%3D&v%5Bcf_3%5D%5B%5D=4%09%D0%92%D0%BE%D1%81%D0%BF%D0%B8%D1%82%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0+%D1%81+%D0%BE%D0%B1%D1%83%D1%87%D0%B0%D1%8E%D1%89%D0%B8%D0%BC%D0%B8%D1%81%D1%8F+%D0%B8+%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F+%D0%BC%D0%BE%D0%BB%D0%BE%D0%B4%D1%91%D0%B6%D0%BD%D0%BE%D0%B9+%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B8&v%5Bcf_3%5D%5B%5D=9%09%D0%98%D0%BD%D0%BD%D0%BE%D0%B2%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%B0%D1%8F+%D0%B8+%D0%BF%D1%80%D0%B5%D0%B4%D0%BF%D1%80%D0%B8%D0%BD%D0%B8%D0%BC%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F+%D0%B4%D0%B5%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C&v%5Bcf_3%5D%5B%5D=22%09%D0%A1%D0%BE%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0+%D1%81+%D0%BE%D0%B1%D1%83%D1%87%D0%B0%D1%8E%D1%89%D0%B8%D0%BC%D0%B8%D1%81%D1%8F+%D0%B8+%D1%81%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D0%BA%D0%B0%D0%BC%D0%B8&f%5B%5D=tracker_id&op%5Btracker_id%5D=%21&v%5Btracker_id%5D%5B%5D=11&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&c%5B%5D=cf_27&group_by=tracker&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_14 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=cf_3&op%5Bcf_3%5D=%3D&v%5Bcf_3%5D%5B%5D=2%09%D0%9E%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F+%D0%B8+%D1%80%D0%B0%D0%B7%D0%B2%D0%B8%D1%82%D0%B8%D0%B5+%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE+%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F&v%5Bcf_3%5D%5B%5D=5%09%D0%92%D0%B7%D0%B0%D0%B8%D0%BC%D0%BE%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5+%D0%BF%D0%BE+%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D0%B0%D0%BC+%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B8+%D0%B8+%D1%82%D1%80%D1%83%D0%B4%D0%BE%D1%83%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%B0+%D0%BE%D0%B1%D1%83%D1%87%D0%B0%D1%8E%D1%89%D0%B8%D1%85%D1%81%D1%8F&v%5Bcf_3%5D%5B%5D=17%09%D0%98%D0%BD%D1%84%D1%80%D0%B0%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0%2C+%D1%81%D1%80%D0%B5%D0%B4%D0%B0+%D0%B8+%D0%BC%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE-%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5+%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5&f%5B%5D=tracker_id&op%5Btracker_id%5D=%21&v%5Btracker_id%5D%5B%5D=11&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&c%5B%5D=cf_27&group_by=tracker&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_15 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=8&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&c%5B%5D=cf_27&group_by=tracker&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_16 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=cf_3&op%5Bcf_3%5D=%3D&v%5Bcf_3%5D%5B%5D=6%09%D0%9D%D0%B0%D1%83%D1%87%D0%BD%D0%BE-%D0%B8%D1%81%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F+%D0%B4%D0%B5%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&c%5B%5D=cf_27&c%5B%5D=cf_26&group_by=tracker&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
r_17 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit=1&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=tracker_id&op%5Btracker_id%5D=%3D&v%5Btracker_id%5D%5B%5D=11&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&c%5B%5D=cf_27&group_by=tracker&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()

x1 = str(r_1['total_count'])
x2 = str(r_2['total_count'])

x4 = str(r_4['total_count'])
x5 = 0
x6 = str(r_6['total_count'])
x7 = str(r_7['total_count'])
x8 = str(r_8['total_count'])
x9 = str(r_9['total_count'])
x10 = str(r_10['total_count'])
x11 = str(r_11['total_count'])
x12 = str(r_12['total_count'])
x13 = str(r_13['total_count'])
x14 = str(r_14['total_count'])
x15 = str(r_15['total_count'])
x16 = str(r_16['total_count'])
x17 = str(r_17['total_count'])


pages = r_3['total_count'] // limit + 1


#list_r3=r_3['issues']
list_r4=r_4['issues'][0]['estimated_hours']

print(list_r4)
#fk_6 = list_r3[15]['custom_fields'][7]#['value']

#print(fk_6)



for page in range(pages):
    r_3 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit={limit}&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%3D&v%5Bcf_26%5D%5B%5D=%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%BE%D0%B2%D0%B0%D0%BD%D0%BE&f%5B%5D=cf_43&op%5Bcf_43%5D=%21*&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
    list_r3=r_3['issues']
    
    for i in range(len(list_r3)) :
        for j in range(len(list_r3[i]['custom_fields'])):
           # print(i, j)
            if str(list_r3[i]['custom_fields'][j]['id']) == '4':
                try:
                    fk_3 = int(list_r3[i]['custom_fields'][j]['value'])
                except:
                    fk_3 = 0
                try:
                    fk_4 = int(list_r3[i]['custom_fields'][j+1]['value'])
                except: 
                    fk_4 = 0
                try:
                    fk_5 = int(list_r3[i]['custom_fields'][j+2]['value'])
                except: 
                    fk_5 = 0
                try:
                    fk_6 = int(list_r3[i]['custom_fields'][j+3]['value'])
                except:
                    fk_6 = 0

                if fk_3+fk_4+fk_5+fk_6 != 0:
                    x3 += 1
                else:
                    pass

                break

    time.sleep(1)
    offset = page * limit

for page in range(pages):
    r_4 = requests.get(f"{base_url}/issues.json?key={api_key}&offset={offset}&limit={limit}&utf8=%E2%9C%93&set_filter=1&sort=id%3Adesc&f%5B%5D=cf_26&op%5Bcf_26%5D=%3D&v%5Bcf_26%5D%5B%5D=%D0%A1%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%BE%D0%B2%D0%B0%D0%BD%D0%BE&f%5B%5D=cf_43&op%5Bcf_43%5D=%21*&f%5B%5D=cf_27&op%5Bcf_27%5D=%21*&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=cf_2&c%5B%5D=subject&c%5B%5D=cf_4&c%5B%5D=cf_5&c%5B%5D=cf_6&c%5B%5D=cf_7&c%5B%5D=estimated_hours&group_by=&t%5B%5D=estimated_hours&t%5B%5D=cf_4&t%5B%5D=cf_5&t%5B%5D=cf_6&t%5B%5D=cf_7&t%5B%5D=").json()
    list_r4=r_4['issues']
    for i in range(len(list_r4)) :
        try:
            hour = int(list_r4[i]['estimated_hours'])
        except:
            hour = 0
        for j in range(len(list_r4[i]['custom_fields'])):
           # print(i, j)
            if str(list_r4[i]['custom_fields'][j]['id']) == '4':
                try:
                    fk_3 = int(list_r4[i]['custom_fields'][j]['value'])
                except:
                    fk_3 = 0
                try:
                    fk_4 = int(list_r4[i]['custom_fields'][j+1]['value'])
                except: 
                    fk_4 = 0
                try:
                    fk_5 = int(list_r4[i]['custom_fields'][j+2]['value'])
                except: 
                    fk_5 = 0
                try:
                    fk_6 = int(list_r4[i]['custom_fields'][j+3]['value'])
                except:
                    fk_6 = 0

                if fk_3+fk_4+fk_5+fk_6 <= 5000 and hour <=25:
                    x5 += 1
                else:
                    pass
                break

    time.sleep(1)
    offset = page * limit
    





text = f'''
<b>Ежедневный отчет по задачам в Трекере</b>

- <b>{x1}</b> задач не согласовано никем.
- <b>{x2}</b> задач согласовано только деканами, из них <b>{x3}</b> требуют финансирование. 
- <b>{x4}</b> задач без визы ректора, из них <b>{x5}</b> задач может согласовать ПАО. 

На согласовании у деканов <b>{x6}</b> задач: ФБП - <b>{x7}</b>, ФГС: - <b>{x8}</b>, ФКЭП - <b>{x9}</b>, ЮФ - <b>{x10}</b>.

На согласовании у АУП: 
- <b>{x11}</b> - Калинин ДС
- <b>{x12}</b>  - Коложвари ЭС
- <b>{x13}</b>  - Обуховский ДА
- <b>{x14}</b>  - Родионова ЗВ
- <b>{x15}</b>  - Павлова ЕВ
- <b>{x16}</b>  - Куницын ДВ / Мельников ВС
- <b>{x17}</b>  - Носырева ЮИ
'''

#print(text)

telegram_bot_sendtext(text)

