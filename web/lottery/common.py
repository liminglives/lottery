


def checkCookies(request):
    if "username" not in request.COOKIES:
        print "username is not in cookies"
        return False
    return True

def getCurRoundID():
	return '20150216';

def genOrderID():
	return '4323121'