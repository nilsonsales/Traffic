# Traffic
This project simulates an urban traffic with some rules to be followed.


### Description

Cars are initially generated in random positions on the map. Each car is represented by a letter.

Cars will move following the road direction, shown in the _map.png_ file.

There are traffic light in the crossroads to avoid collisions.
Cars must stop if there's a red light or a car stopped in front of it.

Each time a car stops, a log is added to the occurrences .txt file.

Implementation details can be found inside the code.


### Running

Just run the _Main.py_ file:

```$ python3 Main.py```


### Output

The output will be the detailed change for each car and the updated map, like the example below (for aesthetic reasons I deleted some occurrences).

<!-- language: lang-none -->

      Updating map...
      #A
      Direction: d
      [current car position] =  [4, 0]
      [new car position] =  [5, 0]
      #J
      Direction: r
      Traffic light in front...
      Red light for car #J in the position [18,12]
      #K
      Direction: r
      Traffic jam: Car #K stuck in the position [18,11]
      #R
      Car in crossroad! Already knows where to go
      Direction: l
      [current car position] =  [12, 12]
      [new car position] =  [12, 11]
      #T
      Direction: d
      Traffic light in front...
      Choosing where to go when the light is green... l
      [current car position] =  [11, 6]
      [new car position] =  [12, 6]

      Map of symbol

      -  -  -  -  -  -  -  P  -  -  Q  -  -  -  -  L  -  -  -  

      -  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  -  

      -  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  O  

      -  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  -  

      -  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  -  

      A  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  -  

      -  -  N  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

      -  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  -  

      -  #  #  #  #  #  S  #  #  #  #  #  -  #  #  #  #  #  -  

      -  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  -  

      -  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  -  

      -  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  E  

      -  -  -  -  H  -  T  -  -  -  -  R  -  -  -  -  -  -  -  

      B  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  F  

      -  #  #  #  #  #  -  #  #  #  #  #  I  #  #  #  #  #  -  

      -  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  -  

      -  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  -  

      C  #  #  #  #  #  -  #  #  #  #  #  -  #  #  #  #  #  M  

      -  -  -  -  -  -  -  -  -  -  K  J  -  -  -  -  -  -  - 
