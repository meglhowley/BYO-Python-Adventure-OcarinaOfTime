# Create your own adventure with python here

def game_over():
    print('Play again? Y/N')
    play_again = str(input('..'))
    if play_again == 'y' or play_again == 'Y':
        ocarina_of_time()
    else:
        return


player_name = None


def ocarina_of_time():
    print(r"""\
                     __        __   /\/
                    /==\      /  \_/\/
                  /======\    \/\__ \__
                /==/\  /\==\    /\_|__ \
             /==/    ||    \=\ / / / /_/
           /=/    /\ || /\   \=\/ /
        /===/   /   \||/   \   \===\
      /===/   /_________________ \===\
   /====/   / |                /  \====\
 /====/   /   |  _________    /  \   \===\    THE LEGEND OF
 /==/   /     | /   /  \ / / /  __________\_____      ______       ___
|===| /       |/   /____/ / /   \   _____ |\   /      \   _ \      \  \
 \==\             /\   / / /     | |  /= \| | |        | | \ \     / _ \
 \===\__    \    /  \ / / /   /  | | /===/  | |        | |  \ \   / / \ \
   \==\ \    \\ /____/   /_\ //  | |_____/| | |        | |   | | / /___\ \
   \===\ \   \\\\\\\/   /////// /|  _____ | | |        | |   | | |  ___  |
     \==\/     \\\\/ / //////   \| |/==/ \| | |        | |   | | | /   \ |
     \==\     _ \\/ / /////    _ | |==/     | |        | |  / /  | |   | |
       \==\  / \ / / ///      /|\| |_____/| | |_____/| | |_/ /   | |   | |
       \==\ /   / / /________/ |/_________|/_________|/_____/   /___\ /___\
         \==\  /               | /==/
         \=\  /________________|/=/    OCARINA OF TIME
           \==\     _____     /==/
          / \===\   \   /   /===/
         / / /\===\  \_/  /===/
        / / /   \====\ /====/
       / / /      \===|===/
       |/_/         \===/
                      =

                                      .......A quest through time, and your terminal.
                      """)

    print("HEY, LISTEN!")
    print("I am Navi. I was sent by the great Deku tree to find the boy without a fairy...and I'm told that's you. What's your name?")
    player_name = str(input('..'))
    print("Alright, we'll call you " + player_name +
          " then. We don't have much time. Great Deku has fallen ill and he has a very important message to communicate to the boy without a fairy. Well... I guess you can call me your fairy now. Let's go " + player_name + "! Are you ready? (Y/N)")
    ready = str(input('..'))
    print(ready)
    if ready == 'N' or ready == 'n':
        print("Well that's too bad. Deku needs us NOW! Let's go!")
    elif ready == 'Y' or ready == 'y':
        print("Excellent! Off we go then.")
    print(r"""\
  .....
  .....
  .....

  """)
    print("Okay, we made it. How are you feeling?")
    emotion = str(input('..'))
    print("Hm, " + emotion + "? That's to be expected. Look who it is!")
    print(r"""\
         &&& &&  & &&
      && &\/&\|& ()|/ @, &&
      &\/(/&/&||/& /_/)_&/_&
   &() &\/&|()|/&\/ '%" & ()
  &_\_&&_\ |& |&&/&__%_/_& &&
&&   && & &| &| /& & % ()& /&&
 ()&_---()&\&\|&&-&&--%---()~
     &&     \|||
             |||
             |||                ~~THE GREAT DEKU TREE~~
             |||
       , -=-~  .-^- _
                __________ /  \____________
               /  ... you made it, just in  \
              |   time. please... sit down.  |
              |   There is much to discuss   |
               \___________________________ /
  """)
    print(player_name + ".........")
    print("It's been so long....")
    input("Make a selection: A) Good to see you. B) And you are...? (A/B)..")
    print("It is a pleasure to see you again " + player_name + ". I am the Great Deku tree, I am the guardian of this forest. I oversee not only the Kokiri forest, but the population of beings that live in my shadow. Hyrule needs your help. I have been cursed by the wicked man of the desert. This man seeks to conquer all of Hyrule. You must stop him. The only way you can do this is with the help of the princess. Go now to the Hyrule Castle Garden. You will find her there.")
    print("...And " + player_name + ", take this.")
    input('Press enter to extend hands. ..')
    print(r"""\

        .     '     ,A
    _________
 _ /_|_____|_\ _
   '. \   / .'
     '.\ /.'
       '.'      *hands over Spiritual Stone*

    """)
    print("This is the spiritual stone of the Forest. It will assist in your quest. Goodbye Navi....and good luck " + player_name + ".")
    print(r"""\
  .....
  .....
  .....
              *Beedle appears*
  """)
    beedle_choice = str(
        input('Make a selection: A) Talk to Beedle B) Go into Hyrule (A/B)..'))
    if beedle_choice == 'A' or beedle_choice == 'a':
        print("Oh no! Beedle talked for way too long and you don't have any rupees to purchase anything of value in the quest. Ganon reached Zelda before you made it into Hyrule. GAME. OVER.")
        game_over()
    else:
        print(r"""\

 [][][] /""\ [][][]
  |::| /____\ |::|
  |[]|_|::::|_|[]|
  |::::::__::::::|      *Hyrule Castle*
  |:::::/||\:::::|
  |:#:::||||::#::|
 #%*###&*##&*&#*&##
##%%*####*%%%###*%*#

         """)
        input('Press enter to go in ..')
        print('Zelda: ' + player_name + "! You're here! I need your help and quickly. Ganon is trying to reach the Triforce, a holy relic that gives its holder godlike power. The Triforce is being kept in the Sacred Realm. I need you to obtain the 3 sacred stones in order for us to enter the Sacred Realm and procure the Triforce. It looks like you already have one stone. GO! NOW!")

        input('Press enter to leave Hyrule ..')
        print('WAIT! LINK! One more thing. Take this!!')
        input('Press enter to extend hands ..')
        print(r"""\

                                   ((  ^_.     (()))
                                    ' / /_\    {' ())
                                      L( '}     )_ (()
                                       ) (_    (   (_)
                                     (_  / }{)===='_/
              *hands over            | `/\/\     |   \
               ocarina*              L___/ |     |    |
                                      |  . \     |    |
                                      |_/ \_\    |    |
                                      ( ____ )   |    |
                                       | | | |   |    |
                                   ( --' | \ |_  '~~~~'
                                   /_/---) (___)  _/Y
          """)
        print("This is the ocarina of time. I'm sure you will find a use for it along your journey. Goodbye, " + player_name)
        input('Press enter to leave Hyrule ..')
        print("Navi: Okay, so the 2 remaining stones are located in the Water Temple and the Fire temple. Which do you want to tackle first?")
        temple_choice = str(input(
            'Make a selection: A) The Water Temple B) The Fire Temple (A/B) ..'))
        if temple_choice == 'A' or temple_choice == 'a':
            print(r"""\

             _.`.         .'.                            .'         `.
            |`-._`-.._..-'_.-|                          /             \
            |  _ `-._ _.-'   |                         |               |
            | | `-._ " _.-'| |                         |               |
            | |    || |    | |                         |               |
            | |    || |    | |                          \             /
            | |    || |    | |                          _`.         .'.
            | |    || |    | |                         |`-.`-.._..-'.-'|
            | |    || |    | |                         |    `-._.-'    |
            | | _.-'| |_   | |                         | |`-._   _.-'| |
            | |'_.-'| |_`-.| |                         | |   || |    | |
           |_.-'    | | `-._ `._|`-._                  | |   || |    | |
          /    /    | |     ``---._  `-._              | |   || |    | |
         | / /    .-' `-._|`-._    ``-._ `-._          | |   || |    | |
        || ||  / /|-| |-._     `-._     `--._`-._|`-._ | |   || |    | |
           | |   ' || |\  `-._     `-._      ``---._  `| |   || |    | |
        | - | | |  || | \  | |`-._     `-._|`-._    ``-| |`-.|| |    | |
    _.-'    |   |  || |  \ | |    `-._          `-._   | |-._ | |._  | |
_.-'     |     |   || |   \| |        `-._          `-.| |   `| |_ `-| |
        |    |  |  || |    | |            `-._       _.| |    | | `.-| |
        |   |  ||  || |    | |              _.-'|_.-'_.-'     | |_.-'  |
         | | |  .  || |    | |          _.-' __.---''       _.| '      |
        |   |  ||  || |    | |\_.-'|_.-'_.-''      _.-'|_.-'        _. |
         | |  |    || |    | |'      _-        _.-'             _.-' | |
        ||    ||   || |_.-'| |_.---''      _.-'             _  |     | |
\          | |  |  || |_.-'| |    _.-'|_.-'             _.-'|| |     | |
 \      |  ||    .'_| |    | |_.-'                  _.-'| | || |     | |
  \     | |     |._ | |    | `-._               _.-'    | | || |     | |
   \    ||  |  |   `| |    ```-._`-._|`-._  _.-'        | | || |     | |
   |\_.-|       |      `-._      ``---._  `-._          | | || |     | |
   |     |                 `-._|`-._    ``-._ `-._      | | || |     | |
   |    || ||  |                    `-._     `--._`-._|`| | || |     | |
   |       | |  |                       `-._      ``---.| |`|| |     | |
   |    |   | | |`-._                       `-._|`-._   | |-.| |-._  | |
   |        |      ||`-._                            `-.| |  | |._ `-| |
   |    |    |  |  || |  `-._                         _.| |  | |  `-_| |
   |    |   |  ||__ | |    | `-._            _.-'|_.-'_.-'   | |_.-'   |
   |     | | |  ._.-| |.   | |   `-._    _.-' __.---''      _|         |
   |    |   |  ||/  | | \  | |  _.-'|_.-'_.-''     _.-'|_.-'           |
   |    ||    ||    | |  .'| |-' __.---''      _.-'                    |
   |       | |  |   |.|   '| |-''     _.-'|_.-'                        |
   |    |  ||  _.   | |  | | |    _.-'                                 |
   |    | |  '  |   | |    | |_.-'                                     |
   |    ||  |  | \  | | / _| '                                      _.-'
   |_.-'     |   _`.| |'-'                                      _.-'
   |`-._          _.|                                       _.-'
   |    `-._  _.-'                                      _.-'
   |        |'                                      _.-'
   |        |                                   _.-'
   |        |                               _.-'
   |        |                           _.-'
   |        |                       _.-'
   |        |                   _.-'
   |        |               _.-'          ~~THE WATER TEMPLE~~
_  |        |           _.-'
 `-|_       |       _.-'
     `-._   |   _.-'
         `-.|.-'
              """)
            input('Press enter to enter ..')
            print('Oh no! You made it halfway through the temple, but this temple is way to daunting for beginners. Everyone knows it is the hardest temple and thereforce needs to be saved for LAST once your strength and prowess is built up.')
            print('GAME. OVER.')
            game_over()
        else:
            print('On to the fire temple then!')
            print(r"""/
                         ooO
                     ooOOOo
                   oOOOOOOoooo
                 ooOOOooo  oooo
                /vvv\
               /V V V\
              /V  V  V\          THE FIRE TEMPLE
             /         \
            /           \               /
          /               \   	  o          o
__       /                 \     /-   o     /-   (GORONS)
/\     /                     \  /\  -/-    /\
                                    /\


            """)
            input("Press enter to enter temple..")
            print("Yay! the friendly Gorons helped you defeat the final boss in the fire temple no sweat. You have now obtained 2/3 sacred stones.")
            print("Do you wish to A) proceed to the Water Temple, or B) obtain a horse to facilitate traveling? (A/B)")
            water_horse = str(input('..'))
            if water_horse == 'B' or water_horse == 'b':
                print(r"""/

                                                              _/
                  ~LON LON RANCH~                       _/\  /
                                        _=~=_        ../   \/
                                        |   |~=_   ./ :     \
              W|  ,              __|__  |   |  |  /  `|'
            -::-/)              L___J  |===|  |     \|/:
              /\                |     |_|___|==|     \|/:'
            " |"               |     |     \  |     \|X|/
        '''''''''"""'''''''''"""""""""``````````````````````````````
        '''''''""""""`````````"""""""""""""`````````````````````
        ''''''"""""""```````````""""""""""""`````````````````````````
        ''''''""""""""```````````"""""""""````````````````````````````````



              ''')
                input('Press enter to enter the ranch ..')
                print("Talon: Hi there, I'm Talon, welcome to Lon Lon Ranch. If you want to obtain a horse, please use that ocarina of yours to play the following song. We call it, Epona's song")
                input('Press enter to take out ocarina ..')
                input(
                    "Yeah, that's the one. Now listen carefully, here is how Epona's song goes:")
                print(r"""/
                                                           |\
---|\------------------------------------------------------|-\\------
---|/--------  ^  -------------  ^  ----------------------0---\|-----
--/|-------------  <  --------------  <  ----------------------|-----
-|-/-\----------------  >  ---------------  >  ---------------0------
--\|/----------------------------------------------------------------

                """)
                print(
                    "You got that? Here it is one more time. Remember to include a space between each note.")
                input("Press enter to view Epona's song again.")
                print(r"""/
                                                           |\
---|\------------------------------------------------------|-\\------
---|/--------  ^  -------------  ^  ----------------------0---\|-----
--/|-------------  <  --------------  <  ----------------------|-----
-|-/-\----------------  >  ---------------  >  ---------------0------
--\|/----------------------------------------------------------------

                """)
                print("Okay....now, play!")
                song = str(input('..'))
                if song == '^ < > ^ < >':
                    print("YES BOY! THAT'S IT! Look, here Epona comes!")
                    input('Press enter to look up ..')
                    print(r"""/

                                                  `T",.`-,
                                                     '8, :.
                                              `""`oooob."T,.
                                            ,-`".)O;8:doob.'-.
                                     ,..`'.'' -dP()d8O8Yo8:,..`,
                                   -o8b-     ,..)doOO8:':o; `Y8.`,
         ~EPONA~                  ,..bo.,.....)OOO888o' :oO.  ".  `-.
                                , "`"d....88OOOOO8O88o  :O8o;.    ;;,b
                               ,dOOOOO"'"'"'"'O88888o:  :O88Oo.;:o888d
                               ""888Ob...,-- :o88O88o:. :o'"""""""Y8OP
                               d8888.....,.. :o8OO888:: ::
                              "" .dOO8bo`'',,;O88O:O8o: ::,
                                 ,dd8".  ,-)do8O8o:"'"; :::
                                 ,db(.  T)8P:8o:::::    :::
                                 -"",`(;O"KdOo::        :::
                                   ,K,'".doo:::'        :o:
                                    .doo:::"'"::  :.    'o:
        ,..            .;ooooooo..o:"'"'     ::;. ::;.  'o.
   ,, "'    ` ..   .d;o:"'"'                  ::o:;::o::  :;
   d,         , ..ooo::;                      ::oo:;::o"'.:o
  ,d'.       :OOOOO8Oo::" '.. .               ::o8Ooo:;  ;o:
  'P"   ;  ;.OPd8888O8::;. 'oOoo:.;..         ;:O88Ooo:' O"'
  ,8:   o::oO` 88888OOo:::  o8O8Oo:::;;     ,;:oO88OOo;  '
 ,YP  ,::;:O:  888888o::::  :8888Ooo::::::::::oo888888o;. ,
 ',d: :;;O;:   :888888::o;  :8888888Ooooooooooo88888888Oo; ,
 dPY:  :o8O     YO8888O:O:;  O8888888888OOOO888"" Y8o:O88o; ,
,' O:  'ob`      "8888888Oo;;o8888888888888'"'     `8OO:.`OOb .
'  Y:  ,:o:       `8O88888OOoo"'"'"'"'"'"           `OOob`Y8b`
   ::  ';o:        `8O88o:oOoP                        `8Oo `YO.
   `:   Oo:         `888O::oP                          88O  :OY
    :o; 8oP         :888o::P                           do:  8O:
   ,ooO:8O'       ,d8888o:O'                          dOo   ;:.
   ;O8odo'        88888O:o'                          do::  oo.:
  d"`)8O'         "YO88Oo'                          "8O:   o8b'
 ''-'`"            d:O8oK  -hrr-                   dOOo'  :o":
                   O:8o:b.                        :88o:   `8:,
                   `8O:;7b,.                       `"8'     Y:
                    `YO;`8b'
                     `Oo; 8:.
                      `OP"8.`
                       :  Y8P
                       `o  `,
                        Y8bod.

                    """)
                else:
                    print(
                        'Hm, not quite. Remember to include a space between each note.')
                    song = str(input('..'))
                if song == '^ < > ^ < >':
                    print("YES BOY! THAT'S IT! Look, here Epona comes!")
                    input('Press enter to look up ..')
                    print(r"""/
                
                                                  `T",.`-,
                                                     '8, :.
                                              `""`oooob."T,.
                                            ,-`".)O;8:doob.'-.
                                     ,..`'.'' -dP()d8O8Yo8:,..`,
                                   -o8b-     ,..)doOO8:':o; `Y8.`,
         ~EPONA~                  ,..bo.,.....)OOO888o' :oO.  ".  `-.
                                , "`"d....88OOOOO8O88o  :O8o;.    ;;,b
                               ,dOOOOO"'"'"'"'O88888o:  :O88Oo.;:o888d
                               ""888Ob...,-- :o88O88o:. :o'"""""""Y8OP
                               d8888.....,.. :o8OO888:: ::
                              "" .dOO8bo`'',,;O88O:O8o: ::,
                                 ,dd8".  ,-)do8O8o:"'"; :::
                                 ,db(.  T)8P:8o:::::    :::
                                 -"",`(;O"KdOo::        :::
                                   ,K,'".doo:::'        :o:
                                    .doo:::"'"::  :.    'o:
        ,..            .;ooooooo..o:"'"'     ::;. ::;.  'o.
   ,, "'    ` ..   .d;o:"'"'                  ::o:;::o::  :;
   d,         , ..ooo::;                      ::oo:;::o"'.:o
  ,d'.       :OOOOO8Oo::" '.. .               ::o8Ooo:;  ;o:
  'P"   ;  ;.OPd8888O8::;. 'oOoo:.;..         ;:O88Ooo:' O"'
  ,8:   o::oO` 88888OOo:::  o8O8Oo:::;;     ,;:oO88OOo;  '
 ,YP  ,::;:O:  888888o::::  :8888Ooo::::::::::oo888888o;. ,
 ',d: :;;O;:   :888888::o;  :8888888Ooooooooooo88888888Oo; ,
 dPY:  :o8O     YO8888O:O:;  O8888888888OOOO888"" Y8o:O88o; ,
,' O:  'ob`      "8888888Oo;;o8888888888888'"'     `8OO:.`OOb .
'  Y:  ,:o:       `8O88888OOoo"'"'"'"'"'"           `OOob`Y8b`
   ::  ';o:        `8O88o:oOoP                        `8Oo `YO.
   `:   Oo:         `888O::oP                          88O  :OY
    :o; 8oP         :888o::P                           do:  8O:
   ,ooO:8O'       ,d8888o:O'                          dOo   ;:.
   ;O8odo'        88888O:o'                          do::  oo.:
  d"`)8O'         "YO88Oo'                          "8O:   o8b'
 ''-'`"            d:O8oK  -hrr-                   dOOo'  :o":
                   O:8o:b.                        :88o:   `8:,
                   `8O:;7b,.                       `"8'     Y:
                    `YO;`8b'
                     `Oo; 8:.
                      `OP"8.`
                       :  Y8P
                       `o  `,
                        Y8bod.
                   
                    """)
                    print(
                        "Epona has given you extra powers! You can go straight to Hyrule to obtain the master sword.")
                    input("Press enter to go back to Hyrule ..")
                    print(r"""\

 [][][] /""\ [][][]
  |::| /____\ |::|
  |[]|_|::::|_|[]|
  |::::::__::::::|      *Hyrule Castle*
  |:::::/||\:::::|
  |:#:::||||::#::|
 #%*###&*##&*&#*&##
##%%*####*%%%###*%*#

                    """)
                    input("Press enter to enter Hyrule ..")
                else:
                    print(
                        "Sorry, that's not it either. You have wasted too much time here and Ganon has obtained the triforce.")
                    print("GAME. OVER.")
                    game_over()


ocarina_of_time()
