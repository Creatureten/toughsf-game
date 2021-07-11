extends Spatial

var module_load = preload("res://Assets/Scenes/Module.tscn")

var symmetry_load = preload("res://Assets/Scenes/SymmetryContainer.tscn")
var symmetry = 1
var camera_dragging = false
var module_dragging = false
var sensitivity = 0.0001
var cur_module_index = 0
var selected_group 	#reference to currently selected module
# Declare member variables here. Examples:
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	if not has_signal("ModuleInteraction"):
		add_user_signal("ModuleInteraction")
	
	$symmetry_counter.text = "Symmetry:" + String(symmetry)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	
	pass

func _input(event):
	
	#Camera controls
	if event.is_action_pressed("middle_mouse"):
		camera_dragging = true
	if event.is_action_released("middle_mouse"):
		camera_dragging = false
	if event is InputEventMouseMotion and camera_dragging == true:
		$Cameraman/Arm.rotate_x(event.speed.y * sensitivity)
		$Cameraman.rotate_y(event.speed.x * sensitivity)
		
		
	if event.is_action_pressed("scroll_up") and event.is_action_pressed("middle_mouse"):
		$Cameraman/Arm/Camera.translation = $Arm/Camera.translation + Vector3(0,0,1)
	if event.is_action_pressed("scroll_down") and event.is_action_pressed("middle_mouse"):
		$Cameraman/Arm/Camera.translation = $Arm/Camera.translation - Vector3(0,0,1)
		
		
		
	if event.is_action_pressed("scroll_up") and not event.is_action_pressed("middle_mouse"):
		symmetry = symmetry + 1
	if event.is_action_pressed("scroll_down") and not event.is_action_pressed("middle_mouse"):
		if symmetry > 1:
			symmetry = symmetry - 1
	$symmetry_counter.text = "Symmetry:" + String(symmetry)




func _on_ModuleList_item_selected(index):
	cur_module_index = index
	var nodes = $Ship.get_children()
	if nodes.size() == 0:
		var new = symmetry_load.instance()
		add_child(new)
		new.create_group(1, index, Vector3(0,0,0),Vector3(0,0,0))
		select_new_group(new)



func _on_Module_input_event(camera, event, click_position, click_normal, shape_idx, module):
	var symmetry_group = module.get_parent()
	if event.is_action_pressed("left_mouse"):
		if not module_dragging:
			var new = symmetry_load.instance()
			add_child(new)
			if pow(click_position.x,2) + pow(click_position.y,2) < 0.01:
				new.create_group(1, 0, Vector3(0,0,click_position.z) , Vector3(0,0,1))
			else:
				new.create_group(symmetry, 0, click_position, click_normal)
			select_new_group(new)
			module_dragging = true
		else:
			module_dragging = false
			
	if module_dragging and module.get_parent() != selected_group:
		if is_instance_valid(selected_group):
			selected_group.move(symmetry, click_position, click_normal)
		else:
			module_dragging = false
			
	if event.is_action_pressed("right_mouse"):
		if symmetry_group == selected_group:
			symmetry_group.queue_free()
		else:
			select_new_group(symmetry_group)
		
	pass # Replace with function body.

func select_new_group(symmetry_group):
	print(symmetry_group)
	if is_instance_valid(selected_group):
		selected_group.module_material.flags_transparent = false	#return the opacity of the previously selected module
	selected_group = symmetry_group				#newly selected module
	symmetry_group.module_material.flags_transparent = true
