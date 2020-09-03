from django.urls import path
import blog.views

app_name = 'blog'

urlpatterns = [
    path('<int:blog_id>', blog.views.detail, name = "detail"),
    path('new/', blog.views.new, name="new"),
    path('create/', blog.views.create, name="create"),
    path('delete/<int:blog_id>', blog.views.delete, name="delete"),
    path('edit/<int:blog_id>', blog.views.edit, name="edit"),
    path('update/<int:blog_id>', blog.views.update, name="update"),
]
