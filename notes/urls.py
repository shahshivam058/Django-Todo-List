from django.contrib import admin
from django.urls import path
from .views import Notelist,finished_item,delete_item,Recover_item,noteform

app_name = "Notes"

urlpatterns = [
    path("",Notelist,name="notelist"),
    path("form",noteform,name="noteform"),
    path("finishitem/<int:id>",finished_item,name="finished_item"),
    path("recoveritem/<int:id>",Recover_item,name="Recover_item"),
    path("deleteitem/<int:id>",delete_item,name="delete_item"),
]



