from functools import lru_cache
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.loader import render_to_string
from django.views.generic import ListView
from user_profile.models import *
from django.db.models import Q
from django.db import connection
from user_profile.models import *
from datetime import datetime
from django.contrib.auth.models import User
from cinemarepn.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
import reportlab  # import the library
from reportlab.pdfgen import canvas  # import modules
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from datetime import datetime
import qrcode
import qrcode.image.svg
from io import BytesIO


@lru_cache()
def logo_data():
    with open(finders.find('emails/logo.png'), 'rb') as f:
        logo_data = f.read()
    logo = MIMEImage(logo_data)
    logo.add_header('Content-ID', '<logo>')
    return logo


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class MoviesListView(ListView):
    model = Films
    context_object_name = 'films_list'
    paginate_by = 4  # if pagination is desired
    template_name = 'Movies/Movies.html'
    ordering = ['id']

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.method == 'GET':
            search = self.request.GET.get('search')
            orderCinema = self.request.GET.get("orderCinema")
            orderTime = self.request.GET.get("orderTime")
            if search:
                with connection.cursor() as cursor:
                    cursor.execute(
                        f'''Select 
                        home_films.name_film,
                        home_films.id, 
                        home_films.image_film,
                        home_films.short_info_film 
                        from home_session left join home_films ON home_films.id = home_session."ID_Films_id" 
                        where home_films.name_film ILIKE  '{search}%' group by home_films.id''')
                    qs = dictfetchall(cursor)
                    return qs
            if orderCinema:
                if orderCinema == "all":
                    return qs
                else:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f'''Select home_films.name_film,
                            home_films.id,
                            home_films.image_film,
                            home_films.short_info_film 
                            from home_session left join home_films ON home_films.id = home_session."ID_Films_id"
                            left join home_cinemas ON home_cinemas.id = home_session."ID_cinema_id"
                            WHERE home_cinemas.id = {orderCinema} group by home_films.id''')
                        qs = dictfetchall(cursor)
                        return qs
            if orderTime:
                if orderTime == "all":
                    return qs
                elif orderTime == "1":
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f'''SELECT HOME_FILMS.NAME_FILM,
                            HOME_FILMS.ID,
                            HOME_FILMS.IMAGE_FILM,
                            HOME_FILMS.SHORT_INFO_FILM
                            FROM HOME_SESSION
                            LEFT JOIN HOME_FILMS ON HOME_FILMS.ID = HOME_SESSION."ID_Films_id"
                            WHERE HOME_SESSION.DATE_SESSION::TIME >= '7:00'
                            AND HOME_SESSION.DATE_SESSION::TIME <= '12:00'
                            GROUP BY HOME_FILMS.ID''')
                        qs = dictfetchall(cursor)
                        return qs
                elif orderTime == "2":
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f'''SELECT HOME_FILMS.NAME_FILM,
                            HOME_FILMS.ID,
                            HOME_FILMS.IMAGE_FILM,
                            HOME_FILMS.SHORT_INFO_FILM
                            FROM HOME_SESSION
                            LEFT JOIN HOME_FILMS ON HOME_FILMS.ID = HOME_SESSION."ID_Films_id"
                            WHERE HOME_SESSION.DATE_SESSION::TIME >= '12:00'
                            AND HOME_SESSION.DATE_SESSION::TIME <= '17:00'
                            GROUP BY HOME_FILMS.ID''')
                        qs = dictfetchall(cursor)
                        return qs
                elif orderTime == "3":
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f'''SELECT HOME_FILMS.NAME_FILM,
                            HOME_FILMS.ID,
                            HOME_FILMS.IMAGE_FILM,
                            HOME_FILMS.SHORT_INFO_FILM
                            FROM HOME_SESSION
                            LEFT JOIN HOME_FILMS ON HOME_FILMS.ID = HOME_SESSION."ID_Films_id"
                            WHERE HOME_SESSION.DATE_SESSION::TIME >= '17:00'
                            AND HOME_SESSION.DATE_SESSION::TIME <= '22:00'
                            GROUP BY HOME_FILMS.ID''')
                        qs = dictfetchall(cursor)
                        return qs
                elif orderTime == "4":
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f'''SELECT HOME_FILMS.NAME_FILM,
                            HOME_FILMS.ID,
                            HOME_FILMS.IMAGE_FILM,
                            HOME_FILMS.SHORT_INFO_FILM
                            FROM HOME_SESSION
                            LEFT JOIN HOME_FILMS ON HOME_FILMS.ID = HOME_SESSION."ID_Films_id"
                            WHERE HOME_SESSION.DATE_SESSION::TIME >= '22:00'
                            AND HOME_SESSION.DATE_SESSION::TIME <= '7:00'
                            GROUP BY HOME_FILMS.ID''')
                        qs = dictfetchall(cursor)
                        return qs
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        context['orderCinema'] = self.request.GET.get("orderCinema")
        context['Cinemas'] = Cinemas.objects.all()
        context['orderTime'] = self.request.GET.get("orderTime")
        return context


