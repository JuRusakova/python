# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinslizer(fixture.destroy)
    return fixture

    
 def test_add_group1(app):
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_group(Group(name="name", header="logo",footer="comment"))
    app.return_to_group_page()
    app.logout()


def test_add_group2(app):
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_group(Group(name="", header="", footer=""))
    app.return_to_group_page()
    app.logout()


