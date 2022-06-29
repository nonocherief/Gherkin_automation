Feature: Test Archicad
    In order to test in Archicad,
    First step is to connect to the program,
    By command steps test the functions,
    Based on Archicad commands.


    Scenario: Wall build
    Given Archicad is running 
    And there is no any exist walls
    When By command build the walls
    Then The wall should be build

    Scenario: Window on the wall
    Given The window submenu is selected
    When Click on the choosen wall
    Then Window is on the wall