def details_films(request, movies_id):
    context = {}
    genre = None
    try:
        movies = Films.objects.filter(id=movies_id)
        context['movies'] = movies
        context['sessions'] = Session.objects.filter(ID_Films=movies_id)
        context['cinemas'] = Cinemas.objects.all()
        for p in movies:
            genre = p.genre_film
        context['genreFilm'] = Films.objects.filter(Q(genre_film=genre), ~Q(id=movies_id))
    except Films.DoesNotExist:
        raise Http404("movies_id does not exist")
    return render(request, 'Movies/MoviesAbout.html', context=context)


class Ticket():
    tickets = None


def sessionInfo(request, id_sess, movies_id):
    context = {}
    try:
        context['sessions'] = Session.objects.get(id=id_sess)
    except Session.DoesNotExist:
        raise Http404("movies_id does not exist")

    if request.method == 'POST':
        Ticket.tickets = request.POST.get('countTicket')
        return HttpResponseRedirect('ticketbuy')
    return render(request, 'Movies/sessioninfo.html', context=context)


def ticket_buy(request, id_sess, movies_id):
    context = {
        'countTicket': Ticket.tickets,
        'sessions': Session.objects.get(id=id_sess),
    }
    ses = Session.objects.get(id=id_sess)
    if request.method == 'POST':
        with connection.cursor() as cursor:
            print(datetime.now())
            cursor.execute(
                f'''insert into user_profile_sales("dataSales","countTicket",price_session,"User_id_id",sessions_id_id)
                 values(NOW() ,{Ticket.tickets},{Ticket.tickets}::numeric * {ses.price_session}::numeric,{request.user.id},{id_sess});
                 UPDATE  home_session set countplaces_session = countplaces_session - {Ticket.tickets} where home_session.id ={id_sess};''')
        context['message'] = 1
        # pdf
        sale = Sales.objects.order_by('-id')[0]
        ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M')
        p = canvas.Canvas(f"pdf_ticket/{sale.id}.pdf")
        p.setFont("Helvetica", 15)
        p.drawString(50, 800, f"Hello " + request.user.username)
        p.drawString(50, 780, f"Film {ses.ID_Films.name_film}")
        my_image = ImageReader(f'C:/Users/bingo/PycharmProjects/cinemarepn/{ses.ID_Films.image_film.url}')
        p.drawImage(my_image, 50, 550, 170, 200)
        p.drawString(230, 740, f"Date: {ses.date_session.strftime('%Y-%m-%d %H:%M')}")
        p.drawString(230, 720, f"Hall: {ses.hallnumber_session}")
        p.drawString(230, 700, f"Price: {sale.price_session}$")
        p.drawString(230, 680, f"Count Ticket: {Ticket.tickets}")
        p.drawString(230, 660, f"Cinema: {ses.ID_cinema.name_cinemas}")
        p.drawString(230, 640, f"Address: {ses.ID_cinema.address_cinemas[:25]}")
        # qrcode
        my_image1 = ImageReader('C:/Users/bingo/PycharmProjects/cinemarepn/static/image/qr.png')
        p.drawImage(my_image1, 50, 400, 150, 150)
        # Close the PDF object.
        p.showPage()
        p.save()
        # pdf

        # send email
        messages = f"{request.user.username} your ticket to {ses.ID_Films.name_film}. " \
                   f" At the cinema {ses.ID_cinema.name_cinemas}. Located at {ses.ID_cinema.address_cinemas}." \
                   f" Your ticket with a number {sale.id}" \
                   f" Hall number {ses.hallnumber_session}, and session time {ses.date_session.strftime('%b %d %Y %H:%M:%S')}"
        subject = 'Your ticket! CinemaRepnik.'
        msg = EmailMessage(subject, messages, EMAIL_HOST_USER, [request.user.email])
        msg.attach_file('films/static/image/desktop.jpg')
        msg.attach_file('C:/Users/bingo/PycharmProjects/cinemarepn/static/image/qr.png')
        msg.attach_file(f'C:/Users/bingo/PycharmProjects/cinemarepn/pdf_ticket/{sale.id}.pdf')
        msg.send(fail_silently=True)
        # send email
        return render(request, 'Movies/buyticket.html', context=context)

    return render(request, 'Movies/buyticket.html', context=context)
