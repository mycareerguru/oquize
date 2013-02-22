from django.http import HttpResponse

def main_page(request):
    return HttpResponse("Hello word")

def first_temp(request):
	output = '''
		<html>
			<head><title>%s</title></head>
			<body>
	     		<h1>%s</h1><p>%s<p>
	  		</body>
		</html>
	''' %(
		'Online test',
		'Welcome to the Online test first page ',
		'where you can gudge uyrself .'
		)
	return HttpResponse(output)	
