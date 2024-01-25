#2. light on/off

def toggle_light(light_on):
    """
    Toggle the state of the light.

    If the light is on, turn it off. If the light is off, turn it on.

    Returns the new state of the light.
    """
    if light_on:
        # light is on, turn it off
        light_on = False #关灯
        print("Light turned off.")
    else:
        # light is off, turn it on
        light_on = True  #开灯
        print("Light turned on.")
    return light_on #返回更新后的灯的状态


# Test the function
new_state = toggle_light(True)
print("New state:", new_state)
print("-" * 30)  # Separator
new_state = toggle_light(False)
print("New state:", new_state)
