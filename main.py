def on_travelled_sprint():
    blocks.place(DIAMOND_BLOCK, pos(0, 0, 0))
    mobs.spawn(CHICKEN, pos(0, 0, 0))
player.on_travelled(SPRINT, on_travelled_sprint)
