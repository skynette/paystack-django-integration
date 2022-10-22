from django.shortcuts import render, redirect
from .models import Payment, UserWallet
from django.conf import settings

def initiate_payment(request):
	if request.method == "POST":
		amount = request.POST['amount']
		email = request.POST['email']

		pk = settings.PAYSTACK_PUBLIC_KEY

		payment = Payment.objects.create(amount=amount, email=email, user=request.user)
		payment.save()

		context = {
			'payment': payment,
			'field_values': request.POST,
			'paystack_pub_key': pk,
			'amount_value': payment.amount_value(),
		}
		return render(request, 'make_payment.html', context)

	return render(request, 'payment.html')


def verify_payment(request, ref):
	payment = Payment.objects.get(ref=ref)
	verified = payment.verify_payment()

	if verified:
		user_wallet = UserWallet.objects.get(user=request.user)
		user_wallet.balance += payment.amount
		user_wallet.save()
		print(request.user.username, " funded wallet successfully")
		return render(request, "success.html")
	return render(request, "success.html")