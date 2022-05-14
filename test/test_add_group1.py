# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinаlizer(fixture.destroy)
    return fixture

    
 def test_add_group1(app):
    app.login(username="admin", password="secret")
    app.create(Group(name="name", header="logo", footer="comment"))
    app.logout()


def test_add_group2(app):
    app.login(username="admin", password="secret")
    app.create(Group(name="", header="", footer=""))
    app.logout()


