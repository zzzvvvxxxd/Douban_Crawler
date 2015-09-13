#! /usr/bin/env python2.7
# coding=utf-8
__author__ = 'bulu_dog'
import requests
from bs4 import BeautifulSoup

# http://book.douban.com/subject_search?search_text=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&cat=1001
URL = 'http://book.douban.com/subject_search'

def search_book(query, page):
    """
    search book on book.douban.com and save these book's info
    :param query: query string
    :param page: the num of page
    :return: True of False
    """
    params = {
        'cat':1001,
        'search_text':query,
        'start':page * 15
    }
    r = requests.get(URL, params=params)
    soup = BeautifulSoup(r.content, 'lxml')

if __name__ == '__main__':
    search_book(u'机器学习', 0)