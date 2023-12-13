# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

# Deklarasikan karakter yang digunakan di game.
define ak = Character("Asep Kuda", color="#000000")
define a = Character('Aria', color="#00ff48")
define h = Character('Dr. Hakari', color="#0011f9")
define b = Character('Bryan', color="#ff00fb")

# Game dimulai disini.
label start:
    
    scene bg cosmos with dissolve
    
    show asep kid at topleft with dissolve

    ak "{cps=10}Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{/cps}"

    play music "jungle.opus"

    play sound "baba booey.mp3"   

    ak "baba booey"

    stop sound

    scene black with fade

    "Dalam dunia yang penuh dengan misteri dan keajaiban, terdapat sebuah sekolah khusus yang menyimpan rahasia tak terduga. Sekolah ini tidak biasa, karena di dalamnya terdapat sesuatu yang disebut \"Pintu Gerbang Alam Semesta.\" Pintu ini, suatu keajaiban yang aneh, membawa karakter utama kita, Aria, ke dalam petualangan yang melibatkan pengetahuan, budaya, dan sejarah di seluruh dunia."
    "Aria, seorang siswi yang penuh semangat untuk belajar, menemukan Pintu Gerbang Alam Semesta secara tak sengaja. Tanpa menyadari kekuatan besar di baliknya, dia bersiap-siap untuk memulai perjalanan yang akan mengubah hidupnya."

    scene bg cosmos with dissolve

    "Episode 1: \"Pembukaan Pintu Alam Semesta\""

    "Suatu hari, di sekolah khusus itu, Aria tanpa sengaja menemukan ruang tersembunyi yang tidak terlihat oleh mata manusia biasa. Di ruang itu, terdapat Pintu Gerbang Alam Semesta."

    show mry_goldsect_neutral with fade

    a "Apa ini? Mengapa tidak pernah kudengar sebelumnya?"

    "Tanpa berpikir panjang, Aria memutuskan untuk membuka pintu misterius tersebut. Begitu pintu terbuka, dia merasakan kekuatan ajaib yang menyeretnya masuk ke dalam sebuah portal cahaya yang mempesona."        

    scene black with fade

    scene bg amazon with dissolve
    
    show mry_goldsect_surprised with fade

    "Sesaat kemudian, Aria mendapati dirinya berdiri di tengah-tengah hutan hujan Amazon. Keindahan alam yang luar biasa dan suara alam yang merdu memenuhi telinganya."

    return
