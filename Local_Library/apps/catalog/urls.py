from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    # url(r'^book/([0-9]{4})$', views.book_details),
    # url(r'^author/([0-9]{4})$', views.author_details),

    # url(r'^login$', views.login, name='login'),
    # url(r'^logout$', views.logout, {'next_page': '/login/'}, name='logout'),
    # url(r'^register$', views.register, name='register'),
    # url(r'^success$', views.success, name='success'),
]
