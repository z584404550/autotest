# -*- coding:utf-8 -*-
import requests, time, sys, re
import urllib, zlib#,
import pymysql
import unittest
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from apitest.celery import app
from time import sleep


@app.task
def hello_world():
    print('已运行')
