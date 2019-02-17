from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from estatisticas import ler_dados, estatisticas_semana, estatisticas_dia

app = Flask(__name__)
Bootstrap(app)


#Create a dictionary called pins to store the pin number (arduino?), name, and pin state:
pins = {
   1 : {'name' : 'bedroom lamp', 'state' : 0},
   2 : {'name' : 'living room lamp', 'state' : 0}
   }

#dados dos planos da EDP
E = [[1.15, 2.3, 3.45, 4.6, 5.75, 6.9, 10.35, 13.8, 17.25, 13.8, 17.25, 20.7], #Potencia
        [42.88, 61.14, 79.64, 100.81, 120.34, 138.48, 194.22, 252.76, 311.05, 370.69], #PrecoA
		[0.1595, 0.1598, 0.1569, 0.1605, 0.1617, 0.1619, 0.162, 0.1633, 0.1642, 0.165], #EnergiaPkW
		[0, 0, 83.26, 102.42, 121.22, 139.98, 194.8, 251.92, 309.74, 370], #PotenciaBi
		[0, 0, 0.2027, 0.2028, 0.2029, 0.2028, 0.2028, 0.203, 0.2034, 0.2033], #EnergiaF
		[0, 0, 0.0968, 0.0969, 0.0969, 0.0969, 0.0969, 0.0971, 0.0975, 0.0974], #EnergiaV
		[0, 0, 0.2297, 0.2816, 0.3336, 0.3857, 0.5357, 0.6928, 0.8584, 1.0242], #PotenciaTri
		[0, 0, 0.2297, 0.2297, 0.2942, 0.2942, 0.2942, 0.2942, 0.2941, 0.2941], #EnergiaPonta
		[0, 0, 0.1715, 0.1715, 0.1715, 0.1715, 0.1715, 0.1715, 0.1714, 0.1714], #EnergiaCheia
		[0, 0, 0.0942, 0.0942, 0.0942, 0.0942, 0.0942, 0.0942, 0.0941, 0.0941]  #EnergiaV
	]

EF = [[3.45, 4.6, 5.75, 6.9, 10.35, 13.8, 17.25, 13.8, 17.25, 20.7], #Potencia
         [78.03, 98.81, 117.93, 135.71, 190.35, 247.73, 304.85, 363.28], #PotenciaPreco
		 [0.1538, 0.1573, 0.1585, 0.1587, 0.1588, 0.16, 0.1609, 0.1616], #EnergiaPkW
		 [82.42, 101.40, 120.01, 138.59, 192.87, 249.40, 306.64, 366.31], #PotenciaBi
		 [0.2007, 0.2008, 0.2009, 0.2008, 0.2008, 0.201, 0.2014, 0.2013], #EnergiaF
		 [0.958, 0.959, 0.959, 0.959, 0.959, 0.0961, 0.0965, 0.0964] #EnergiaV
	]

tarifario = {
   1 : {'name' : 'Eletricidade'},
   2 : {'name' : 'Eletricidade + Funcionalidade'},
   }


#Create home page
@app.route('/')
def home():
   return render_template('home.html')

#Create lights page, with links to turn on/off each of the lamps. the links redirect to '/pin/on' or '/pin/off'
@app.route('/lights')
def lights():
    #For each pin, read the pin state and store it in the pins dictionary:
    for pin in pins:
       #codigo para perguntar (ao arduino?) o estado do pin.
       #se estivessem ligados ao pi seria  pins[pin]['state'] = GPIO.input(pin)

    #Cria um dictionary para mandar o estado dos pinos para a pagina "lights".
        templateData = {
           'pins' : pins
           }
    #Pass the template data into the template lights.html and return it to the user
    return render_template('lights.html', **templateData)

#Create statistics page
@app.route('/statistics')
def statistics():
    dados = ler_dados()
    estatisticas_semana(dados)
    estatisticas_dia(dados)
    return render_template('statistics.html')

#create suggestions page
@app.route('/suggestions')
def suggestions():
    for ntarifario in tarifario:
        templateData2 = {
            'tarifario' : tarifario
            }
    return render_template('suggestions.html', **templateData2)


#Code of pages the links in "lights" redirect to
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      #GPIO.output(changePin, GPIO.HIGH)
      #change pin state in pins dictionary
      pins[changePin]['state'] = 1
      # Save the state message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      #GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."
      #change pin state in pins dictionary
      pins[changePin]['state'] = 0
   if action == "toggle":
      # Read the pin and set it to whatever it isn't (that is, toggle it):
      #GPIO.output(changePin, not GPIO.input(changePin))
      message = "Toggled " + deviceName + "."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      #pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
       templateData = {
          'message' : message,
          'pins' : pins
       }

   return render_template('lights.html', **templateData)


<<<<<<< HEAD
if (__name__) == ('__main__'):
=======
if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True, host='0.0.0.0', port=5000)
=======
>>>>>>> 7794e5293bac96ceb36872cd4ecd99275bbe7e6f
    app.run(host='0.0.0.0', port=80, debug=True)
>>>>>>> 75794fc9f009b4338cdf2ab3b44385ccd3dc42b9
