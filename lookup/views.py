from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=D0AB4C8B-3336-43A4-AC10-A69EF01083CE")
		#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=98105&distance=25&API_KEY=D0AB4C8B-3336-43A4-AC10-A69EF01083CE
		
		try:
			api = json.loads(api_request.content)
			if api[0]['Category']['Name'] == "Good":
				catogory_color = "good"
				category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
			elif api[0]['Category']['Name'] == "Moderate":
				catogory_color = "moderate"
				category_description =  "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."  			
			elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
				catogory_color = "usg"
				category_description = "(101 - 150) Members of sensitive groups may experience health effects. The general public is not likely to be affected."  			
			elif api[0]['Category']['Name'] == "Unhealthy":
				catogory_color = "unhealthy"
				category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			elif api[0]['Category']['Name'] == "Very Unhelthy":
				catogory_color = "veryunhealthy"
				category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
			elif api[0]['Category']['Name'] == "Hazardous":
				catogory_color = "hazardous"
				category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
				


			return render(request, 'home.html', {
				'api': api, 
				'category_description': category_description,
				'catogory_color' : catogory_color
				})
		except Exeption as e:
			api = "Error..."

		
	


	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=98105&distance=25&API_KEY=D0AB4C8B-3336-43A4-AC10-A69EF01083CE")
		#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=98105&distance=25&API_KEY=D0AB4C8B-3336-43A4-AC10-A69EF01083CE
		
		try:
			api = json.loads(api_request.content)
		except Exeption as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
				catogory_color = "good"
				category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
		elif api[0]['Category']['Name'] == "Moderate":
				catogory_color = "moderate"
				category_description =  "(51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."  			
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
				catogory_color = "usg"
				category_description = "(101 - 150) Members of sensitive groups may experience health effects. The general public is not likely to be affected."  			
		elif api[0]['Category']['Name'] == "Unhealthy":
				catogory_color = "unhealthy"
				category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
		elif api[0]['Category']['Name'] == "Very Unhelthy":
				catogory_color = "veryunhealthy"
				category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
		elif api[0]['Category']['Name'] == "Hazardous":
				catogory_color = "hazardous"
				category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."
				


		return render(request, 'home.html', {
			'api': api, 
			'category_description': category_description,
			'catogory_color' : catogory_color
			})


def about(request):
	return render(request, 'about.html', {})