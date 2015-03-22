####################################################################
# NOTE: Change IP Address
####################################################################

from bottle import route, run, template
import requests
IP_ADDRESS = '192.168.0.207'

def get_one_bus_away_info(lat, lon):
	r = requests.get('http://api.pugetsound.onebusaway.org/api/where/routes-for-location.json?key=b1d2f2f3-e73a-4d0e-8db1-b44c5cde5627&lat=' + str(lat) + '&lon=' + str(lon))
	response = r.json()['data']['list']
	alternate_route_count = len(response)
	if (alternate_route_count > 5):
		alternate_route_count = 5

	final_result = '<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.2//EN" "http://www.openmobilealliance.org/tech/DTD/xhtml-mobile12.dtd">'
	final_result = '<html><body><table style="width:200px -webkit-text-size-adjust: 50%"><tr style= "background-color: #FFA48D;"><td><b>Number</b></td><td><b>Description</b></td><td><b>LINK</b></td></tr>'
	for current_route in xrange(0,alternate_route_count):
		final_result +=	'<tr><td>' + str(response[current_route]['shortName']) + '</td><td>' + str(response[current_route]['description'])+ '</td><td><a href=' + str(response[current_route]['url']) + '>Link</a>' + '</td></tr>'
	final_result += '</table></body></html>'

	return final_result


def get_pronto_bike_info(my_lat, my_lon):
	r = requests.get('https://communities.socrata.com/resource/rsib-fvg5.json?$$app_token=frFwYpvNTUXQWxNJWQ49YJu5q')
	final_result = '<html><body><table style="width:200px -webkit-text-size-adjust: 50%"><tr style= "background-color: #FFA48D;"><td><b>Number</b></td><td><b>Description</b></td><td><b>Docks</b></td></tr>'
	
	final_result +=	'<tr><td>' + str('CBD-06') + '</td><td>' + str('2nd Ave & Spring St') + '</td><td><a href=' + str('https://secure.prontocycleshare.com/map/') + '>20</a>' + '</td></tr>'
	final_result +=	'<tr><td>' + str('CBD-05') + '</td><td>' + str('1st Ave & Marion St') + '</td><td><a href=' + str('https://secure.prontocycleshare.com/map/') + '>20</a>' + '</td></tr>'
	final_result +=	'<tr><td>' + str('CBD-07') + '</td><td>' + str('City Hall') + '</td><td><a href=' + str('https://secure.prontocycleshare.com/map/') + '>17</a>' + '</td></tr>'
	final_result +=	'<tr><td>' + str('WF-04') + '</td><td>' + str('Seattle Aquarium') + '</td><td><a href=' + str('https://secure.prontocycleshare.com/map/') + '>18</a>' + '</td></tr>'
	final_result +=	'<tr><td>' + str('FH-01') + '</td><td>' + str('Frye Art Museum') + '</td><td><a href=' + str('https://secure.prontocycleshare.com/map/') + '>16</a>' + '</td></tr>'
	return final_result
	
# Request: http://192.168.72.134:8080/onebusaway/47.6221660/-122.3405270
# Response: ROUTE_TEXT,ID,URL|...
@route('/onebusaway/<lat>/<lon>')
def index(lat,lon):
    #return template('<b>Hello {{name}}</b>!', name=name)
    return get_one_bus_away_info(lat, lon)

# Request: http://192.168.72.134:8080/pronto/47.6221660/-122.3405270
# Response: ROUTE_TEXT,ID,URL|...
@route('/pronto/<my_lat>/<my_lon>')
def index(my_lat,my_lon):
    return get_pronto_bike_info(my_lat, my_lon)
    



run(host=IP_ADDRESS, port=8080)



