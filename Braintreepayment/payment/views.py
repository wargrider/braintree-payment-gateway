import braintree
from django.shortcuts import render, redirect
from Braintreepayment.settings import BRAINTREE_PUBLIC_KEY


def payment_process(request):
    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # retrieve amount
        amount = request.POST.get('amount')
        # create and submit transaction
        result = braintree.Transaction.sale({
            "amount": amount,
            "payment_method_nonce": nonce,
            "options": {
                "submit_for_settlement": True
            }
        })
        if result.is_success:
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token
        client_token = braintree.ClientToken.generate()
        return render(request, 'payment/process.html', {'client_token': client_token})


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')

