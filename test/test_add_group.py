# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group2(app):
   app.group.create(Group(name="nhb", header="juyy", footer="fhu"))

def test_add_group3(app):
    app.group.create(Group(name="", header="", footer=""))
