from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import TaskForm
from .models import ModelTask
from .serializers import ModelTaskSerializer
from .tasks import send_task_notification


class ModelTaskViewSet(viewsets.ModelViewSet):
    queryset = ModelTask.objects.all()
    serializer_class = ModelTaskSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            task = ModelTask.objects.get(id=response.data["id"])
            send_task_notification.delay(
                task.email,
                "Tarea creada",
                f"La tarea '{task.title}' ha sido creada con éxito.",
            )
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            task = ModelTask.objects.get(id=response.data["id"])
            send_task_notification.delay(
                task.email,
                "Tarea actualizada",
                f"La tarea '{task.title}' ha sido actualizada con éxito.",
            )
        return response


@method_decorator(login_required, name="dispatch")
class TaskListView(ListView):
    model = ModelTask
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required, name="dispatch")
class TaskCreateView(CreateView):
    model = ModelTask
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        task = form.instance
        send_task_notification.delay(
            task.email,
            "Tarea creada",
            f"La tarea '{task.title}' ha sido creada con éxito.",
        )
        return response


@method_decorator(login_required, name="dispatch")
class TaskUpdateView(UpdateView):
    model = ModelTask
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        task = form.instance
        send_task_notification.delay(
            task.email,
            "Tarea actualizada",
            f"La tarea '{task.title}' ha sido actualizada con éxito.",
        )
        return response


@method_decorator(login_required, name="dispatch")
class TaskDeleteView(DeleteView):
    model = ModelTask
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")
