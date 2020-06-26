# -*- coding: utf-8 -*-
from .models import Person
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from faker import Faker


def generate_pdf(request):
    """Generate pdf."""
    # Model data
    people = Person.objects.filter(pk__lte=200).order_by('name')

    # Rendered
    html_string = render_to_string('person/index.html', {'people': people})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response


def create_users(request):
    fake = Faker()

    for i in range(1000):
        Person.objects.create(name=fake.email().split(
            '@')[0], email=fake.email(), surname=fake.email().split('@')[0])
