#! /usr/bin/env python2.7
# coding=utf-8
__author__ = 'bulu_dog'

from douban_util.movie import search_for_movie_cat

for item in search_for_movie_cat('星球大战'):
    print item