#! /usr/bin/python3
import validation_dungeon
import json

start_ref = int(input("Start reference: "))
end_ref = int(input("End reference: "))
data_location = input("Question schema: ")
period = int(input("Period: "))

resps = validation_dungeon.ValidationDungeon(data_location, start_ref, end_ref, period)
current_outputs = []

for i in resps:
    current_outputs.append(resps.check_should_fail_status(i))

output_backdata_location = input("Back data output: ")
resps.output_back_data(output_backdata_location)
output_current_location = input("Current period location: ")
with open(output_current_location, "w+") as file:
    file.write(json.dumps(current_outputs, indent=4))

