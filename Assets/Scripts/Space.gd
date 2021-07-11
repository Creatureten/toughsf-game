extends Spatial


# Declare member variables here. Examples:
var objectList = []
var timewarp = 1
var gravityForce
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
				gravityForce = (_i.translation -_j.translation).normalized() / pow(getDistance(_i, _j),2) * pow(timewarp,2)
				_i.linear_velocity = _i.linear_velocity - gravityForce #* _j.masss
func getDistance(nodeOne, nodeTwo):
	return nodeOne.translation.distance_to(nodeTwo.translation)

 


func _on_Timewarphalf_pressed():
	timewarp = timewarp * 0.5
	for _i in objectList:
		_i.linear_velocity = _i.linear_velocity * 0.5
		_i.angular_velocity = _i.angular_velocity * 0.5
	pass # Replace with function body.


func _on_Timewarpdouble_pressed():
	timewarp = timewarp * 2
	for _i in objectList:
		_i.linear_velocity = _i.linear_velocity * 2
		_i.angular_velocity = _i.angular_velocity * 2
	pass # Replace with function body.
