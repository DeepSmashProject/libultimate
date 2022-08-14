from libultimate import Controller, Console

console = Console(address="0.0.0.0:10000")
controller = Controller(console=console, port=1)

console.run()
with console.connect():
    for gamestate in console.stream():
        print("gamestate: ", gamestate.message)
        result = controller.press()
        print("controled: ", result.message)
