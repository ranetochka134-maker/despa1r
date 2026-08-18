from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.translation import gettext as _

from .models import Project


def home(request):
    projects = Project.objects.all()

    return render(
        request,
        "portfolio/home.html",
        {"projects": projects}
    )


def project_list(request):
    projects = Project.objects.all()

    return render(
        request,
        "portfolio/projects.html",
        {"projects": projects}
    )


def project_detail(request, project_id):
  project = get_object_or_404(Project, id=project_id)

  # Соседние проекты для навигации
  prev_project = (
      Project.objects.filter(id__lt=project.id).order_by('-id').first()
  )
  next_project = (
      Project.objects.filter(id__gt=project.id).order_by('id').first()
  )

  return render(
      request,
      'portfolio/project_detail.html',
      {
          'project': project,
          'prev_project': prev_project,
          'next_project': next_project,
      },
  )


def about(request):
    return render(
        request,
        "portfolio/about.html"
    )


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"Message from {name} ({email})"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                body,
                email,
                ["admin@atelier.design"],
                fail_silently=False,
            )
            messages.success(request, _("Your message has been sent successfully!"))
        except Exception:
            messages.error(request, _("An error occurred. Please try again later."))

        return redirect("contact")

    return render(
        request,
        "portfolio/contact.html"
    )