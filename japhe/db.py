import pymysql.cursors
import json

# sudo /opt/lampp/lampp stop

# Connect to the database.
with open('test.json', 'r') as file:
    data = json.load(file)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='mat@1234',
                             db='japhe',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print ("connect successful!!")

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `transactions` (`Receipt_No`, `Completion_Time`, `Details`, `Paid_In`, `Withdrawn`, `Balance`) VALUES (%s, %s, %s, %s, %s, %s)"
        for a in range(len(data['Receipt No.'])):

            try:
                cursor.execute(
                    sql, (data['Receipt No.'][a], data['Completion Time'][a], data['Details'][a], data['Paid In'][a], data['Withdrawn'][a], data['Balance'][a]))

            except:
                print('DB upto date fox')
                break

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `Receipt_No` FROM `transactions` WHERE `Paid_In`=%s"
        cursor.execute(sql, ('500.00',))
        result = cursor.fetchone()
        print(result)
