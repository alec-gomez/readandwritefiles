import csv

# create reader object-----------------------------------
sales_report = open("salesreport.csv", "w", newline="")
sales = open("sales.csv", "r")

reader = csv.reader(sales)

# skip fields name row----------------------------
next(reader)

# Creation of writer object-----------------------
writer = csv.writer(sales_report, delimiter=",")

# Field names-----------------------
fieldnames = ["Customer", ", Total"]
writer.writerow(fieldnames)

# Dictionary---- something went wrong here ask teacher
id_salary_Dict = {}

# Loop of Customer Name-------------------
for row in reader:
    customer_id = int(row[250])
    subtotal = float(row[3])
    taxAMT = float(row[4])
    Freight = float(row[5])
    total = subtotal + taxAMT + Freight

    if customer_id in id_salary_Dict:
        id_salary_Dict[customer_id] += total
    elif customer_id:
        id_salary_Dict[customer_id] = total
    else:
        id_salary_Dict[customer_id] == customer_id

for cust_id, total in id_salary_Dict.items():
    new_row = [format(cust_id, ">d"), format(total, "<.2f")]
    writer.writerow(new_row)

# close file ----------------------
sales.close()
sales_report.close()
