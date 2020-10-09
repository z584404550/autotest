from django.shortcuts import render
from django.http import HttpResponseRedirect  # 加入引用
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.clickjacking import xframe_options_exempt
from djcelery.models import PeriodicTask, CrontabSchedule, IntervalSchedule
from .models import ApiTest, ApiStep
import pymysql
# Create your views here.


def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password error'})

    # else:
    # context = {}
    # return render(request, 'login.html', context)
    return render(request, 'login.html')


@xframe_options_exempt
def home(request):
    return render(request, "home.html")


def left(request):
    return render(request, "left.html")


# 接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apitestid = request.GET.get('apitest.id', None)
    apitest = ApiTest.objects.get(id=apitestid)
    apistep_list = ApiStep.objects.all()
    return render(request, "apistep_manage.html", {"user": username, "apitest": apitest, "apisteps": apistep_list})


# 搜索功能
@login_required
def apisearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录 session
    search_apitestname = request.GET.get("apitestname", "")
    apitest_list = ApiTest.objects.filter(apitestname__icontains=search_apitestname)
    return render(request, 'apitest_manage.html', {"user": username, "apitests": apitest_list})


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


# 流程接口管理
@login_required
def apitest_manage(request):
    apitest_list = ApiTest.objects.all()  # 获取所有接口测试用例
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    paginator = Paginator(apitest_list, 10)  # 生成 paginator 对象，设置每页显示 10 条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
    currentpage = int(page)  # 把获取的当前页码数转换成整数类型
    apis_count = ApiTest.objects.all().count()  # 统计产品数
    try:
        apitest_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        apitest_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
    except EmptyPage:
        apitest_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，则显示最后一页内容
    return render(request, "apitest_manage.html", {"user": username, "apitests": apitest_list,
                                                   "apiscounts": apis_count})  # 定义流程接口数据的变量并返回到前端


def welcome(request):
    return render(request, "welcome.html")


# 任务计划
@login_required
def periodic_task(request):
    username = request.session.get('user', '')
    task_list = PeriodicTask.objects.all()
    task_count = PeriodicTask.objects.all().count()  # 统计数
    periodic_list = IntervalSchedule.objects.all()  # 周期任务（如每隔 1 小时执行 1 次）
    crontab_list = CrontabSchedule.objects.all()  # 定时任务（如某年某月某日的某时，每天的某时）
    paginator = Paginator(task_list, 5)  # 生成 paginator 对象,设置每页显示 5 条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数,默认为第 1 页
    currentpage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        task_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        task_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
    except EmptyPage:
        task_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，# 则显示最后一页内容
    return render(request, "periodic_task.html", {"user": username, "tasks": task_list, "taskcounts": task_count,
                                                  "periodics": periodic_list, "crontabs": crontab_list})


# 搜索功能
@login_required
def tasksearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    search_name = request.GET.get("task", "")
    task_list = PeriodicTask.objects.filter(task__icontains=search_name)
    periodic_list = IntervalSchedule.objects.all()  # 周期任务（如每隔 1 小时执行 1 次）
    crontab_list = CrontabSchedule.objects.all()  # 定时任务（如某年某月某日的某时，每# 天的某时）
    return render(request, 'periodic_task.html', {"user": username, "tasks": task_list,
                                                  "periodics": periodic_list, "crontabs": crontab_list})


# 测试报告
@login_required
def test_report(request):
    username = request.session.get('user', '')
    apis_list = ApiStep.objects.all()
    apis_count = ApiStep.objects.all().count()  # 统计接口数
    db = pymysql.connect(user='root', db='autotest', passwd='123456', host='127.0.0.1')
    cursor = db.cursor()
    sql1 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=1'
    aa = cursor.execute(sql1)
    apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
    sql2 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=0'
    bb = cursor.execute(sql2)
    apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    db.close()
    return render(request, "report.html", {"user": username, "apiss": apis_list, "apiscounts": apis_count,
                                           "apis_pass_counts": apis_pass_count,
                                           "apis_fail_counts": apis_fail_count})  # 把值赋给apiscounts变量
