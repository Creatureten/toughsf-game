extends MarginContainer


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	if Input.is_action_pressed("ui_cancel"):
		$PauseMenu.visible = true

func _on_SandboxButton_pressed():
	#get_tree().change_scene()
	pass # Replace with function body.


func _on_ShipButton_pressed():
	pass # Replace with function body.


func _on_ModuleButton_pressed():
	get_tree().change_scene("res://Assets/Scenes/Module editor.tscn")


func _on_OptionButton_pressed():
	pass # Replace with function body.


func _on_ExitButton_pressed():
	get_tree().quit()


func _on_ReturnButton_pressed():
	$PauseMenu.visible = false
