from playsound import playsound

stations = {
    88.5: "https://knkx-live-a.edge.audiocdn.com/6284_256k",
    92.5: "https://playerservices.streamtheworld.com/api/livestream-redirect/KQMVFM.mp3",
    94.1: "https://live.amperwave.net/direct/audacy-kswdfmaac-imc",
    94.9: "https://playerservices.streamtheworld.com/api/livestream-redirect/KUOWFM_HIGH_MP3.mp3",
    95.7: "https://stream.revma.ihrhls.com/zc2569",
    96.5: "https://stream.revma.ihrhls.com/zc7788",
    98.1: "http://classicalking.streamguys1.com/king-fm-mp3",
    102.5: "https://stream.revma.ihrhls.com/zc7787",
    106.1: "https://stream.revma.ihrhls.com/zc4257",
    106.9: "https://playerservices.streamtheworld.com/api/livestream-redirect/KRWMFM.mp3",
    107.7: "https://live.amperwave.net/direct/audacy-knddfmaac-imc"
}

while True:
    print("Frequency Options:")
    for station in stations:
        print(station)

    choice = float(input("Enter your frequency: "))
    if choice in stations:
        station = stations[choice]
        playsound(station)
        break

    else:
        print("Station non-existant")
