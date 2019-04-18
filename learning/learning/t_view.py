from django.shortcuts import render
from django.http import HttpResponse
import pymysql
import json

def getNames():
    conn=pymysql.connect("localhost","root","123456","pythondb")
    cursor=conn.cursor()
    cursor.execute("select * from MovieName")
    res=cursor.fetchall()
    cursor.close()
    conn.close()
    return res

def mymain(request):
    context={}
    movieNames=[]
    for i in getNames()[:25]:        
        movieNames.append(i[1])
    context['names']=movieNames
    return render(request,'showNames.html',context)

def mymain2(request):
    context={}
    movieNames=[]
    for i in getNames()[25:50]:
        movieNames.append(i[1])
    context['names']=movieNames
    return render(request,'showNames.html',context)

#返回商家列表
def getStores(request):
    conn=pymysql.connect("localhost","root","123456","androiddb")
    if(request.GET.get("storeId")!=None):     
        sql="select food.*,foodtype.name from product\
    left join food on food.id=product.foodId\
    left join foodtype on foodtype.id=product.typeId\
    where product.storeId="+request.GET.get("storeId")
        cur=conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        res=cur.fetchall()
        cur.close()
        conn.close()
        return HttpResponse(json.dumps(res,ensure_ascii=False))
    else:
        sql="select * from Store"
        cur=conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        res=cur.fetchall()
        cur.close()
        conn.close()
        #将从数据库得到数据转化为json格式   
        return HttpResponse(json.dumps(res,ensure_ascii=False))


#返回商家对应商品列表
def getProducts(request):
    conn=pymysql.connect("localhost","root","123456","androiddb")
    sql="select * from Product where storeId="+request.GET.get("storeId")
    cur=conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql)
    res=cur.fetchall()
    cur.close()
    conn.close()
    return HttpResponse(json.dumps(res,ensure_ascii=False))

#返回服务列表
def getServes(request):
    conn=pymysql.connect("localhost","root","123456","androiddb")
    if(request.GET.get("serveId")!=None):
        sql="select * from Food"
        cur=conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        res=cur.fetchall()
        cur.close()
        conn.close()
        return HttpResponse(json.dumps(res,ensure_ascii=False))
    else:
        sql="select * from Serve"
        cur=conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        res=cur.fetchall()
        cur.close()
        conn.close()
        return HttpResponse(json.dumps(res,ensure_ascii=False))

def getRealServes(request):
    conn=pymysql.connect("localhost","root","123456","androiddb")
    sql="select * from Food"
    cur=conn.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(sql)
    res=cur.fetchall()
    cur.close()
    conn.close()
    return HttpResponse(json.dumps(res,ensure_ascii=False))


def getUser(request):
    #conn=pymysql.connect("localhost","root","123456","androiddb")
    #account=request.POST.get("account")
    #password=request.POST.get("password")
    
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['username']
    return render(request,"test.html")
    '''if(account!=None and password!=None):
        sql="select * from MyUser where account='"+account+\
             "' and password='"+password+"'"
        cur=conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        res=cur.fetchall()
        cur.close()
        conn.close()
        return HttpResponse(json.dumps(res,ensure_ascii=False))
    else:
        sql="insert into MyUser(account,password) values('"+account+\
             "','"+password+"')"
        cur=conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return HttpResponse("success")'''

