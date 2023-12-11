# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

# Deklarasikan karakter yang digunakan di game.
define e = Character('Eileen', color="#c8ffc8")
define ak = Character("Asep Kuda", color="#fff000")

# Game dimulai disini.
label start:
    
    scene bg cosmos with dissolve
    
    show asep kid at topleft with dissolve

    ak "{cps=10}Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/cps}"

    play sound "baba booey.mp3" loop   

    ak "baba booey"

    return
