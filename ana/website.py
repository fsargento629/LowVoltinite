from flask import Flask, render_template

app = Flask(__name__)


#Create a dictionary called pins to store the pin number (arduino?), name, and pin state:
pins = {
   1 : {'name' : 'bedroom lamp', 'state' : 0},
   2 : {'name' : 'living room lamp', 'state' : 0}
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
       #código para perguntar (ao arduino?) o estado do pin.
       #se estivessem ligados ao pi seria  pins[pin]['state'] = GPIO.input(pin)

    #Cria um dictionary para mandar o estado dos pinos para a página "lights".
        templateData = {
           'pins' : pins
           }
    #Pass the template data into the template lights.html and return it to the user
    return render_template('lights.html', **templateData)

#Create statistics page
@app.route('/statistics')
def statistics():
    return render_template('statistics.html')


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
