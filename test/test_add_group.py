# -*- coding: utf-8 -*-

from model.group import Group
import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group2(app):
   app.session.login(username="admin", password="secret")
   app.group.create(Group(name="nhb", header="juyy", footer="fhu"))
   app.session.logout()

def test_add_group3(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()