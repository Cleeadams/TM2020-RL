# TM 2020

## Setup
1. Install TM 2020
	- May need to pay for the club memebership $20 / year.
2. Install OpenPlanet
3. Install Plugin Record Raw Vehicle Data
4. Install packages in requirement.txt
5. Create a .env file in the config folder
	- Add MONGO_NM and MONGO_PWD environment variables
## Plugin
- [Record Raw Vehicle Data](https://openplanet.dev/plugin/recordrawvehicledata) from OpenPlanet by XetroV

## Data Wanted

- Speed
- Position
- Roll
- Tilt/Pitch
- Inputs (Froward, Left, Right)
- Wheels Sliding
- Wheels Contact
- Direction
- Time
- Acceleration
- Distance to next turn
- Direction of next turn

## Data Have

- Speed
- Position
- Roll
- Tilt/Pitch
- Inputs
- Wheels Sliding
- All Wheels Grounded
- Direction
- Time

$\newline$
- Acceleration = $\frac{\Delta v}{\Delta t}$
- Single Wheel Contact = DamperLen > .1?
	- Still struggling to get this from data source


## Problems to solve
1. How to control the car
	- opencv?
	- Angelscript file
	- Plugin?
		- Haven't found anything yet

2. Get track data
	- Get distance till next turn
	- Direction of next turn