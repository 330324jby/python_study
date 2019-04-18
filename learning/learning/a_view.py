from django.shortcuts import render
from django.http import HttpResponse
import pymysql
import json

def getStore(request):
    sql="select * from store"
    return HttpResponse(commSql(sql))

def getFood(request):
    sql="select * from food"
    return HttpResponse(commSql(sql))

def getProduct(request):
    sql="select * from product"
    return HttpResponse(commSql(sql))

def getShoppingCar(request):
    sql="select * from shoppingcar"
    return HttpResponse(commSql(sql))

def getUser(request):
    sql="select * from myuser"
    return HttpResponse(commSql(sql))

def getServe(request):
    sql="select * from serve"
    return HttpResponse(commSql(sql))

def setUser(request):
    if request.method=="GET":
        sql="select * from myuser where account='"+request.GET.get\
             ("account")+"'"
        if commSql(sql)=='[]':
            sql="insert into myuser(account,password,nickName) values('"\
                 +request.GET.get("account")+"','"+request.GET.get\
                 ("password")+"','"+request.GET.get("nickName")+"')"
        return HttpResponse(commSql(sql))
    else:
        sql="select * from myuser where account='"+request.POST.get\
             ("account")+"'"
        if commSql(sql)=='[]':
            sql="insert into myuser(account,password,nickName) values('"\
                 +request.POST.get("account")+"','"+request.POST.get\
                 ("password")+"','"+request.POST.get("nickName")+"')"
        return HttpResponse(commSql(sql))

def setShoppingCar(request):
    #如果数据库有相同数据，则数量加一，否则插入
    if request.method=="GET":
        sql="select * from shoppingcar where userId="+request.GET.get\
             ("userId")+" and productId="+request.GET.get("productId")
        if commSql(sql)=='[]':
            sql="insert into shoppingcar(userId,productId) values("+request\
                 .GET.get("userId")+","+request.GET.get("productId")+")"
        return HttpResponse(commSql(sql))
    else:
        sql="select * from shoppingcar where userId="+request.POST.get\
             ("userId")+" and productId="+request.POST.get("productId")
        if commSql(sql)=='[]':
            sql="insert into shoppingcar(userId,productId) values("+request\
                 .POST.get("userId")+","+request.POST.get("productId")+")"
        return HttpResponse(commSql(sql))

def commSql(sql):
    conn=pymysql.connect("localhost","root","123456","androiddb")
    cur=conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql)
    conn.commit()
    res=cur.fetchall()
    cur.close()
    conn.close()
    return json.dumps(res,ensure_ascii=False)

#print(commSql("insert into myuser(account) values('1')")=='[]')
