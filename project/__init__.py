from __future__ import absolute_import, unicode_literals

# Evita que las tareas sean importadas de forma temprana para evitar errores de carga.
from .celery import app as celery_app

__all__ = ("celery_app",)