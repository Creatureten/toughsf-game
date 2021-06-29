extends Spatial


# Declare member variables here. Examples:
var objectList = []
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	for _i in self.get_children ():
		if _i is RigidBody:
			objectList.append(_i)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _physics_process(delta):
	for _i in objectList:
		for _j in objectList:
			if _i != _j:
				_i.linear_velocity = _i.linear_velocity - (_i.translation -_j.translation) / pow(getDistance(_i, _j),2)

func getDistance(nodeOne, nodeTwo):
	print(nodeOne.translation.distance_to(nodeTwo.translation))
	return nodeOne.translation.distance_to(nodeTwo.translation)
