from behave import *
from archicad import ACConnection
import pywinauto

conn = ACConnection.connect()
assert conn
acc = conn.commands
act = conn.types
app = pywinauto.Application().connect(path='ARCHICAD.exe')
dlg=app["Új terv - ARCHICAD 24"]

@given("Archicad is running")
def run(context):
    a=acc.IsAlive()
    assert a

def wallcount():
    e=acc.GetElementsByType("Wall")
    return len(e)

@given(u'there is no any exist walls')
def step_impl(context):
    assert wallcount() == 0

@when(u'By command build the walls')
def step_impl(context):
    dlg.click_input(coords=(500,500))
    dlg.click_input(coords=(900,500))
    dlg.minimize()

@then(u'The wall should be build')
def step_impl(context):
    assert wallcount() > 0
    #dlg.type_keys("^z")

@given(u"The window submenu is selected")
def step_impl(context):
    d=dlg.menu_select("Tervezés->#0->#13")

def windowcount():    
    e=acc.GetElementsByType("Window")
    return len(e)

@when(u'Click on the choosen wall')
def step_impl(context):
    dlg.click_input(coords=(700,500))
    dlg.click_input(coords=(680,480))

@then(u'Window is on the wall')
def step_impl(context):
    assert windowcount()>0