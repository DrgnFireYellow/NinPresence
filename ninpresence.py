from pypresence import Presence
import tkinter

games = {
    "Super Mario Oddysey": "supermariooddysey",
    "Animal Crossing: New Horizons": "animalcrossingnewhorizons",
    "Splatoon 3": "splatoon3",
    "Splatoon 2": "splatoon2",
    "Game Builder Garage": "gamebuildergarage",
    "Nintendo Switch Sports": "nintendoswitchsports",
    "Sonic Superstars": "sonicsuperstars",
    "DRAGON QUEST TREASURES": "dragonquesttreasures",
}
window = tkinter.Tk()
window.title("NinPresence")
window.geometry("300x300")
window.configure(background="red")
tkinter.Label(bg="red", fg="white", text="NinPresence", font=("Arial", 32)).pack()
tkinter.Label(bg="red", fg="white", text="Enter your Discord application id").pack()
client_id = tkinter.Entry(show="*", highlightbackground="red")
client_id.pack()


def start_rpc(game):
    RPC = Presence(client_id.get())
    RPC.connect()
    RPC.update(details=f"Playing {game}", large_image=games[game], large_text=game)


selected = tkinter.StringVar(window, "- Select a Game -")
selector = tkinter.OptionMenu(window, selected, *games.keys(), command=start_rpc)
selector.pack()
tkinter.mainloop()
