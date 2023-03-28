from libultimate import UltimateClient, Button
import cv2
if __name__ == "__main__":
    client = UltimateClient("http://localhost:8008")
    client.add_controller(0)
    for gamestate in client.stream(fps=5, include_image=True, image_size=(84, 84)):
        print("gamestate: ", gamestate.players[0].position, gamestate.image.shape)
        cv2.imshow('camera' , gamestate.image)

        key =cv2.waitKey(10)
        if key == 27:
            break
        #client.input(0, [Button.A])
        
    cv2.destroyAllWindows()