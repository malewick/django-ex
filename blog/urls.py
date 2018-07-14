from  django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-datefrom")[:],
                                    template_name="blog/blog.html")),

                url(r'^(?P<tag>\D+)/?$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-datefrom")[:],
                                    template_name="blog/tag.html",
				    ),
				    ),

                url(r'^(?P<pk>\d+)$', DetailView.as_view(
                                    model = Post,
                                    template_name="blog/post.html")),
            ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
