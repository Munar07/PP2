import re
import json

with open("raw.txt", encoding="utf-8") as f:
    receipt = f.read()

raw_prices = re.findall(r"\d[\d\s\n]*,\d{2}", receipt)
prices = [float(p.replace(" ", "").replace("\n", "").replace(",", ".")) for p in raw_prices]

product_pattern = re.compile(r"\d+\.\s*(.+?)\n\d+,\d+\s*x\s*\d[\d\s\n]*,\d{2}")
products = product_pattern.findall(receipt)

total_match = re.search(r"ИТОГО:\s*(\d[\d\s]*,\d{2})", receipt)
total_amount = float(total_match.group(1).replace(" ", "").replace(",", ".")) if total_match else sum(prices)

datetime_match = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", receipt)
date, time = datetime_match.groups() if datetime_match else ("", "")

payment_match = re.search(r"Банковская карта:\s*(\d[\d\s]*,\d{2})", receipt)
payment_method = "Card" if payment_match else "Cash"
payment_amount = float(payment_match.group(1).replace(" ", "").replace(",", ".")) if payment_match else total_amount

parsed_receipt = {
    "products": products,
    "prices": prices,
    "total_amount": total_amount,
    "date": date,
    "time": time,
    "payment_method": payment_method,
    "payment_amount": payment_amount
}

print(json.dumps(parsed_receipt, ensure_ascii=False, indent=2))