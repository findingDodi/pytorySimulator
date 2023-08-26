# Pytory Simulator

## Requirements
- something to render things
- game logic
- vehicles
  - limited slots
  - speed
  - destination
- buildings
  - factories
    - input and/or output
    - requests
    - production states
  - parking lot
- resources
  - stackable
    - stack size

## TODO 
- fix resource properties (buildings and vehicles)

## stock
- input_resources = {}
  - in den input_resources -> list für versch. resources
- def add_to_item_stocks
  - items werden zum jeweiligen item stock hinzugefügt
- process 
  - muss abfragen, ob externe Ressourcen benötigt werden
  - wenn ja
      - prüfen ob items in item_stocks vorhanden
          - nicht da ?
              - items anfragen (über vehicle)
          - wenn da
              - weiter mit process (ressourcen verarbeiten)
  - wenn nein
      - weiter mit process