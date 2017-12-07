from django.shortcuts import render

def post_list(request):
    """ post_list view """
    return render(request, 'blog/post_list.html')
