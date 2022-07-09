
if __name__ == '__main__':
    wgr = float(input("Enter weight in grains:\n"))
    fps = float(input("Enter speed in FPS:\n"))
    #print(wgr, fps)
    # energy in footpounds = weight in grains times the square of the velocity divided by 450800
    footPounds = (wgr * fps * fps)/450800
    slugFPS = (wgr * fps)/225400

    print(f"\nKE : {round(footPounds, 3)}",
          f"\nMomentum (Slug FPS) : {round(slugFPS, 3)}")