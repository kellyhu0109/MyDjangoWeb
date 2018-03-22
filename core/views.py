from django.shortcuts import render


def hi(request, n1, n2):
    s = n1 + n2
    return render(request, 'hi.html', {
        's': s,
    })


def r(request, start, stop):
    if start > stop:
        start, stop = stop, start

    rr = range(start, stop+1)
    if start > stop:
        rr = reversed(rr)

    return render(request, 'r.html', {
        'rr': rr,
    })


def hw1(request, start, stop, odd_or_even):
    need_reverse = start > stop
    start, stop = min(start, stop), max(start, stop)

    if odd_or_even not in [0, 1]:
        return r(request, start, stop)

    if start % 2 == 1 and odd_or_even == 0:
        start += 1
    elif start % 2 == 0 and odd_or_even == 1:
        start += 1

    rr = range(start, stop+1, 2)
    if need_reverse:
        rr = reversed(rr)

    return render(request, 'r.html', {
        'rr': rr
    })
