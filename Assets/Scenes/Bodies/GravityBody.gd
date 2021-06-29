extends RigidBody


# Declare member variables here. Examples:
# var a = 2
var gravitational_parameter = 1

# Called when the node enters the scene tree for the first time.
func _ready():
	linear_velocity = Vector3(0,6,0)


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
