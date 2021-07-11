extends MarginContainer


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func _on_SandboxButton_pressed():
	#get_tree().change_scene()
	pass # Replace with function body.

func _on_DesignerButton_pressed():
	get_tree().change_scene("res://Assets/Scenes/Designer.tscn")


func _on_OptionButton_pressed():
	pass # Replace with function body.


func _on_ExitButton_pressed():
	get_tree().quit()

