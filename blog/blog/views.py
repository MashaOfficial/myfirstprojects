from django.shortcuts import render

# Create your views here.

from .models import Post, Comment
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from .forms import PostForm, CommentForm

from django.contrib.auth.decorators import login_required

# @login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')  # список записей блога, отсортированных по published_date
    return render(request, 'blog/post_list.html', {'posts': posts})

# @login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# def post_new(request):
#     form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_new(request):
        if request.method == "POST":
        # if request.user == User.is_superuser:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                # post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                # post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


# @login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)



@login_required
def comment_drafts(request):
    comments = Comment.objects.filter(approved_comment__isnull=True).order_by('-post_id')
    return redirect(request, 'blog/comment_drafts.html', {'comments': comments})



# '''
# from django.views.generic.edit import FormView
# from django.contrib.auth.forms import UserCreationForm

# class RegisterFormView(FormView):
#     form_class = UserCreationForm

#     # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
#     # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
#     success_url = "/accounts/login/"

#     # Шаблон, который будет использоваться при отображении представления.
#     template_name = "registration/register.html"

#     def form_valid(self, form):
#         # Создаём пользователя, если данные в форму были введены корректно.
#         form.save()

#         # Вызываем метод базового класса
#         return super(RegisterFormView, self).form_valid(form)


# from django.contrib.auth.forms import AuthenticationForm

# # Функция для установки сессионного ключа.
# # По нему django будет определять, выполнил ли вход пользователь.
# from django.contrib.auth import login

# class LoginFormView(FormView):
#     form_class = AuthenticationForm

#     # Аналогично регистрации, только используем шаблон аутентификации.
#     template_name = "login.html"

#     # В случае успеха перенаправим на главную.
#     success_url = "/"

#     def form_valid(self, form):
#         # Получаем объект пользователя на основе введённых в форму данных.
#         self.user = form.get_user()

#         # Выполняем аутентификацию пользователя.
#         login(self.request, self.user)
#         return super(LoginFormView, self).form_valid(form)
#        