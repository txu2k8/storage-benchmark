#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file  : download.py
@Time  : 2020/11/23 14:24
@Author: Tao.Xu
@Email : tao.xu2008@outlook.com
"""

from six.moves import urllib
import os
import sys


def download(url_list, save_dir):
    """
    Download files by URL address
    :param url_list: The to download-files url list
    :param save_dir: save the download files to a local dir
    :return:
    """
    for url, index in zip(url_list, range(len(url_list))):
        filename = url.split('/')[-1]
        save_path = os.path.join(save_dir, filename)
        if os.path.exists(save_path):
            print('\n{} already exist, skip'.format(save_path))
            continue
        urllib.request.urlretrieve(url, save_path)
        sys.stdout.write('\r>> Downloading %.1f%%' % (float(index + 1) / float(len(url_list)) * 100.0))
        sys.stdout.flush()
    print('\nSuccessfully downloaded')


def get_file_urls(url_txt):
    """
    Get the url list from a txt file
    :param url_txt: url txt-file full path
    :return:
    """

    url_list = []
    file = open(url_txt, 'r')
    for line in file.readlines():
        line = line.strip()
        url_list.append(line)
    file.close()
    return url_list


if __name__ == '__main__':
    # file_url_txt = 'file_url_txt.txt'
    # urls = get_file_urls(file_url_txt)
    local_dir = '/tmp'
    download(['https://www.samba.org/ftp/tridge/dbench/README'], local_dir)
