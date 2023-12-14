import pytest
import requests
from uuid import UUID, uuid4
from datetime import datetime

base_url = 'http://localhost:80/'


def test_allow_users_get():
    res = requests.get(base_url).json()
    assert(res == "Allow users: id-1:User1; id-2:User2; id-3:User3")


def test_cancel_users_get():
    res = requests.get(base_url+'cancel_users').json()
    assert(res == "Cancel users: id-4:User4; id-5:User5; id-6:User6")


test_allow_users_get()
test_cancel_users_get()