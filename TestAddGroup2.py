# -*- coding: utf-8 -*-

from group2 import Group
import pytest
from application2 import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group2(app):
   app.login(username="admin", password="secret")
   app.create_group(Group(name="nhb", header="juyy", footer="fhu"))
   app.logout()

def test_add_group3(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
