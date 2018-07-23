from Rocket import Rocket, Material, LaunchError

steelRocket = Rocket(100, Material.steel)
# steelRocket.build()

try:
    steelRocket.launch()
except LaunchError as error:
    print("Error: {}".format(error.args))
finally:
    print("TEST")

print(steelRocket.test)