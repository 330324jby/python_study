from django.shortcuts import render
from django.http import HttpResponse
import pymysql
import json

def getServe(request):
    sql="select * from serve"
    return HttpResponse(commSql(sql))

def getStore(request):
    sql="select * from store"
    return HttpResponse(commSql(sql))

def getFood(request):
    storeId=request.GET.get("storeId")
    if storeId!=None:
        sql="select picName,food.name,mouthSales,price,product.id,\
    foodtype.id tId,foodtype.name tName from product,food,foodtype\
     where product.foodId=food.id and \
        product.typeId=foodtype.id and product.storeId="+storeId
        return HttpResponse(commSql(sql))
    return HttpResponse("请求错误！")

def getUser(request):
    account=request.GET.get("account")
    if account!=None:
        if hasUser(account):
            password=request.GET.get("password")
            if password!=None:
                sql="select * from myuser where account='"+account+"\
    ' and password='"+password+"'"
                res=commSql(sql)
                if res=='[]':
                    return HttpResponse("密码错误！")
                return HttpResponse(res)
            return HttpResponse("请求错误1！")
        return HttpResponse("不存在用户！")
    return HttpResponse("请求错误！")

def hasUser(account):
    sql="select * from myuser where account='"+account+"'"
    if commSql(sql)=='[]':
        return False
    return True

def getShoppingCar(request):
    userId=request.GET.get("userId")
    if userId!=None:
        sql="select shoppingcar.id,shoppingcar.productId,userId,\
    picName,name,mouthSales,price,number from shoppingcar,food,product where\
    shoppingcar.productId=product.id and food.id=product.foodId\
    and userId="+userId
        return HttpResponse(commSql(sql))
    return HttpResponse("请求错误！")

def setUser(request):
    getParams=[request.GET.get("account"),request.GET.get("password")\
               ,request.GET.get("nickName")]
    postParams=[request.POST.get("account"),request.POST.get("password")\
                ,request.POST.get("nickName")]
    
    if request.method=="GET":
        if None==getParams[0]:
            return HttpResponse("请求错误！")
        if hasUser(getParams[0]):
            return HttpResponse("已经存在！")
        if paramsIsNone(getParams):
            return HttpResponse("请求错误！")
        insertsql="insert into myuser(account,password,nickName) values('"\
                     +getParams[0]+"','"+getParams[1]+"','"+getParams[2]+"')"
        if commSql(insertsql)=='[]':
            return HttpResponse("成功！")
        return HttpResponse("失败")
    else:
        if None==postParams[0]:
            return HttpResponse("请求错误！")
        if hasUser(postParams[0]):
            return HttpResponse("已经存在！")        
        if paramsIsNone(postParams):
            return HttpResponse("请求错误！")
        insertsql="insert into myuser(account,password,nickName) values('"\
                     +postParams[0]+"','"+postParams[1]+"','"+postParams[2]+"')"
        return HttpResponse(commSql(insertsql))
        if commInsert(selectsql,insertsql)=='[]':
            return HttpResponse("成功！")
        return HttpResponse("失败")

def insertShoppingCar(request):
    getParams=[request.GET.get("userId"),request.GET.get("productId")\
               ,request.GET.get("number")]
    postParams=[request.POST.get("userId"),request.POST.get("productId")\
               ,request.POST.get("number")]
    if request.method=="GET":
        if paramsIsNone(getParams):
            return HttpResponse("请求错误！")
        insertsql="insert into shoppingcar(userId,productId,number)\
    values("+getParams[0]+","+getParams[1]+","+getParams[2]+")"
        if commSql(insertsql)=="[]":
            sql="select * from shoppingcar where userId='"+getParams[0]+\
                 "'"+" and productId='"+getParams[1]+"'"+" and number='"\
                 +getParams[2]+"'"
            return HttpResponse(commSql(sql))
        return HttpResponse("失败")
    else:
        if paramsIsNone(postParams):
            return HttpResponse("请求错误！")
        insertsql="insert into shoppingcar(userId,productId,number)\
    values("+postParams[0]+","+postParams[1]+","+postParams[2]+")"
        if commSql(insertsql)=="[]":
            sql="select * from shoppingcar where userId='"+postParams[0]+\
                 "'"+" and productId='"+postParams[1]+"'"+" and number='"\
                 +postParams[2]+"'"
            return HttpResponse(commSql(sql))
        return HttpResponse("失败")

def deleteShoppingCar(request):
    carid=request.GET.get("id")
    if carid==None:
        return HttpResponse("请求错误！")
    deletesql="delete shoppingcar where id="+carid
    if commSql(deletesql)=="[]":
        return HttpResponse("成功！")
    return HttpResponse("失败")

def updateShoppingCar(request):
    getParams=[request.GET.get("id"),request.GET.get("number")]
    postParams=[request.POST.get("id"),request.POST.get("number")]
    if request.method=="GET":
        if paramsIsNone(getParams):
            return HttpResponse("请求错误！")
        updatesql="update shoppingcar set number="+getParams[1]\
            +" where id="+getParams[0]
        if commSql(updatesql)=="[]":
            sql="select * from shoppingCar where id="+postParams[0]
            return HttpResponse(commSql(sql))
        return HttpResponse("失败")
    else:
        if paramsIsNone(postParams):
            return HttpResponse("请求错误！")
        updatesql="update shoppingcar set number="+postParams[1]\
            +" where id="+postParams[0]
        if commSql(updatesql)=="[]":
            sql="select * from shoppingCar where id="+postParams[0]
            return HttpResponse(commSql(sql))
        return HttpResponse("失败")

def paramsIsNone(params):
    for p in params:
        if p==None:
            return True
    return False   

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
