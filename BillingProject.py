import mysql.connector as sql
import random
conn=sql.connect(host='localhost',user='root',passwd='dps123',database='grocery_shop')
if conn.is_connected():
    c=conn.cursor()

while (True):
    print('''
                    ==========GROCERY SHOP MANAGMENT SYSTEM==========
                    ''')
    print('''
                    ::::Select Your Choice::::

                    1.!!!!!!!!~PLACE AN ORDER~!!!!!!!!

                    2.Add Product Record

                    3.Add Customer Records

                    4.Add Worker Records

                    5.View Customer Records

                    6.View Product Records

                    7.View Worker Records

                    8.Details Of One Customer

                    9.Details Of One Product

                    10.Details Of One Worker

                    11.Purchase From Supplier
                    ----------------------
                    12.EXIT

               ''')

    choice=int(input('===:ENTER YOUR CHOICE:=== '))
#customer
    if choice==3:
            name=input('Enter Name:')
            age=int(input('Enter Age:'))
            sex=input ('Enter Your Sex(M/F);')
            phone_no=int(input('Enter Phone Number:'))                        
            sql_insert="insert into customer_details(c_name,c_age,sex,phone_no) values(%s,%s,%s,%s)"
            data=[name,age,sex,phone_no]
            c.execute(sql_insert,data)
            conn.commit()
            print('-----Data Is Updated-----')
#product
    if choice==2:
            pa_name=input('Enter  Product Name:')
            pa_cost=int(input ('Enter Product Cost(in riyal):'))
            pa_stock=int(input('Enter stock:'))
            query=('insert into product_details(p_name,p_cost,stock) values(%s,%s,%s)')
            d=[pa_name,pa_cost,pa_stock]
            c.execute(query,d)
            conn.commit()
            print('-----Data Is Updated-----')
    elif choice==1:
        l1=[]
        l2=[]
        while (True):
            ch=str(input('Add Another Item?(yes/no): '))
            if ch=='yes':
                p_name=input('Enter  Product Name=')
                p_quantity=int(input ('Enter Product Quantity='))
                c.execute("select p_cost,stock from product_details where p_name='"+p_name+"'")
                stok=c.fetchall()
                l1.append(p_name)
                lis=stok[0]
                b=lis[0]
                a=p_quantity*b
                l2.append(a)
                print(l1,l2)
                st=lis[1]
                st=st-p_quantity
                c.execute("update product_details set stock=%s where p_name='"+p_name+"'",[st])
                conn.commit()
            if ch=='no':
                        print(l1,l2)
                        print('''
             Your Bill Number Is: ''',random.randint(10000,10000000000))
                        print('TOTAL AMOUNT=',sum(l2))
                        print('Items Purchased: ')
                        for i in l1:
                                print(i)
                        break
    elif choice==4:
            worker_name=input('Enter Worker Name=')
            worker_work=input('Enter Worker Work=')
            worker_age=int(input('Enter Worker Age='))
            worker_salary=float(input('Enter Worker Salary='))
            phone_no =int(input('Enter Worker Phone Number='))
            sql_insert="insert into worker_details values(" "'"+(worker_name)+"'," "'"+(worker_work)+"',"+str(worker_age)+","+str(worker_salary)+","+str(phone_no)+ ")"
            c.execute(sql_insert)
            conn.commit()
            print('-----Data Is Updated-----')
    elif choice==5:
            t=conn.cursor()
            t.execute('select*from customer_details')
            record=t.fetchall()
            for i in record:
                print(i)            
    elif choice==6:
            t=conn.cursor()
            t.execute('select*from product_details')
            record=t.fetchall()
            for i in record:
                print(i)
        
    elif choice==7:
            t=conn.cursor()
            t.execute('select*from worker_details')
            record=t.fetchall()
            for i in record:
                print(i)
    elif choice==8:
            a=str(input('Enter Customer Name:'))
            t='select*from customer_details where c_name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
    elif choice==9:
       a=str(input('Enter Product_Name:'))
       t='select*from product_details where p_name=("{}")'.format(a)
       c.execute(t)
       v=c.fetchall()
       for i in v:
             print(v)
    elif choice==10:
            a=str(input('Enter Worker Name:'))
            t='select*from worker_details where w_name=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
    elif choice==11:
        l3=[]
        x=str(input('Enter Product Name To Restock: '))
        query='select stock from product_details where p_name="'+x+'"'
        c.execute(query)
        f=c.fetchall()
        print('Current Stock of ',x,' is ',f)
        y=int(input('Enter Quantity Bought:'))      
        lis=f[0]
        b=lis[0]
        b=b+y
        c.execute("update product_details set stock=%s where p_name='"+x+"'",[b])
        c.execute(query)
        new_stok=c.fetchall()
        print('Stock Of Product ',x,' is now ',new_stok)
        conn.commit()
        
    elif choice==12:
            exit()
            break