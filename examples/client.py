from libultimate import UltimateClient, Button
import json
import cv2
if __name__ == "__main__":
    client = UltimateClient("http://localhost:8008")
    client.add_controller(0)
    for gamestate in client.stream(fps=5, include_image=True, image_size=(84, 84)):
        print("gamestate: ", gamestate.players[0].position, gamestate.image.shape)
        cv2.imshow('camera' , gamestate.image)

        #繰り返し分から抜けるためのif文
        key =cv2.waitKey(10)
        if key == 27:
            break
        #client.input(0, [Button.A])
        
#メモリを解放して終了するためのコマンド
cv2.destroyAllWindows()