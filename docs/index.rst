.. humanstxt documentation master file, created by
   sphinx-quickstart on Sat May 25 23:37:51 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Humanstxt
=====================================

Humanstxt is a python library for dealing with humans.txt.

.. note:: Humanstxt only works with vailed humans.txt ( like template in http://humanstxt.org/Standard.html)

Quickstart
------------

Using humanstxt is quite simple.You can use :func:`parse` to turn humans.txt text into :class:`HumansTxt`
and dealing with it like a dict ::

        from humanstxt import parse

        txt = """
        /* TEAM */
            Founder & Developer: Jacky Chan
            Contact: linux_china [at] hotmail.com
            Weibo: @linux_china
            Blog: http://intellij.org.cn/blog
            From: HangZhou, ZheJiang, China
            University: Beijing Institute of Technology
            Degree: Bachelor

        /* THANKS */
            humans.txt Founder: Abel Cabans
            Site: http://www.humanstxt.org

        /* SITE */
            Last update: 2013/01/23
            Language: Chinese
            Doctype: HTML5
            Standards: HTML5, CSS3
            Components: RequireJS, JQuery, Backbone, BootStrap
            Software: ImageMagick, PhantomJS
            IDE: IntelliJ IDEA

                __  __                                _______  ________
               / / / /_  ______ ___  ____ _____  ____/_  __/ |/ /_  __/
              / /_/ / / / / __ `__ \/ __ `/ __ \/ ___// /  |   / / /
             / __  / /_/ / / / / / / /_/ / / / (__  )/ /  /   | / /
            /_/ /_/\__,_/_/ /_/ /_/\__,_/_/ /_/____//_/  /_/|_|/_/
        """

        humanstxt = parse(txt)

        print(humanstxt.keys())  # ['team', 'thanks', 'site', 'description']

        print(humanstxt["team"]["Contact"])  # linux_china@hotmail.com

        print(str(humanstxt))  # the same as ``txt`` above


.. attention::  Humanstxt will replace ``[at]`` with ``@`` ( ``whtsky [at] gmail.com`` => ``whtsky@gmail.com`` )
.. note::  You can turn a :class:`HumansTxt` into a vailed humans.txt text via ``str`` .

API
------

.. module:: humanstxt

.. autofunction:: parse
.. autoclass:: HumansTxt
