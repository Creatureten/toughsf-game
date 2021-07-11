extends RigidBody


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	if not has_signal("ModuleInteraction"):
		add_user_signal("ModuleInteraction")
	if not is_connected("ModuleInteraction", get_parent().get_parent(), "_on_Module_input_event"):
		connect("ModuleInteraction", get_parent().get_parent(), "_on_Module_input_event")
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass



func _on_Module_input_event(camera, event, click_position, click_normal, shape_idx):
	emit_signal("ModuleInteraction", camera, event, click_position, click_normal, shape_idx, self)
