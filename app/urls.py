from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    ModelTaskViewSet,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r"tasks", ModelTaskViewSet, basename="tasks")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("tasks/list/", login_required(TaskListView.as_view()), name="task_list"),
    path("tasks/create/", login_required(TaskCreateView.as_view()), name="task_create"),
    path(
        "tasks/update/<int:pk>/",
        login_required(TaskUpdateView.as_view()),
        name="task_update",
    ),
    path(
        "tasks/delete/<int:pk>/",
        login_required(TaskDeleteView.as_view()),
        name="task_delete",
    ),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
]
