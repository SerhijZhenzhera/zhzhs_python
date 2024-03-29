from .models import BlogModel, CommentModel
from .forms import SearchForm, CommentForm
from django.shortcuts import render, redirect


def BlogListView(request):
    dataset = BlogModel.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = BlogModel.objects.get(blog_title=title)
            # return redirect(f'/blog/{blog.id}')
            return '/blog/', redirect(blog.id)
    else:
        form = SearchForm()
        context = {
            'dataset': dataset,
            'form': form,
        }
    return render(request, 'blogapp/listview.html', context)


def BlogDetailView(request, _id):
    try:
        data = BlogModel.objects.get(id=_id)
        comments = CommentModel.objects.filter(blog=data)
    except BlogModel.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(nic_name=form.cleaned_data['nic_name'],
                                   comment_text=form.cleaned_data['comment_text'],
                                   blog=data)
            Comment.save()
            # return redirect(f'/blog/{_id}')
            return '/blog/', redirect(_id)
    else:
        form = CommentForm()

    context = {
        'data': data,
        'form': form,
        'comments': comments,
    }
    return render(request, 'blogapp/detailview.html', context)
