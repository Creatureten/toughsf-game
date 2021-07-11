extends Spatial
var symmetry_count = 1
var symmetry_members = []
var module_material = preload("res://Assets/Media/ModuleMaterial.tres").duplicate()
# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func create_group(symmetry, module, position, normal):
	symmetry_count = symmetry
	var angular_separation = 2*PI/(symmetry_count)
	for _i in symmetry_count:
		var rotated_position = Vector2(position.x, position.y).rotated(angular_separation*_i)
		var rotated_normal = Vector2(normal.x, normal.y).rotated(angular_separation*_i)
		rotated_position = Vector3(rotated_position.x, rotated_position.y, position.z)
		rotated_normal = Vector3(rotated_normal.x, rotated_normal.y, normal.z)
		symmetry_members.append(spawnModule(0, rotated_position , rotated_normal))

func move(symmetry, position, normal):
	if symmetry_count < symmetry:
		for _i in symmetry - symmetry_count:
			symmetry_members.append(spawnModule(0, position , normal))
	if symmetry_count > symmetry:
		for _i in symmetry_count - symmetry:
			symmetry_members.pop_back().queue_free()
	
	symmetry_count = symmetry
	var angular_separation = 2*PI/(symmetry_count)
	for _i in symmetry_members.size():
		var rotated_position = Vector2(position.x, position.y).rotated(angular_separation*_i)
		var rotated_normal = Vector2(normal.x, normal.y).rotated(angular_separation*_i)
		rotated_position = Vector3(rotated_position.x, rotated_position.y, position.z)
		rotated_normal = Vector3(rotated_normal.x, rotated_normal.y, normal.z)
		symmetry_members[_i].translation = rotated_position + rotated_normal
		symmetry_members[_i].look_at(rotated_position, Vector3(0,1,0))
	
func spawnModule(index, position, direction):
	var newModule = get_parent().module_load.instance()
	add_child(newModule)
	newModule.get_node("Model").set_surface_material(0, module_material)
	newModule.translation = position + direction
	newModule.look_at(position, Vector3(0,1,0))
	return newModule
	
