from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from normalaccount.forms import CreateUserForm, CustomAuthenticationForm
from normalaccount.models.custom_user import CustomUser
from normalaccount.token import user_tokenizer_generate


def auth_view(request):
    form = CustomAuthenticationForm()
    context = {"login_form": form}

    return render(request, "account/auth.html", context)


def register_view(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            user.is_active = False

            user.save()

            # sent email verification
            current_site = get_current_site(request)
            subject = "Activeaza contul"
            message = render_to_string(
                "account/email_verification.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": user_tokenizer_generate.make_token(user),
                },
            )

            user_email = user.email

            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[
                    user_email,
                ],
                html_message=message,
            )

            # return redirect("email-verification-sent")
            return JsonResponse({"signed_in": True})

    context = {"register_form": form}

    return render(request, "account/partials/register.html", context)


def login_view(request):
    form = CustomAuthenticationForm()

    if request.method == "POST":

        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            login(request, user)
            # return redirect("home")
            return JsonResponse({"logged_in": True})

    context = {"login_form": form}
    # gCTcD*KeJV!u=TO=
    return render(request, "account/partials/login.html", context)


def logout_view(request):
    logout(request)

    return redirect("home")


def profile_view(request, pk):
    user = CustomUser.objects.get(pk=pk)

    context = {"user": user}
    return render(request, "account/profile.html", context)


def delete_account_view(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)

    user.delete()

    # return redirect(reverse("home"))
    return JsonResponse({"success": True})


def email_verification_view(request, uidb64, token):
    unique_token = force_str(urlsafe_base64_decode(uidb64))
    custom_user = CustomUser.objects.get(pk=unique_token)

    if custom_user and user_tokenizer_generate.check_token(custom_user, token):
        custom_user.is_active = True
        custom_user.save()

        return redirect("email-verification-success")
    else:
        return redirect("email-verification-failed")


def email_verification_sent_view(request):
    return render(request, "account/email_verification_sent.html")


def email_verification_success_view(request):
    return render(request, "account/email_verification_success.html")


def email_verification_failed_view(request):
    return render(request, "account/email_verification_failed.html")
